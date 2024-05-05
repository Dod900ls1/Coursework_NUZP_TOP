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
        Newton's method for finding a local minimum of a function.

        Args:
        - f (sp.Expr): The Sympy expression of the function to be minimized.
        - x_k (float): Initial guess for the minimum point.
        - precision (float): Precision for convergence.
        - max_iterations (int): Maximum number of iterations to perform.

        Returns:
        - tuple: (x_k, f(x_k), iterations) where x_k is the approximate minimum,
                 f(x_k) is the function value at x_k, and iterations is the number of iterations performed.
        """
        x = sp.symbols('x')
        f_prime = sp.diff(f, x)
        f_double_prime = sp.diff(f_prime, x)
        f_prime_lambdified = sp.lambdify(x, f_prime, "numpy")
        f_double_prime_lambdified = sp.lambdify(x, f_double_prime, "numpy")
        iterations = 0
        result_status = "Success"

        while iterations < max_iterations:
            try:
                first_derivative_at_x = f_prime_lambdified(x_k)
                second_derivative_at_x = f_double_prime_lambdified(x_k)

                # Check if the second derivative is inf or nan, or too close to zero
                if np.isinf(second_derivative_at_x) or np.isnan(second_derivative_at_x) or abs(
                        second_derivative_at_x) < 1e-8:
                    print("Invalid second derivative encountered.")
                    result_status = "Failure"
                    break

                x_k1 = x_k - first_derivative_at_x / second_derivative_at_x

                if np.isnan(x_k1):
                    result_status = "Failure"
                    break

                if abs(x_k1 - x_k) < precision:
                    x_k = x_k1
                    break

                x_k = x_k1
                iterations += 1
            except Exception as e:
                print(f"Numerical error encountered: {e}")
                return None, None, None, "Failure"

        f_lambdified = sp.lambdify(x, f, "numpy")
        return x_k, f_lambdified(x_k), iterations, result_status


    @staticmethod
    def gradient_method(fun: sp.Expr, uk: float, max_iterations: int = 1000, tolerance: float = 1e-6,
                        alpha: float = 0.01, beta: float = 0.5, max_value: float = 1e20) -> tuple:
        """
        Gradient descent method for optimizing a function.

        Args:
        - fun (sp.Expr): The function to optimize, represented as a Sympy expression.
        - uk (float): Initial guess for the minimum value.
        - max_iterations (int): Maximum allowed iterations.
        - tolerance (float): Convergence tolerance.
        - alpha (float): Coefficient for the line search.
        - beta (float): Reduction factor for step size during line search.
        - max_value (float): Maximum allowed value for uk to prevent overflow.

        Returns:
        - tuple: (uk, best_function_value, iterations) where uk is the optimized variable,
                 best_function_value is the function value at uk, and iterations is the number of iterations used.
        """
        x = sp.symbols('x')
        f = fun
        gradient = sp.diff(f, x)
        gradient_fun = sp.lambdify(x, gradient, 'numpy')
        fun = sp.lambdify(x, f, 'numpy')
        i = 0
        result_status = "Success"

        for k in range(max_iterations):
            try:
                grad_val = gradient_fun(uk)
            except ZeroDivisionError:
                print("Division by zero. Stop iteration")
                result_status = "Failure"
                return None, None, None, result_status
            step_size = 1.0

            while fun(uk - step_size * grad_val) > fun(uk) - alpha * step_size * np.square(np.linalg.norm(grad_val)):
                step_size *= beta

            uk = uk - step_size * grad_val
            if np.linalg.norm(grad_val) < tolerance:
                break
            i += 1

            if abs(uk) > max_value:
                result_status = "Failure"
                return None, None, None, result_status

        return uk, fun(uk), i, result_status

    @staticmethod
    def random_search(fun_expr: sp.Expr, x_k: float, tolerance: float = 1e-6, step_size: float = 1,
                      max_iterations: int = 1000,
                      shrink_step: bool = False) -> tuple:
        """
        Random search method for optimizing a function starting from an initial guess.

        Args:
        - fun_expr (sp.Expr): Sympy expression of the function to optimize.
        - x_k (float): Initial guess for the optimal value.
        - tolerance (float): Tolerance for convergence.
        - step_size (float): Magnitude of the initial random steps.
        - max_iterations (int): Maximum number of iterations.
        - shrink_step (bool): Whether to decrease step size over iterations.

        Returns:
        - tuple: (x_k, best_fun_val, iterations) where x_k is the optimized variable,
                 best_fun_val is the function value at x_k, and iterations is the number of iterations performed.
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
