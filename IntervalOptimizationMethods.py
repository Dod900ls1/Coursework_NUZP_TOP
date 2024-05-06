import numpy as np
from typing import Callable, Tuple, Union, Any
import sympy as sp


class IntervalOptimizationMethods:
    """
    A class that provides various methods for optimizing a function over a specified interval. These methods are designed
    to find the local minimum of a function within given bounds. The class implements three different interval optimization
    techniques: Golden Ratio Optimization, Fibonacci Search, and Bisection Method.
    """

    @staticmethod
    def golden_ratio_optimization(func: Callable, lower_bound: float, upper_bound: float, tolerance: float = 1e-6) -> \
    Tuple[
        float, float, int, str]:
        """
        Implements the Golden Ratio Optimization method to find the minimum of a unimodal function within a specified interval.

        Parameters:
        - func (Callable): The function to minimize.
        - a (float): The lower boundary of the search interval.
        - b (float): The upper boundary of the search interval.
        - tolerance (float): The precision tolerance of the search (default is 1e-6).

        Returns:
        Tuple[float, float, int, str]: A tuple containing the estimated x-value at the minimum (float), the minimum value of the function
                                       at that x-value (float), the number of iterations performed (int), and the result status ("Success" or "Failure").
        """
        x = sp.symbols("x")
        # Golden ratio constant
        golden_ratio = (np.sqrt(5) - 1) / 2

        f = sp.lambdify(x, func, 'numpy')
        a_init = lower_bound
        b_init = upper_bound
        # Initial points
        x1 = lower_bound + (1 - golden_ratio) * (upper_bound - lower_bound)
        x2 = lower_bound + golden_ratio * (upper_bound - lower_bound)

        iterations = 0
        while abs(upper_bound - lower_bound) > tolerance:
            iterations += 1
            # Calculate function values at x1 and x2
            f_x1 = f(x1)
            f_x2 = f(x2)

            # Choose the new interval
            if f_x1 < f_x2:
                upper_bound = x2
                x2 = x1
                x1 = lower_bound + (1 - golden_ratio) * (upper_bound - lower_bound)
            else:
                lower_bound = x1
                x1 = x2
                x2 = lower_bound + golden_ratio * (upper_bound - lower_bound)

        # Return the midpoint of the final interval
        x_min = (lower_bound + upper_bound) / 2
        best_function_value = f(x_min)

        # Check if optimization is at a boundary
        if np.isclose(x_min, a_init, atol=tolerance) or np.isclose(x_min, b_init, atol=tolerance):
            result_status = "Failure"
        else:
            result_status = "Success"

        return x_min, best_function_value, iterations, result_status

    @staticmethod
    def fibonacci_optimization(func: Callable, lower_bound: float, upper_bound: float, tolerance: float = 1e-6,
                               n: int = 100) -> tuple[Union[float, Any], Any, int, str]:
        """tolerance
        Utilizes Fibonacci numbers to determine the minimum of a function within an interval by progressively narrowing the range of search.

        Parameters:
        - func (Callable): The function to minimize.
        - lower_bound (float): The start of the interval.
        - upper_bound (float): The end of the interval.
        - tolerance (float): The convergence tolerance.
        - n (int): The number of Fibonacci iterations to perform (default is 100).

        Returns:
        Tuple[float, float, int, str]: A tuple containing the estimated x-value at the minimum (float), the minimum value of the function
                                       at that x-value (float), the number of iterations performed (int), and the result status ("Success" or "Failure").
        """
        lower_bound_init = lower_bound
        upper_bound_init = upper_bound

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
        while abs(upper_bound - lower_bound) > tolerance and iterations < n - 2:
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

        # Check if optimization is at a boundary
        if np.isclose(x_min, lower_bound_init, atol=tolerance) or np.isclose(x_min, upper_bound_init, atol=tolerance):
            result_status = "Failure"
        else:
            result_status = "Success"

        return x_min, minimum, iterations, result_status

    @staticmethod
    def bisection_optimization(func: Callable, lower_bound: float, upper_bound: float, delta: float = 0.1,
                               tolerance: float = 1e-6) -> \
            tuple[Union[float, Any], Any, int, str]:
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
        lower_bound_init = lower_bound
        upper_bound_init = upper_bound
        x = sp.symbols('x')
        f = sp.lambdify(x, func, modules='numpy')
        iterations = 0
        while abs(lower_bound - upper_bound) > tolerance:
            mid = (lower_bound + upper_bound) / 2
            left = mid - delta
            right = mid + delta
            if f(left) < f(right):
                upper_bound = mid
            else:
                lower_bound = mid
            iterations += 1

        x_min = (lower_bound + upper_bound) / 2
        minimum = f(x_min)
        if np.isclose(x_min, lower_bound_init, atol=tolerance) or np.isclose(x_min, upper_bound_init, atol=tolerance):
            result_status = "Failure"
        else:
            result_status = "Success"

        return  x_min, minimum, iterations, result_status
