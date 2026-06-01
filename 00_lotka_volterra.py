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

#################################################################################################







#################################################################################################
################### SECCIÓN DE CRECIMIENTO RATONES CON ZORROS ###################################


params_rat_zor = (1.0, 0.1, 0.075, 1.5)     # alpha, beta, delta, gamma

ratones_con_zorros_resultado = euler_method(
    lotka_volterra,
    np.array([10.0, 5.0]), # y0: 10 preys and 5 predators
    0.0,                   # t0: initial time
    0.01,                  # delta
    800,                   # iterations
    *params_rat_zor                # lotka volterra parameters of the equations
)

df_rat_zor = ratones_con_zorros_resultado

ax[1,0].set_xlim(df_rat_zor.iterations.min(), df_rat_zor.iterations.max())
ax[1,0].set_ylim(0, df_rat_zor.y0.max() * 1.1)
ax[1,0].set_title('Poblacion ratones viviendo con zorros\nvariando el gamma. @hijoarbol')
ax[1,0].set_xlabel('Tiempo')
ax[1,0].set_ylabel('Población')

# Líneas vacías que se van llenando
line_rat_zor, = ax[1,0].plot([], [], color='purple', label='gamma=1.5', linewidth=1.5)

ax[1,0].legend()

def update_rat_zor(frame):
    line_rat_zor.set_data(df_rat_zor.iterations[:frame], df_rat_zor.y0[:frame])
    return line_rat_zor,

ani_rat_zor = FuncAnimation(
    fig,
    update_rat_zor,
    frames=len(df_rat_zor),  # cuántos frames en total
    interval=20,      # ms entre frames (más bajo = más rápido)
    blit=True
)

#################################################################################################













#################################################################################################
################### SECCIÓN DE CRECIMIENTO EXPONENCIAL SIN RATONES ##############################

# Parámetros iniciales
R0 = 10.0      # población inicial de presas
alpha = 1.0    # tasa de crecimiento
t = np.linspace(0, 5, 250)  # tiempo

# Solución analítica
R = R0 * np.exp(alpha * t)

# Crear subplot para la animación
ax[1,1].set_xlim(t.min(), t.max())
ax[1,1].set_ylim(0, R.max() * 1.1)
ax[1,1].set_title('Crecimiento exponencial de presas\nsin predadores. @hijoarbol')
ax[1,1].set_xlabel('Tiempo')
ax[1,1].set_ylabel('Población')

line_exp, = ax[1,1].plot([], [], color='purple', linewidth=1.5, label='R(t)=R0 exp(alpha t)')
ax[1,1].legend()

# Función de actualización
def update_exp(frame):
    line_exp.set_data(t[:frame], R[:frame])
    return line_exp,

ani3 = FuncAnimation(
    fig,
    update_exp,
    frames=len(t),
    interval=10,
    blit=True
)

#################################################################################################











plt.tight_layout()
plt.show()