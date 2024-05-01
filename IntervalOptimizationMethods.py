import numpy as np
from typing import Callable, Tuple



class IntervalOptimizationMethods:
    @staticmethod
    def golden_ratio_optimization(func: Callable, a: float, b: float, tolerance: float = 1e-6) -> Tuple[
        float, float, int]:
        """
        Golden Ratio Optimization method for finding the minimum of a unimodal function.

        Parameters:
        - func: The objective function to minimize.
        - a: The left endpoint of the initial interval.
        - b: The right endpoint of the initial interval.
        - tolerance: The tolerance for the minimum value.

        Returns:
        - x_optimal: The x-value corresponding to the minimum of the function.
        - best_function_value: The minimum value of the function.
        - iterations: Number of iterations performed.
        """
        # Golden ratio constant
        golden_ratio = (np.sqrt(5) - 1) / 2

        # Initial points
        x1 = a + (1 - golden_ratio) * (b - a)
        x2 = a + golden_ratio * (b - a)

        iterations = 0
        while abs(b - a) > tolerance:
            iterations += 1
            # Calculate function values at x1 and x2
            f_x1 = func(x1)
            f_x2 = func(x2)

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
        best_function_value = func(x_optimal)
        return x_optimal, best_function_value, iterations

    @staticmethod
    def fibonacci_optimization(func: Callable, lower_bound: float, upper_bound: float, tolerance: float = 1e-6, n: int = 100) -> Tuple[float, float, int]:
        """
        Fibonacci Search method for finding the minimum of a function. This method uses Fibonacci
        numbers to progressively narrow the search interval.

        Parameters:
        - func (Callable): The objective function to minimize.
        - lower_bound (float): The lower boundary of the initial interval.
        - upper_bound (float): The upper boundary of the initial interval.
        - tolerance (float): The tolerance for the minimum value.
        - n (int): The number of Fibonacci numbers to generate.

        Returns:
        Tuple[float, float, int]: Optimal x-value, minimum function value, and number of iterations.
        """
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])

        x1 = lower_bound + (fib[n - 2] / fib[n]) * (upper_bound - lower_bound)
        x2 = lower_bound + (fib[n - 1] / fib[n]) * (upper_bound - lower_bound)
        f1 = func(x1)
        f2 = func(x2)

        iterations = 0
        while (upper_bound - lower_bound) > tolerance and iterations < n-2:
            iterations += 1
            if f1 < f2:
                upper_bound = x2
                x2 = x1
                f2 = f1
                x1 = lower_bound + (fib[n - iterations - 2] / fib[n - iterations]) * (upper_bound - lower_bound)
                f1 = func(x1)
            else:
                lower_bound = x1
                x1 = x2
                f1 = f2
                x2 = lower_bound + (fib[n - iterations - 1] / fib[n - iterations]) * (upper_bound - lower_bound)
                f2 = func(x2)

        x_min = (x1 + x2) / 2
        minimum = func(x_min)
        return x_min, minimum, iterations

    @staticmethod
    def bisection_optimization(func: Callable, a: float, b: float, delta: float, epsilon: float) -> Tuple[float, float, int]:
        """
        Bisection method for finding the minimum of a function. This method evaluates
        the function at points around the midpoint of the interval, adjusting the interval
        based on which side yields a smaller function value.

        Parameters:
        - func (Callable): The objective function to minimize.
        - a (float): The left endpoint of the interval.
        - b (float): The right endpoint of the interval.
        - delta (float): The distance to shift from the midpoint for function evaluation.
        - epsilon (float): The tolerance for convergence.

        Returns:
        Tuple[float, float, int]: Minimum x-value, minimum function value, and number of iterations.
        """
        iterations = 0
        while abs(a - b) > epsilon:
            mid = (a + b) / 2
            left = mid - delta
            right = mid + delta
            if func(left) < func(right):
                b = mid
            else:
                a = mid
            iterations += 1

        x_min = (a + b) / 2
        minimum = func(x_min)
        return x_min, minimum, iterations

