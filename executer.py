# Developing the animation that compares chaotic curves
# with very simmilar initial conditions. 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.utils import logistic_eq_iterator

# Number of iterations
iterations = 50

# Sample data
x = [i for i in range(iterations)]
y1 = logistic_eq_iterator(4, 0.4, iterations)#[i**0.5 for i in x]
y2 = logistic_eq_iterator(4, 0.400001, iterations)#[i**0.3 for i in x]  
y3 = logistic_eq_iterator(3.5, 0.1, iterations)

# Initialize the figure and axis
# Here fig represents the entire figure in which the plot is drawn.
# ax is an axes obj, it represents a single plot inside the figure, it 
# is the area where the data is plotted, and it contains the x and y axis,
# the plot itself, labels, etc.
fig, ax = plt.subplots()

# the , after line1 and line2 is necessary because ax.plot()
# returns a tuple, because ax.plot() can plot multiple lines,
# if we pass multiple parameters to it. In this case, cause we are
# passing just 1 line, we just need the first element of the tuple.
#line1, = ax.plot(x, y1, 'r--', label='0.4')  # Red curve
#line2, = ax.plot(x, y2, 'k-', label='0.400001')  # Black curve
line3, = ax.plot(x, y3, 'g*-', label='Periodic')  # Black curve

# Set up the plot limits
ax.set_xlim(0, max(x))
ax.set_ylim(0, max(max(y1)+0.1, max(y2)+0.1, max(y3)+0.1))
ax.legend()

# Add titles and labels
ax.set_title('Simulación Ecuación logística por Alejandro Espinal')
ax.set_xlabel('Tiempo')
ax.set_ylabel('% población con respecto al máximo posible')

# The update function is responsible for updating the data in the plot
# for each frame. The function receives a frame as a parameter, and
# updates the data in the plot to show the data up to that point in time.
# The set_data() sets the x and y fata of the line, changing what is
# displayed in the plot. 
def update(frame):
    #line1.set_data(x[:frame], y1[:frame])
    #line2.set_data(x[:frame], y2[:frame])
    line3.set_data(x[:frame], y3[:frame])
    return [line3] #line1, line2

# Create the animation
# A frame: represents a single step in the animation, each frame 
# updates the plot to show the data up to that point in time. 
# the frame can be an iterable or an integer. Also with the 
# frame, the speed of the animation can be controlled.
ani = animation.FuncAnimation(
    fig, 
    update, 
    frames= range(0, iterations, 1), 
    blit=True,
    interval=600 # delay btween frames in miliseconds
)



# Save the animation as an MP4 file
# ani.save('simulation.gif', writer='pillow', fps=7)

# Show the plot
plt.show()






# Developing the animation that compares chaotic curves
# with very simmilar initial conditions.    vbvufzz