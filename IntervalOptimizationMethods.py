import numpy as np


class GoldenRatioOptimization:
    @staticmethod
    def golden_ratio_optimization(func: callable, a: float, b: float, tol: float = 1e-6,
                                  max_iterations: int = 100) -> tuple:
        """
        Golden Section Search for function optimization within an interval.

        Args:
        - func: The function to optimize.
        - a: Lower bound of the interval.
        - b: Upper bound of the interval.
        - tol: Tolerance for convergence.
        - max_iterations: Maximum number of iterations.

        Returns:
        - x_opt: Optimal value within the interval.
        - f(x_opt): Value of the function at the optimal value.
        - iterations: Number of iterations performed.
        """

        # Golden ratio constant
        golden_ratio = (np.sqrt(5) + 1) / 2

        # Initial points
        x1 = a + (golden_ratio - 1) * (b - a)
        x2 = b - (golden_ratio - 1) * (b - a)

        iterations = 0
        for i in range(max_iterations):
            if np.abs(b - a) < tol:
                break

            f_x1 = func(x1)
            f_x2 = func(x2)

            if f_x1 < f_x2:
                b = x2
                x2 = x1
                x1 = a + (golden_ratio - 1) * (b - a)
            else:
                a = x1
                x1 = x2
                x2 = b - (golden_ratio - 1) * (b - a)
            iterations += 1

        x_opt = (a + b) / 2
        return x_opt, iterations
