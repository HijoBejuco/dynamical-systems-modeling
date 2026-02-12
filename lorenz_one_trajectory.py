import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de Lorenz
sigma = 10
rho = 28
beta = 8/3

# Sistema de ecuaciones
def lorenz(x, y, z, dt):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    x = x + dx * dt
    y = y + dy * dt
    z = z + dz * dt

    return x, y, z

# Tiempo
dt = 0.01
steps = 16000

# Condiciones iniciales
x, y, z = 1.0, 1.0, 1.0

# Guardar trayectoria
xs, ys, zs = [], [], []

# _ is when the i is not needed. so we just want the iteration
# and dont want to do anything with the counter e.j 'i'. 
for _ in range(steps):
    x, y, z = lorenz(x, y, z, dt)
    xs.append(x)
    ys.append(y)
    zs.append(z)

# --- Animación ---
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection='3d')

ax.set_xlim(-25, 25)
ax.set_ylim(-35, 35)
ax.set_zlim(0, 50)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Add titles and labels
ax.set_title('Simulación Atractor de Lorenz @hijoarbol')
ax.set_xlabel('velocidad convectiva')
ax.set_ylabel('diferencia de temperaturas ascendente-descendente')
ax.set_zlabel('mezcla térmica del sistema')

line, = ax.plot([], [], [], lw=0.8)

def update(frame):
    line.set_data(xs[:frame], ys[:frame])
    line.set_3d_properties(zs[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=steps, interval=1)

plt.show()
