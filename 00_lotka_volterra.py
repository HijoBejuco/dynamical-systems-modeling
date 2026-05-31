# The Callable is any object that can be called (funct, method, class)
from typing import List, Tuple, Dict, Union, Callable
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from src.utils import (
                       euler_method,
                       lotka_volterra
                       )



params1 = (1.0, 0.1, 0.075, 1.5)     # alpha, beta, delta, gamma
params2 = (1.0, 0.1, 0.075, 1.0)     # alpha, beta, delta, gamma
params3 = (1.0, 0.1, 0.075, 0.5)     # alpha, beta, delta, gamma

l_v_results1 = euler_method(
    lotka_volterra,
    np.array([10.0, 5.0]), # y0: 10 preys and 5 predators
    0.0,                   # t0: initial time
    0.01,                  # delta
    800,                   # iterations
    *params1                # lotka volterra parameters of the equations
)

l_v_results2 = euler_method(
    lotka_volterra,
    np.array([10.0, 5.0]), # y0: 10 preys and 5 predators
    0.0,                   # t0: initial time
    0.01,                  # delta
    800,                   # iterations
    *params2                # lotka volterra parameters of the equations
)

l_v_results3 = euler_method(
    lotka_volterra,
    np.array([10.0, 5.0]), # y0: 10 preys and 5 predators
    0.0,                   # t0: initial time
    0.01,                  # delta
    800,                   # iterations
    *params3                # lotka volterra parameters of the equations
)



df1 = l_v_results1
df2 = l_v_results2
df3 = l_v_results3

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0,1].set_xlim(df1.iterations.min(), df1.iterations.max())
ax[0,1].set_ylim(0, max(df1.y1.max(), df2.y1.max(), df3.y1.max()) * 1.1)
ax[0,1].set_title('Poblacion predadores en el tiempo,\nvariando el gamma. @hijoarbol')
ax[0,1].set_xlabel('Tiempo')
ax[0,1].set_ylabel('Población')

# Líneas vacías que se van llenando
line1, = ax[0,1].plot([], [], color='steelblue', label='gamma=1.5', linewidth=1.5)
line2, = ax[0,1].plot([], [], color='red',       label='gamma=1.0', linewidth=1.5)
line3, = ax[0,1].plot([], [], color='green',     label='gamma=0.5', linewidth=1.5)
ax[0,1].legend()

def update(frame):
    line1.set_data(df1.iterations[:frame], df1.y1[:frame])
    line2.set_data(df2.iterations[:frame], df2.y1[:frame])
    line3.set_data(df3.iterations[:frame], df3.y1[:frame])
    return line1, line2, line3

ani = FuncAnimation(
    fig,
    update,
    frames=len(df1),  # cuántos frames en total
    interval=20,      # ms entre frames (más bajo = más rápido)
    blit=True
)

plt.tight_layout()
plt.show()