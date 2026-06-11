"""
SIMULACIÓN DE MURMURACION DE AVES (Boids Algorithm)
====================================================
Basado en el algoritmo de Craig Reynolds (1986)
Solo necesitas: pip install pygame numpy

Cómo funciona en resumen:
  Cada pájaro mira a sus vecinos cercanos y aplica 3 reglas:
  1. Separación  → no chocar
  2. Alineación  → ir en la misma dirección
  3. Cohesión    → acercarse al grupo
"""

import pygame
import numpy as np
import sys

# ─────────────────────────────────────────────
# PARÁMETROS — AQUÍ ES DONDE PUEDES EXPERIMENTAR
# ─────────────────────────────────────────────

ANCHO = 1400          # Ancho de la ventana en píxeles
ALTO  = 720           # Alto de la ventana en píxeles

NUM_PAJAROS = 200     # Cuántos pájaros. Más = más impresionante pero más lento

RADIO_VISION = 100     # Qué tan lejos "ve" cada pájaro (en píxeles)
                      # Más grande = grupos más grandes y fluidos
                      # Más pequeño = muchos grupos pequeños

VELOCIDAD_MIN = 2.5   # Velocidad mínima (los pájaros siempre se mueven)
VELOCIDAD_MAX = 20.5   # Velocidad máxima

# Pesos de cada regla — aquí está la magia visual
PESO_SEPARACION = 4.8  # Qué tanto se evitan entre sí
                       # Súbelo → se dispersan, bajan → se amontonan

PESO_ALINEACION = 1.5  # Qué tanto copian la dirección de sus vecinos
                       # Súbelo → movimiento muy sincronizado y fluido

PESO_COHESION   = 0.2  # Qué tanto se atraen hacia el centro del grupo
                       # Súbelo → grupos muy densos y compactos

RADIO_SEPARACION = 50  # Radio más pequeño para la regla de "no choquen"
                       # Si dos pájaros están más cerca que esto, se alejan

# Colores
COLOR_FONDO  = (5, 5, 20)       # Azul muy oscuro (cielo nocturno)
COLOR_PAJARO = (200, 220, 255)  # Azul claro casi blanco
COLOR_BRILLO = (255, 255, 255)  # Para el punto de brillo del pájaro

FPS = 60  # Fotogramas por segundo


# ─────────────────────────────────────────────
# CLASE PAJARO
# Representa a un solo pájaro con su posición y velocidad
# ─────────────────────────────────────────────

class Pajaro:
    def __init__(self):
        # Posición inicial aleatoria en la pantalla.
        # Generates a random number between 0 and ANCHO/ALTO.
        self.pos = np.array([
            np.random.uniform(0, ANCHO),
            np.random.uniform(0, ALTO)
        ], dtype=float)

        # Velocidad inicial aleatoria en cualquier dirección
        # np.random.uniform(0, 2*np.pi) da un número entre 0 y 2pi, esto calcula el ángulo
        # de dirección a donde se moverá el pájaro en la siguiente iteración. 2pi radianes
        # indica una circunferencia completa, significa 0 o 360°. 
        angulo = np.random.uniform(0, 2 * np.pi)
        
        # en el circulo unitario (radio=1), cualquier punto sobre la circunferencia, se puede
        # expresar como (x,y) = (cos(ang), sen(ang)), donde ang es el angulo medido desde el eje x.
        # Entonces, ya teniendo un vector unitario (x,y), si le multiplicamos el parametro velocidad 
        # a este vector, podemos encontrar la velocidad. 

        self.vel = np.array([np.cos(angulo), np.sin(angulo)]) * VELOCIDAD_MAX

    def actualizar(self, todos_los_pajaros):
        """
        Calcula las 3 fuerzas y actualiza la velocidad del pájaro.
        Este método se llama una vez por frame para cada pájaro.
        """

        # Primero encontramos a los vecinos cercanos
        vecinos = self._encontrar_vecinos(todos_los_pajaros)

        if len(vecinos) > 0:
            # Calculamos las 3 fuerzas
            sep = self._separacion(vecinos) * PESO_SEPARACION
            ali = self._alineacion(vecinos) * PESO_ALINEACION
            coh = self._cohesion(vecinos)   * PESO_COHESION

            # Sumamos las fuerzas a la velocidad actual
            self.vel += sep + ali + coh

        # Limitamos la velocidad para que no vaya demasiado rápido ni demasiado lento
        self._limitar_velocidad()

        # Movemos el pájaro según su velocidad
        self.pos += self.vel

        # Si sale de la pantalla, aparece por el lado opuesto (efecto toroidal)
        self.pos[0] %= ANCHO
        self.pos[1] %= ALTO

    def _encontrar_vecinos(self, todos):
        """
        Devuelve una lista con los pájaros que están dentro del radio de visión.
        Excluye al propio pájaro.
        """
        vecinos = []
        for otro in todos:
            if otro is self:
                continue
            distancia = np.linalg.norm(self.pos - otro.pos)
            if distancia < RADIO_VISION:
                vecinos.append(otro)
        return vecinos

    def _separacion(self, vecinos):
        """
        REGLA 1: Alejarse de los pájaros demasiado cercanos.
        
        Si un vecino está muy cerca, calculamos un vector que apunta
        HACIA AFUERA (lejos de ese vecino), proporcional a qué tan cerca está.
        Sumamos todos esos vectores.
        """
        fuerza = np.zeros(2)
        for otro in vecinos:
            diff = self.pos - otro.pos
            distancia = np.linalg.norm(diff)
            if distancia < RADIO_SEPARACION and distancia > 0:
                # Mientras más cerca, más fuerte la repulsión
                fuerza += diff / distancia
        return fuerza

    def _alineacion(self, vecinos):
        """
        REGLA 2: Volar en la misma dirección que los vecinos.
        
        Calculamos la velocidad promedio de todos los vecinos
        y ajustamos la nuestra para parecerse a esa.
        """
        vel_promedio = np.mean([v.vel for v in vecinos], axis=0)
        # Devolvemos la diferencia: cuánto nos tenemos que ajustar
        return vel_promedio - self.vel

    def _cohesion(self, vecinos):
        """
        REGLA 3: Moverse hacia el centro del grupo.
        
        Calculamos la posición promedio de los vecinos (el "centro de masa")
        y devolvemos un vector que apunta hacia allá.
        """
        centro = np.mean([v.pos for v in vecinos], axis=0)
        # Vector que apunta del pájaro hacia el centro del grupo
        return centro - self.pos

    def _limitar_velocidad(self):
        """
        Asegura que la velocidad esté entre VELOCIDAD_MIN y VELOCIDAD_MAX.
        Primero calculamos la magnitud (qué tan rápido va),
        luego la escalamos si es necesario.
        """
        magnitud = np.linalg.norm(self.vel)
        if magnitud > VELOCIDAD_MAX:
            self.vel = (self.vel / magnitud) * VELOCIDAD_MAX
        elif magnitud < VELOCIDAD_MIN and magnitud > 0:
            self.vel = (self.vel / magnitud) * VELOCIDAD_MIN

    def dibujar(self, pantalla):
        """
        Dibuja el pájaro como un triángulo apuntando en su dirección de movimiento.
        Calculamos el ángulo de la velocidad para rotar el triángulo correctamente.
        """
        # Ángulo de movimiento en radianes
        angulo = np.arctan2(self.vel[1], self.vel[0])

        # Tamaño del triángulo
        largo = 7   # longitud del pájaro
        ancho = 3   # ancho de las "alas"

        # Los 3 vértices del triángulo (nariz, ala izq, ala der)
        # antes de rotar, el pájaro "apunta" hacia la derecha
        puntos_local = np.array([
            [ largo,  0    ],   # punta delantera
            [-largo,  ancho],   # ala trasera izquierda
            [-largo, -ancho],   # ala trasera derecha
        ])

        # Matriz de rotación 2D
        cos_a, sin_a = np.cos(angulo), np.sin(angulo)
        rot = np.array([[cos_a, -sin_a], [sin_a, cos_a]])

        # Rotamos y trasladamos a la posición del pájaro
        puntos = [rot @ p + self.pos for p in puntos_local]

        # Dibujamos el triángulo relleno
        pygame.draw.polygon(pantalla, COLOR_PAJARO, puntos)

        # Pequeño punto blanco en la punta para dar sensación de profundidad
        pygame.draw.circle(pantalla, COLOR_BRILLO,
                           (int(self.pos[0]), int(self.pos[1])), 1)


# ─────────────────────────────────────────────
# FUNCIÓN PRINCIPAL — EL LOOP DEL JUEGO
# ─────────────────────────────────────────────

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Murmuración de Aves")
    reloj = pygame.time.Clock()

    # Crear todos los pájaros
    pajaros = [Pajaro() for _ in range(NUM_PAJAROS)]

    print("Controles:")
    print("  ESC o cerrar ventana → salir")
    print("  R → reiniciar con nuevas posiciones")

    # ── LOOP PRINCIPAL ──
    # Este loop se repite FPS veces por segundo
    while True:

        # 1. Manejar eventos (teclas, cerrar ventana)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_r:
                    pajaros = [Pajaro() for _ in range(NUM_PAJAROS)]

        # 2. Actualizar la lógica de cada pájaro
        for pajaro in pajaros:
            pajaro.actualizar(pajaros)

        # 3. Dibujar todo en pantalla
        pantalla.fill(COLOR_FONDO)          # Borrar frame anterior
        for pajaro in pajaros:
            pajaro.dibujar(pantalla)

        # Mostrar FPS en el título (útil para saber si va fluido)
        fps_actual = reloj.get_fps()
        pygame.display.set_caption(f"Murmuración | {fps_actual:.0f} FPS | {NUM_PAJAROS} pájaros")

        pygame.display.flip()               # Mostrar el frame en pantalla
        reloj.tick(FPS)                     # Esperar para mantener los FPS


if __name__ == "__main__":
    main()
