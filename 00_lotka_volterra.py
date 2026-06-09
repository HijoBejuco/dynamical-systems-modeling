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
################### INICIO SECCIÓN SERIE DE TIEMPO ZORROS-RATONES ############################

params_zorro_rat = (1.0, 0.1, 0.075, 1.5)     # alpha, beta, delta, gamma

l_v_zorro_rat = euler_method(
    lotka_volterra,
    np.array([10.0, 5.0]), # y0: 10 preys and 5 predators
    0.0,                   # t0: initial time
    0.01,                  # delta
    2000,                   # iterations
    *params_zorro_rat                # lotka volterra parameters of the equations
)



df_zorro_rat = l_v_zorro_rat


ax[0,0].set_xlim(df_zorro_rat.iterations.min(), df_zorro_rat.iterations.max())
ax[0,0].set_ylim(0, max(df_zorro_rat.y0.max(), df_zorro_rat.y1.max()) * 1.1)
ax[0,0].set_title('Poblacion zorros y ratones,\nen el tiempo. @hijoarbol')
ax[0,0].set_xlabel('Tiempo')
ax[0,0].set_ylabel('Población')

# Líneas vacías que se van llenando
line_zorros, = ax[0,0].plot([], [], color='orange', label='zorros', linewidth=1.5)
line_ratones, = ax[0,0].plot([], [], color='silver', label='ratones', linewidth=1.5)

ax[0,0].legend()

def update_zorros_ratones(frame):
    line_zorros.set_data(df_zorro_rat.iterations[:frame], df_zorro_rat.y1[:frame])
    line_ratones.set_data(df_zorro_rat.iterations[:frame], df_zorro_rat.y0[:frame])

    return line_zorros, line_ratones

ani_serie_tiempo_zorros_rat = FuncAnimation(
    fig,
    update_zorros_ratones,
    frames=len(df_zorro_rat),  # cuántos frames en total
    interval=1,      # ms entre frames (más bajo = más rápido)
    blit=True
)



################### FIN SECCIÓN SERIE DE TIEMPO ZORROS-RATONES ############################
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


##################################################################
######################## PHASE DIAGRAM ###########################

# params_zorro_rat = (1.0, 0.5, 0.2, 0.6)     # alpha, beta, delta, gamma

# l_v_phase_space = euler_method(
#     lotka_volterra,
#     np.array([8.0, 4.0]), # y0: 10 preys and 5 predators
#     0.0,                   # t0: initial time
#     0.001,                  # delta
#     50000,                   # iterations
#     *params_zorro_rat                # lotka volterra parameters of the equations
# )



# df_phase = l_v_phase_space


# fig, ax = plt.subplots()

# ax.set_xlim(0, max(df_phase.y0.max(), df_phase.y1.max()) * 1.1)
# ax.set_ylim(0, max(df_phase.y0.max(), df_phase.y1.max()) * 1.1)
# ax.set_title('zorros vs ratones,\ncomportamiento cíclico. @hijoarbol')
# ax.set_xlabel('población de zorros')
# ax.set_ylabel('población de ratones')

# # Líneas vacías que se van llenando
# line_phase_space, = ax.plot([], [], color='green', linewidth=1.5)



# def update_phase_space(frame):
#     line_phase_space.set_data(df_phase.y0[:frame], df_phase.y1[:frame])

#     return line_phase_space, 

# ani_phase_space = FuncAnimation(
#     fig,
#     update_phase_space,
#     frames=len(df_phase),  # cuántos frames en total
#     interval=0.0001,      # ms entre frames (más bajo = más rápido)
#     blit=True
# )




##################################################################









plt.tight_layout()
plt.show()