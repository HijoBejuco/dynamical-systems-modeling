

# Developing the animation that compares chaotic curves
# with very simmilar initial conditions. 

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Sample data
x = [i for i in range(100)]
y1 = [i**0.5 for i in x]  # Example data for the red curve
y2 = [i**0.3 for i in x]  # Example data for the black curve

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
line1, = ax.plot(x, y1, 'r-', label='Red Curve')  # Red curve
line2, = ax.plot(x, y2, 'k-', label='Black Curve')  # Black curve

# Set up the plot limits
ax.set_xlim(0, max(x))
ax.set_ylim(0, max(max(y1), max(y2)))
ax.legend()

# The update function is responsible for updating the data in the plot
# for each frame. The function receives a frame as a parameter, and
# updates the data in the plot to show the data up to that point in time.
# The set_data() sets the x and y fata of the line, changing what is
# displayed in the plot. 
def update(frame):
    line1.set_data(x[:frame], y1[:frame])
    line2.set_data(x[:frame], y2[:frame])
    return line1, line2

# Create the animation
# A frame: represents a single step in the animation, each frame 
# updates the plot to show the data up to that point in time. 
# the frame can be an iterable or an integer. Also with the 
# frame, the speed of the animation can be controlled.
ani = animation.FuncAnimation(
    fig, 
    update, 
    frames= range(0, 100, 5), 
    blit=True
)

# Show the plot
plt.show()


