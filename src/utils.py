
# Importing typing for dealing with Type Hinting. Union is used to specify 
# that such parameter can recieve more than one data types
from typing import List, Tuple, Dict, Union, Callable
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class dummy:
    pass

def logistic_eq_iterator(r_value:float, seed: Union[float, int], iterations = int) -> List[float]:
    """
    Method for iterating the logistic equation and recieving it's orbit

    Args:
        r_value(int): this is the r parameter of the logistic equation
        seed(float | int): starting point of the orbit
        iterations(int): how many iterations
    """

    # This is the list which will store the orbit of the iterated function
    orbit = [seed]

    for i in range(1,iterations,1):
        # Calculating the x value, which is just the previous value 
        # in the orbit list
        x = orbit[i-1]

        # Iterating the function 
        iterate = r_value*x*(1-x)

        # Adding the iterate to the orbit list, be careful with this
        # rounding. make sure leave enough decimals to avoid induce
        # misscalculations or imprecisions. 
        orbit.append(round(iterate, 10))

    return orbit

# Create the differential equation we are about to solve.



def newtons_law_of_cooling(t: float, y0: np.ndarray, k: float, Tr: float) -> float:
    """
    This is a differential equation of the form: dT(t)/dt = k(Tr - T(t)); 
    where T(t) is the temperature at time t (this is the parameter 
    that controls the initial conditions of the system). 

    Args:
    -------
        t: float
            current time (not used explicitly, but required by the solver interface)
        y: np.ndarray of shape (n,) in this case, (1,)
            The variable magnitude of the differential equation.
            This can also be interpreted as the initial condition.
        k: float
            Constant that models how the object exchange heat with 
            the environment
        Tr: float
            Temperature of the environment.

    """
    y = y0[0]
    return np.array([k*(Tr - y)])


def euler_method(differential_eq: Callable, y0: np.ndarray, t0: float, delta: float, iterations: int, *args) -> pd.DataFrame:
    """
    This solves a dy/dt = f(t, y, *args) for a system of n ecuations, such as the
    Lotka-Volterra model or Lorenz equations system. 

        This is the Euler's method for solving differential equations.
    Args:
    -------
        differential_eq: Callable (function, method, class)
            The differential equation to solve. This differential equation MUST have
            a predefined structure like this: 
                def diff_eq_system_name(t: float, y: float, *args) -> np.ndarray of shape (n,)
                    This function returns a np array, bacause it can also be a system of n equations,
                        such as Lorenz eq (3 eqs) and Lotka-Volterra model (2 eqs)
                    t: current time (not used explicitly, but required by the solver interface)
                    y: The variable magnitude of the differential equation.
                        This can also be interpreted as the initial condition.
                    *args: are all the parameters needed for the diffetential_eq()
        y0: np.ndarray of shape (n,)
            Initial conditions of the system, every member of the array is a specific initial
            condition of the equation to solve. If is a system of n equations, it goes in order
            depending on the differential_eq function. 
        t0: float
            initial time
        delta: float
            This is the step size for the Euler's method. this
            is the size of the interval we assume the differential
            equation is constant.
        iterations: int
            quantity of steps/ iterations well run.
        *args: Tuple
            The arguments needed for the differential equation. These
            are the parameters required for the diff eq. 

    Returns: DataFrame
    -------
        A pandas DataFrame with the results of the Euler's method.
        The DataFrame contains the iteration number and the variable magnitude
        of the differential equation.

    Euler's Method Algorithm:
        Steps of the Eulers method:

        1. Calculate the rate of change of the process. 
        Here we need to replace into the differential equation 
        the variable magnitude, so we know the rate of change. 

        2. Then, we need to sum/substract the rate of change to the 
        variable value, but before that, we need to multiply the 
        rate of change by the delta. 
            e.j. Suppose our rate of change is 2°c/min, and our delta 
            is 2min, so, to know the temperature change after 2 minutes, we 
            need to multiply the 2°c/min rate of change, by the delta 2min.
                temp_after_2min = variable_magnitude + (2°c/min * 2min)

        3. The step 2 gives us the new magnitude after our delta. 
            e.j. In our case, we know the temperature after 2 minutes.

        4. After we have the new magnitude, just repeat te process
        from the first step of this algorithm.
    """

    t = t0
    y = y0.copy() #Here we avoid losing initial conditions
    n = len(y0)
    results = []
    for i in range(iterations):
        results.append({"iterations": i, "t": t, **{f"y{j}": y[j] for j in range(n)}})
        
        dydt = differential_eq(t, y, *args) # vector (n,)
        # Vectorial simultaneous update, here we update all the
        # values of the eqs we are solving.
        y = y + dydt * delta
        t = t + delta
    
    return pd.DataFrame(results)



def lotka_volterra(t, y, alpha, beta, delta, gamma):
    """
    
    """
    # unpack state vector
    x_prey, y_pred = y

    # Equation for preys
    dxdt = alpha * x_prey - beta * x_prey * y_pred
    
    # Equation for predators
    dydt = delta * x_prey * y_pred - gamma * y_pred
    
    # Return detivates vector
    return np.array([dxdt, dydt])
 






