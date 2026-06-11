
# Index 
<ol><!-- Tag for ordered list -->
    <li><!-- list item -->
        <a href="#mathematics">Mathematics</a>
        <ul><!-- Tag for unordered list -->
            <li><a href="#two-dimensional-discrete-dynamical-systems">Two dimensional discrete dynamical systems</a></li>
            <li>
                <a href="#differential-equations">Differential equations</a>
                <ul>
                    <li><a href="#one-dimensional-differential-equations">One dimensional differential equations</a></li>
                    <li><a href="#two-dimensional-differential-equations">Two dimensional differential equations</a></li>                    
                    <li><a href="#computational-solutions">Computational solutions</a></li>                    
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <a href="#environmental-modeling">Environmental modeling</a>
        <ul>
            <li><a href="#plotting-in-three-dimensions-3d">Plotting in three dimensions 3D</a></li>
        </ul>
    </li>
</ol>


# Animations and Simulations
Here we will document some tools for excecute and create basic animations


## **Pygame**

### Coordinates in Pygame: 
The origin of the win, so we use (x,y) coordenates, is the upper left corner of the window. so, increasing y drives us towards down and increasing x drives us towards right.

### Speed / Velocity
Here, the speed is the change in position at each frame of every animated object

new position = current position + speed

for example, if the initial position is [100, 200] and the velocity is [14.5, 14.5], the next frame the position will be [114.5, 214.5]


### Main loop:
the animation/game in pygame always has a main loop, so it update the window at each iteration.



## **matplotlib.animation**
The basic example here is the animation of a time series, ploting gradually a time series into a chart. 

**Step 1:** create the figure with its axis, in this case we create a subplot of shape (2,2). Also, we must have the data, in this case we have 3 dataframes (df1, df2, df3) which have 3 columns (iterations, y0, y1)
```python 
fig, ax = plt.subplots(2, 2, figsize=(10, 8))
```

**Step 2:** configuring the plot

```python
ax[0,1].set_xlim(df1.iterations.min(), df1.iterations.max())
ax[0,1].set_ylim(0, max(df1.y1.max(), df2.y1.max(), df3.y1.max()) * 1.1)
ax[0,1].set_title('Poblacion predadores en el tiempo,\nvariando el gamma. @hijoarbol')
ax[0,1].set_xlabel('Tiempo')
ax[0,1].set_ylabel('Población')
```


**Step 3:** Create the empty lines, we are going to fill on each iteration.
the , after line1 and line2 is necessary because ax.plot() returns a tuple, because ax.plot() can plot multiple lines, if we pass multiple parameters to it. In this case, cause we are passing just 1 line, we just need the first element of the tuple.
```python
line1, = ax[0,1].plot([], [], color='steelblue', label='gamma=1.5', linewidth=1.5)
line2, = ax[0,1].plot([], [], color='red',       label='gamma=1.0', linewidth=1.5)
line3, = ax[0,1].plot([], [], color='green',     label='gamma=0.5', linewidth=1.5)
```



**Step 4:** the update function. 
The update function is responsible for updating the data in the plot for each frame. The function receives a frame as a parameter, and updates the data in the plot to show the data up to that point in time. The set_data() sets the x and y fata of the line, changing what is displayed in the plot. 

```python
def update(frame):
    line1.set_data(df1.iterations[:frame], df1.y1[:frame])
    line2.set_data(df2.iterations[:frame], df2.y1[:frame])
    line3.set_data(df3.iterations[:frame], df3.y1[:frame])
    return line1, line2, line3
```

**Step 5:**
Create the animation A frame: represents a single step in the animation, each frame  updates the plot to show the data up to that point in time.  the frame can be an iterable or an integer. Also with the  frame, the speed of the animation can be controlled.

```python
ani = FuncAnimation(
    fig,
    update,
    frames=len(df1),  # cuántos frames en total
    interval=20,      # ms entre frames (más bajo = más rápido)
    blit=True
)

plt.tight_layout()
plt.show()
```


# Mathematics


## Two dimensional discrete dynamical systems
In this kind of systems, there is a **function** that takes 2 numbers as input, and returns two numbers as outputs. Note that this is not the same as two separate functions. The process should be seen as one multi input and multi-output function. The output for y depends not just on the input of y but also on the input of x.

* If a one dimensional dynamical system gives us an scalar in R1, a two dimensional system gives us a point in R2 --> (x, y)

<img src="images\mathematics\two_dimensional_discrete_dynamical_systems\00_multi_variable_function.jpg" alt="correlation_vs_causation" width="250" height="90">


### The Hénon map
Functions are also commonly refered as **maps** by mathematicians, so map = function. 

<!-- This is latex syntax -->
$$
\begin{align*}
x_{n+1} &= y_n + 1 - a x_n^2 , \\
y_{n+1} &= b x_n ,
\end{align*}
$$

Where a and b are parameters. These parameters define the orbit's behaviour. 
* The Hénon map, from Michel Hénon, is constructed as an approximation to the Lorenz equations. 



### **References of this section:**
* [Feldman, D. P. (2012). Chaos and fractals: an elementary introduction. Oxford University Press.](https://dpfeldman.github.io/Chaos/index.html)

## Differential equations

### One dimensional differential equations
About Newtons law of cooling and how to solve a differential equation.
<img src="images\mathematics\one_dimensional_differential_equations\newtons_law_differential_equation.jpg" alt="newtons_law_of_cooling" width="" height="">

Another example on solving a differential equation, and which are the possible solutions for a differential equation of the form: 

<!-- This is latex syntax -->
$\frac{dx}{dt} = f(x)$

<img src="images\mathematics\one_dimensional_differential_equations\solution_dif_equation_phase_line.jpg" alt="solving_diff_eq" width="" height="">

### Two dimensional differential equations

The model we are going to study to exemplify the two dim. dif. eq. is the **Lotka-Volterra** model. 
<img src="images\mathematics\two_dimensional_differential_equations\01.jpg" alt="lotka_volterra_1" width="" height="">
<img src="images\mathematics\two_dimensional_differential_equations\02.jpg" alt="lotka_volterra_2" width="" height="">

### Computational solutions
Computational methods for solving differential equations, here we describe the **Euler's Method**
<img src="images\mathematics\computational_solutions\computational_solutions_differential_equations_eulers_method.jpg" alt="eulers_method" width="" height="">
<img src="images\mathematics\computational_solutions\eulers_method_two_equations.jpg" alt="eulers_method_2" width="" height="">


# Environmental modeling

## Plotting in three dimensions 3D




# dynamical-systems-modeling

## Important references and links:

* Web page of the professor David P. Feldman for comparing software and further readings: http://hornacek.coa.edu/dave/Chaos/programs.html

## Description
The purpose of this repo is to study dynamical systems theory, using python code. 


# 