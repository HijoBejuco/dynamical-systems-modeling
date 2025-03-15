import sys
import os
import json
import time
import pytest
import pandas as pd

# Add the root path to the sys.path
# This will allow us to import the modules in the src folder
root_path = os.path.dirname(os.path.dirname(__file__))
print(root_path)
sys.path.append(root_path)
from src.utils import (
    logistic_eq_iterator,
    euler_method,
    newtons_law_of_cooling
    )


def test_logistic_eq_iterator():
    """
        Compares a predefined output for iterating the
        logistic equation
    """
    result_list = [0.8, 0.432, 0.6625152, 0.6036897864, 0.6459707561]
    assert logistic_eq_iterator(2.7, 0.8, 5) == result_list

def test_euler_method():
    """
        Compares a predefined output for solving a
        differential equation using the Euler method
    """
    # List for comparing the result of euler method
    result_list = [80.00000, 68.00000, 58.40000, 50.72000, 44.57600, 
                   39.66080, 35.72864, 32.58291, 30.06633, 28.05306]
    
    # The euler_method function returns a dataframe, so here, we
    # extract the variable_magnitude column.
    equation_solution = euler_method(newtons_law_of_cooling, 1, 10, 0.2, 20, variable_magnitude=80).variable_magnitude

    # Convert into a list for comparison.
    assert equation_solution.tolist() == result_list









