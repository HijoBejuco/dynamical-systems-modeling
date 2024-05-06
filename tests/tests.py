import sys
import os
import json
import time
import pytest
import pandas as pd
sys.path.append("./src")
from src.utils import(
    logistic_eq_iterator
)

def test_logistic_eq_iterator():
    """
        Compares a predefined output for iterating the
        logistic equation
    """
    result_list = [0.8, 0.432, 0.663, 0.603, 0.646]
    assert logistic_eq_iterator(2.7, 0.8, 5) == result_list

print(sys.path)