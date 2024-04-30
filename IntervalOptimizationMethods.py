import numpy as np


class IntervalOptimizationMethods:
    @staticmethod
    def golden_ratio_optimization(func, a, b, tolerance=1e-6):
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
