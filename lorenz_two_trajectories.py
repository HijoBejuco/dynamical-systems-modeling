import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Parámetros de Lorenz
# -----------------------------
sigma = 10
rho = 28
beta = 8/3

def lorenz(x, y, z, dt):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    x += dx * dt
    y += dy * dt
    z += dz * dt

    return x, y, z

# -----------------------------
# Tiempo
# -----------------------------
dt = 0.01
steps = 12000

# -----------------------------
# Dos condiciones iniciales
# (casi idénticas)
# -----------------------------
x1, y1, z1 = 1.0, 1.0, 1.0
x2, y2, z2 = 1.0001, 1.0, 1.0   # diferencia mínima

xs1, ys1, zs1 = [], [], []
xs2, ys2, zs2 = [], [], []

for _ in range(steps):
    x1, y1, z1 = lorenz(x1, y1, z1, dt)
    x2, y2, z2 = lorenz(x2, y2, z2, dt)

    xs1.append(x1)
    ys1.append(y1)
    zs1.append(z1)

    xs2.append(x2)
    ys2.append(y2)
    zs2.append(z2)

# -----------------------------
# Animación estilo cinematográfico
# -----------------------------
plt.style.use("dark_background")

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')

# Fondo negro real
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_xlim(-25, 25)
ax.set_ylim(-35, 35)
ax.set_zlim(0, 50)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_title('Sensibilidad a condiciones iniciales\nAtractor de Lorenz\n@hijoarbol',
             fontsize=14)

# Colores contrastantes
line1, = ax.plot([], [], [], lw=1.2, color='cyan',
                 label='IC1: (1.0, 1.0, 1.0)')

line2, = ax.plot([], [], [], lw=1.2, color='orange',
                 label='IC2: (1.0001, 1.0, 1.0)')

legend = ax.legend(loc='upper left', frameon=False, fontsize=9)

for text in legend.get_texts():
    text.set_color("white")


# Vista más atractiva
ax.view_init(elev=25, azim=45)

# Efecto de rastro dinámico
trail = 5000  # longitud del rastro visible

def update(frame):

    start = max(frame - trail, 0)

    line1.set_data(xs1[start:frame], ys1[start:frame])
    line1.set_3d_properties(zs1[start:frame])

    line2.set_data(xs2[start:frame], ys2[start:frame])
    line2.set_3d_properties(zs2[start:frame])

    # rotación lenta de cámara
    ax.view_init(elev=25, azim=45 + frame * 0.02)

    return line1, line2

ani = FuncAnimation(fig, update, frames=steps, interval=10)

plt.show()
