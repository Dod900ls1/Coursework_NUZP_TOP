import random
import sympy as sp
import numpy as np


class PointOptimizationMethods:
    """
    This class contains all methods of optimization we needed for our project.
    """

    @staticmethod
    def newtons_method(f: sp.Expr, x_k: float, precision: float = 1e-6, max_iterations: int = 100) -> tuple:
        """
        Newton's method for optimization.

        Args:
        - f: The function to optimize.
        - x_k: Initial guess for the optimal value.
        - precision: Tolerance for convergence.
        - max_iterations: Maximum number of iterations.

        Returns:
        - x_k: Optimal value.
        - best_function_value: Best function value
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

        return float(x_k), f.subs(x, x_k), iterations

    @staticmethod
    def gradient_method(fun: sp.Expr, uk: float, max_iterations: int = 1000, tolerance: float = 1e-6,
                        alpha: float = 0.01, beta: float = 0.5) -> tuple:
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
        - best_function_value: Best function value
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

        return uk, fun(uk), i

    @staticmethod
    def random_search(fun_expr: sp.Expr, x_k: float, tolerance: float = 1e-6, step_size: float = 1,
                      max_iterations: int = 1000,
                      shrink_step: bool = False) -> tuple:
        """
        Random search method for function optimization starting from an initial point.

        Args:
        - fun_expr: The Sympy expression of the function to optimize.
        - x_k: Initial guess for the optimal value.
        - tolerance: Tolerance for convergence.
        - step_size: Initial magnitude of the random steps.
        - max_iterations: Maximum number of iterations.
        - shrink_step: Boolean to decide if the step size should decrease over iterations.

        Returns:
        - x_k: The x value that resulted in the lowest function value.
        - best_fun_val: The lowest function value found.
        - iterations: The number of iterations performed.
        """
        x = sp.symbols('x')
        fun_lambdified = sp.lambdify(x, fun_expr, 'numpy')

        best_x = x_k
        best_fun_val = fun_lambdified(x_k)
        iterations = 0
        previous_fun_val = best_fun_val

        for i in range(max_iterations):
            step_direction = random.choice([-1, 1])
            x_k_new = x_k + step_direction * step_size * random.random()

            fun_val = fun_lambdified(x_k_new)

            if fun_val < best_fun_val:
                best_fun_val = fun_val
                best_x = x_k_new
                x_k = x_k_new

            if shrink_step and (step_size > tolerance):
                step_size = 0.95 * step_size

            iterations += 1
            # Terminate if improvement is less than tolerance
            if abs(fun_val - previous_fun_val) < tolerance:
                break

            previous_fun_val = fun_val

        return best_x, best_fun_val, iterations
