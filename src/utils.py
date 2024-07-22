
# Importing typing for dealing with Type Hinting. Union is used to specify 
# that such parameter can recieve more than one data types
from typing import List, Tuple, Dict, Union


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