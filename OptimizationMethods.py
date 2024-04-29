import random
import sympy as sp
import numpy as np

class OptimizationMethods:
    """
    This class contains all methods of optimization we needed for our project.
    """

    @staticmethod
    def newtons_method(f, x_k, precision=1e-6, max_iterations=100) -> tuple:
        """
        Newton's method for optimization.

        Args:
        - f: The function to optimize.
        - x_k: Initial guess for the optimal value.
        - precision: Tolerance for convergence.
        - max_iterations: Maximum number of iterations.

        Returns:
        - x_k: Optimal value.
        - iterations: Number of iterations.
        """
        x = sp.symbols('x')
        f_prime = sp.diff(f, x)
        f_double_prime = sp.diff(f_prime, x)
        iterations = 0

        for i in range(max_iterations):
            first_derivative_at_x = f_prime.subs(x, x_k).evalf()
            second_derivative_at_x = f_double_prime.subs(x, x_k).evalf()

            if second_derivative_at_x == 0:
                print("Division by zero. Stopping the iteration.")
                break

            x_k1 = x_k - first_derivative_at_x / second_derivative_at_x
            if abs(x_k1 - x_k) < precision:
                break
            x_k = x_k1
            iterations += 1

        return float(x_k), iterations

    @staticmethod
    def gradient_method(fun, uk, max_iterations=1000, tolerance=1e-6, alpha=0.01, beta=0.5):
        """
        Gradient descent method for optimization.

        Args:
        - fun: The function to optimize.
        - uk: Initial guess for the optimal value.
        - max_iterations: Maximum number of iterations.
        - tolerance: Tolerance for convergence.
        - alpha: Coefficient for line search.
        - beta: Reduction factor for step size.

        Returns:
        - uk: Optimal value.
        - i: Number of iterations.
        """
        x = sp.symbols('x')
        f = fun(x)
        gradient = sp.diff(f, x)
        gradient_fun = sp.lambdify(x, gradient, 'numpy')
        fun = sp.lambdify(x, f, 'numpy')
        i = 0

        for k in range(max_iterations):
            grad_val = gradient_fun(uk)
            step_size = 1.0

            while fun(uk - step_size * grad_val) > fun(uk) - alpha * step_size * np.square(np.linalg.norm(grad_val)):
                step_size *= beta

            uk = uk - step_size * grad_val
            if np.linalg.norm(grad_val) < tolerance:
                break
            i += 1

        return uk, i

    @staticmethod
    def random_search(fun, bounds, max_iterations=1000):
        """
        Random search method for function optimization.

        Args:
        - fun: The function to optimize.
        - bounds: A tuple of (min, max) defining the range of x values to search.
        - max_iterations: Maximum number of iterations to perform.

        Returns:
        - best_x: The x value that resulted in the lowest function value.
        - best_fun_val: The lowest function value found.
        - iterations: The number of iterations performed.
        """
        x = sp.symbols('x')
        fun_lambdified = sp.lambdify(x, fun(x), 'numpy')  # Convert symbolic expression to a numerical function

        best_x = None
        best_fun_val = float('inf')  # Initialize to the largest possible value
        iterations = 0  # Initialize iteration counter

        for i in range(max_iterations):
            x_k = random.uniform(bounds[0], bounds[1])  # Generate a random candidate within the bounds
            fun_val = fun_lambdified(x_k)  # Evaluate the function at the candidate point

            if fun_val < best_fun_val:  # If the current value is the best so far, update the best records
                best_fun_val = fun_val
                best_x = x_k

            iterations += 1  # Update the iteration count

        return best_x, iterations


