# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html

def f1(x: np.ndarray) -> np.ndarray: 
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
        return np.multiply(np.add(np.multiply(np.add(x[0], np.add(x[1], x[1])), np.cos(np.sqrt(np.abs(np.add(x[0], x[2]))))), np.add(np.multiply(np.add(x[2], x[1]), np.divide(np.sin(x[0]), x[0])), np.multiply(np.add(np.sin(x[0]), x[0]), 2))), 700000)

def f3(x: np.ndarray) -> np.ndarray: 
    return np.add(np.add(np.subtract(4, np.multiply(x[2], np.divide(7, 2))), np.multiply(x[0], np.add(x[0], x[0]))), np.multiply(np.multiply(x[1], x[1]), np.subtract(0, x[1])))

def f4(x: np.ndarray) -> np.ndarray:
    return np.add(np.add(np.multiply(7, np.cos(x[1])), np.log(27)), np.divide(np.multiply(7, x[0]), -75))

def f5(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.subtract(np.sin(np.multiply(np.divide(x[1], 100), np.divide(x[0], 50))), np.multiply(np.divide(x[1], 100), np.divide(x[0], 50))), np.multiply(np.cos(np.cos(x[1])), np.cos(np.cos(x[1]))))

def f6(x: np.ndarray) -> np.ndarray: 
    return np.add(np.multiply(np.divide(7, 10), np.subtract(x[1], x[0])), x[1])

def f7(x: np.ndarray) -> np.ndarray: 
    return np.abs(np.divide(np.multiply(np.multiply(-71, x[0]), np.multiply(np.divide(x[0], 24), x[1])), np.add(np.abs(np.subtract(x[0], x[1])), np.sin(-66))))

def f8(x: np.ndarray) -> np.ndarray:
     return np.add(np.add(np.multiply(np.multiply(np.multiply(x[5], x[5]), x[5]), np.abs(np.multiply(np.multiply(x[5], x[5]), x[5]))), np.multiply(np.multiply(x[5], np.sqrt(np.abs(x[5]))), 90)), np.multiply(x[4], np.multiply(x[4], -75)))

