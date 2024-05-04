import numpy as np
from typing import Callable, Tuple
import sympy as sp


class IntervalOptimizationMethods:
    """
    A class that provides various methods for optimizing a function over a specified interval. These methods are designed
    to find the local minimum of a function within given bounds. The class implements three different interval optimization
    techniques: Golden Ratio Optimization, Fibonacci Search, and Bisection Method.
    """

    @staticmethod
    def golden_ratio_optimization(func: Callable, a: float, b: float, tolerance: float = 1e-6) -> Tuple[
        float, float, int]:
        """
        Implements the Golden Ratio Optimization method to find the minimum of a unimodal function within a specified interval.

        Parameters:
        - func (Callable): The function to minimize.
        - a (float): The lower boundary of the search interval.
        - b (float): The upper boundary of the search interval.
        - tolerance (float): The precision tolerance of the search (default is 1e-6).

        Returns:
        Tuple[float, float, int]: A tuple containing the estimated x-value at the minimum (float), the minimum value of the function
                                  at that x-value (float), and the number of iterations performed (int).
        """
        x = sp.symbols("x")
        # Golden ratio constant
        golden_ratio = (np.sqrt(5) - 1) / 2

        f = sp.lambdify(x, func, 'numpy')

        # Initial points
        x1 = a + (1 - golden_ratio) * (b - a)
        x2 = a + golden_ratio * (b - a)

        iterations = 0
        while abs(b - a) > tolerance:
            iterations += 1
            # Calculate function values at x1 and x2
            f_x1 = f(x1)
            f_x2 = f(x2)

            # Choose the new interval
            if f_x1 < f_x2:
                b = x2
                x2 = x1
                x1 = a + (1 - golden_ratio) * (b - a)
            else:
                a = x1
                x1 = x2
                x2 = a + golden_ratio * (b - a)

        # Return the midpoint of the final interval
        x_optimal = (a + b) / 2
        best_function_value = f(x_optimal)
        return x_optimal, best_function_value, iterations

    @staticmethod
    def fibonacci_optimization(func: Callable, lower_bound: float, upper_bound: float, tolerance: float = 1e-6,
                               n: int = 100) -> Tuple[float, float, int]:
        """
        Utilizes Fibonacci numbers to determine the minimum of a function within an interval by progressively narrowing the range of search.

        Parameters:
        - func (Callable): The function to minimize.
        - lower_bound (float): The start of the interval.
        - upper_bound (float): The end of the interval.
        - tolerance (float): The convergence tolerance.
        - n (int): The number of Fibonacci iterations to perform (default is 100).

        Returns:
        Tuple[float, float, int]: A tuple containing the x-value where the function is minimized (float), the function's minimum value
                                  at that x-value (float), and the number of iterations (int).
        """
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])

        x1 = lower_bound + (fib[n - 2] / fib[n]) * (upper_bound - lower_bound)
        x2 = lower_bound + (fib[n - 1] / fib[n]) * (upper_bound - lower_bound)
        x = sp.symbols("x")
        f = sp.lambdify(x, func, modules='numpy')
        f1 = f(x1)
        f2 = f(x2)

        iterations = 0
        while (upper_bound - lower_bound) > tolerance and iterations < n - 2:
            iterations += 1
            if f1 < f2:
                upper_bound = x2
                x2 = x1
                f2 = f1
                x1 = lower_bound + (fib[n - iterations - 2] / fib[n - iterations]) * (upper_bound - lower_bound)
                f1 = f(x1)
            else:
                lower_bound = x1
                x1 = x2
                f1 = f2
                x2 = lower_bound + (fib[n - iterations - 1] / fib[n - iterations]) * (upper_bound - lower_bound)
                f2 = f(x2)

        x_min = (x1 + x2) / 2
        minimum = f(x_min)
        return x_min, minimum, iterations

    @staticmethod
    def bisection_optimization(func: Callable, a: float, b: float, delta: float, epsilon: float) -> Tuple[
        float, float, int]:
        """
        The Bisection method is used to find the minimum of a function by evaluating the function at the midpoint and points slightly
        left and right of the midpoint, then narrowing the search interval based on these evaluations.

        Parameters:
        - func (Callable): The function to minimize.
        - a (float): The left endpoint of the interval.
        - b (float): The right endpoint of the interval.
        - delta (float): The distance from the midpoint where the function is evaluated.
        - epsilon (float): The precision tolerance of the convergence.

        Returns:
        Tuple[float, float, int]: A tuple containing the x-value of the minimum (float), the minimum value of the function (float),
                                  and the number of iterations (int) it took to converge.
        """
        x = sp.symbols('x')
        f = sp.lambdify(x, func, modules='numpy')
        iterations = 0
        while abs(a - b) > epsilon:
            mid = (a + b) / 2
            left = mid - delta
            right = mid + delta
            if f(left) < f(right):
                b = mid
            else:
                a = mid
            iterations += 1

        x_min = (a + b) / 2
        minimum = f(x_min)
        return x_min, minimum, iterations
