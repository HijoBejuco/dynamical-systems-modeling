
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

### Computational solutions
Computational methods for solving differential equations, here we describe the **Euler's Method**
<img src="images\mathematics\computational_solutions\computational_solutions_differential_equations_eulers_method.jpg" alt="eulers_method" width="" height="">


# Environmental modeling

## Plotting in three dimensions 3D




# dynamical-systems-modeling

## Important references and links:

* Web page of the professor David P. Feldman for comparing software and further readings: http://hornacek.coa.edu/dave/Chaos/programs.html

## Description
The purpose of this repo is to study dynamical systems theory, using python code. 


# 