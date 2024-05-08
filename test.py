import sympy as sp
import numpy as np
from PointOptimizationMethods import PointOptimizationMethods
from IntervalOptimizationMethods import IntervalOptimizationMethods

x = sp.symbols("x")

test_functions = {
    'Exponential 1': sp.exp(x**2),
    'Exponential 2': 2 ** x - x ** 2,
    'Exponential 3': 2 ** x * 9*x**2,
    'Logarithmic 1': sp.log(sp.exp(x**2) + x + 1),
    'Logarithmic 2': x * sp.log(x) - x ** 0.5,
    'Logarithmic 3': x*sp.log(x) + x ** 2
}

function_types = {
    'Quadratic': ['Quadratic 1', 'Quadratic 2', 'Quadratic 3', 'Quadratic 4', 'Quadratic 5'],
    'Cubic': ['Cubic 1', 'Cubic 2', 'Cubic 3', 'Cubic 4', 'Cubic 5'],
    'Quartic': ['Quartic 1', 'Quartic 2', 'Quartic 3', 'Quartic 4', 'Quartic 5'],
    'Exponential': ['Exponential 1', 'Exponential 2', 'Exponential 3'],
    'Logarithmic': ['Logarithmic 1', 'Logarithmic 2', 'Logarithmic 3']
}

for i in test_functions.values():
    print(PointOptimizationMethods.newtons_method(i, 1))

f = x ** 3 - 3 * x - 1
# print(IntervalOptimizationMethods.bisection_optimization(f, lower_bound=4, upper_bound=-4, delta=0.1))