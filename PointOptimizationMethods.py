import random
import sympy as sp
import numpy as np
from typing import Tuple, Optional


class PointOptimizationMethods:
    """
    This class contains all methods of optimization we needed for our project.
    """

    @staticmethod
    def newtons_method(f: sp.Expr, x_k: float, tolerance: float = 1e-6, max_iterations: int = 100) -> Tuple[
        Optional[float], Optional[float], Optional[int], str]:
        """
        Newton's method for finding a local minimum of a function using its derivatives.

        Parameters:
        - f (sp.Expr): The function to be minimized, expressed as a SymPy expression.
        - x_k (float): Initial guess for the location of the minimum.
        - tolerance (float): The convergence criterion; the algorithm stops when the difference between successive
        iterates is below this value.
        - max_iterations (int): The maximum number of iterations to execute before stopping.

        Returns:
        Tuple[Optional[float], Optional[float], Optional[int], str]: Returns a tuple containing the approximate minimum
        location, the function value at this location, the number of iterations performed, and the status of the
         computation ("Success" or "Failure").
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
                    return None, None, None, result_status

                if np.isinf(first_derivative_at_x) or np.isnan(first_derivative_at_x):
                    print("Invalid first derivative encountered.")
                    result_status = "Failure"
                    return None, None, None, result_status

                x_k1 = x_k - first_derivative_at_x / second_derivative_at_x

                if np.isnan(x_k1):
                    result_status = "Failure"
                    return None, None, None, result_status

                if abs(x_k1 - x_k) < tolerance:
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
                        alpha: float = 0.01, beta: float = 0.5, max_value: float = 1e20) -> Tuple[
        Optional[float], Optional[float], int, str]:
        """
        Gradient descent method for optimizing a function by iteratively moving against the gradient.

        Parameters:
        - fun (sp.Expr): The function to optimize, represented as a SymPy expression.
        - uk (float): Initial guess for the minimum value.
        - max_iterations (int): Maximum allowed number of iterations.
        - tolerance (float): Convergence tolerance, the algorithm stops when the gradient's norm is less than this value.
        - alpha (float): Coefficient for the line search to ensure sufficient decrease in function value.
        - beta (float): Reduction factor for step size during line search.
        - max_value (float): Maximum allowed value for the function argument to prevent overflow or extreme values.

        Returns:
        Tuple[Optional[float], Optional[float], int, str]: Returns the optimized variable value, the function value at
        this optimized variable, the number of iterations used, and the status ("Success" or "Failure").
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
                return 0, 0, 0, result_status
            step_size = 1.0

            while fun(uk - step_size * grad_val) > fun(uk) - alpha * step_size * np.square(np.linalg.norm(grad_val)):
                step_size *= beta

            uk = uk - step_size * grad_val
            if np.linalg.norm(grad_val) < tolerance:
                break
            i += 1

            if abs(uk) > max_value:
                result_status = "Failure"
                return 0, 0, 0, result_status

        return uk, fun(uk), i, result_status

    @staticmethod
    def random_search(fun_expr: sp.Expr, x_k: float, tolerance: float = 1e-6, step_size: float = 1,
                      max_iterations: int = 1000, shrink_step: bool = True) -> Tuple[float, float, int, str]:
        """
        Random search method for function optimization starting from an initial guess and exploring the function
        space randomly.

        Parameters:
        - fun_expr (sp.Expr): The function to optimize, given as a SymPy expression.
        - x_k (float): Initial guess for the optimal value.
        - tolerance (float): Tolerance for convergence; the search stops when the improvement between iterations is
        smaller than this value.
        - step_size (float): Initial step size for the random steps.
        - max_iterations (int): Maximum number of iterations to perform.
        - shrink_step (bool): Indicates whether to decrease the step size after each iteration to refine the search.

        Returns:
        Tuple[float, float, int, str]: Returns the optimized variable value, the best function value found, the number
         of iterations performed, and the result status ("Success" or "Failure").
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
        if iterations == max_iterations:
            return best_x, best_fun_val, iterations, "Failure"
        return best_x, best_fun_val, iterations, "Success"
