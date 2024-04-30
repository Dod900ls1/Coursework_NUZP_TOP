from PointOptimizationMethods import PointOptimizationMethods
from IntervalOptimizationMethods import IntervalOptimizationMethods
import sympy as sp

if __name__ == '__main__':
    # Define the symbolic expression for Newton's method
    x = sp.symbols('x')
    f = x ** 4 / 20 + x / 4 + 1


    # Define the function for gradient descent
    def fun(x):
        return x ** 4 / 20 + x / 4 + 1


    # Newton's optimization method
    x_optimal_newton, best_function_value_newton, iterations_newton = PointOptimizationMethods.newtons_method(f, x_k=3)
    print("Newton's Method:")
    print("Optimal value (x):", x_optimal_newton)
    print("Best function value:", best_function_value_newton)
    print("Iterations:", iterations_newton)
    print()

    # Gradient optimization method
    x_optimal_gradient, best_function_value_gradient, iterations_gradient = PointOptimizationMethods.gradient_method(
        fun, uk=3)
    print("Gradient Descent Method:")
    print("Optimal value (x):", x_optimal_gradient)
    print("Best function value:", best_function_value_gradient)
    print("Iterations:", iterations_gradient)
    print()

    # Random search optimization method
    x_optimal_random, best_function_value_random, iterations_random = PointOptimizationMethods.random_search(f, x_k=3,
                                                                                                             shrink_step=True)
    print("Random Search Method:")
    print("Optimal value (x):", x_optimal_random)
    print("Best function value:", best_function_value_random)
    print("Iterations:", iterations_random)
    print()

    # Golden ratio optimization method
    x_optimal_golden, best_function_value_golden, iterations_golden = IntervalOptimizationMethods.golden_ratio_optimization(
        fun, a=2, b=-2)
    print("Golden Ratio Optimization Method:")
    print("Optimal value (x):", x_optimal_golden)
    print("Best function value:", best_function_value_golden)
    print("Iterations:", iterations_golden)