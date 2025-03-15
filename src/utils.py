
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


def newtons_law_of_cooling(k:float, Tr:float, variable_magnitude:float):
    """
    This is a differential equation of the form: dT(t)/dt = k(Tr - T(t)); 
    where T(t) is the temperature at time t (this is the parameter 
    that controls the initial conditions of the system). 

    Args:
    -------
        variable_magnitude: float
            The variable magnitude of the differential equation.
            This can also be interpreted as the initial condition.
        k: float
            Constant that models how the object exchange heat with 
            the environment
        Tr: float
            Temperature of the environment.

    """
    T = variable_magnitude
    return k*(Tr - T)


# Function for applying the Euler's method to solve the differential equation
def euler_method(differential_eq: Callable, delta, iterations, *args, **kwargs):
    """
    This is the Euler's method for solving differential equations.
    Args:
    -------
        differential_eq: Callable (function, method, class)
            The differential equation to solve
        delta: float
            This is the step size for the Euler's method. this
            is the size of the interval we assume the differential
            equation is constant.
        *args: Tuple
            The arguments needed for the differential equation.
        **kwargs: Dict
            The positional arguments needed for the differential equation.

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

    
    # Accessing to the Kwargs dictionary to extract the 
    # variable magnitude, so we can apply the Euler's method.
    # The first time we call this variable magnitude is the initial
    # condition of the system.
    # The **Kwargs is a dictionary that contains all the
    # positional arguments and can be accessed by the key.
    variable_magnitude = kwargs['variable_magnitude']

    results = []

    for i in range(iterations):
        results.append(variable_magnitude)

        rate_of_change = differential_eq(*args, variable_magnitude)

        # Calculating new variable magnitude
        variable_magnitude = round((rate_of_change * delta) + variable_magnitude, 5)

    df_result = pd.DataFrame(data={
        "iteration": np.arange(0, iterations, 1),
        "variable_magnitude": results
    })


    return df_result