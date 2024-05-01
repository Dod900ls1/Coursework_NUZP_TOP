from PointOptimizationMethods import PointOptimizationMethods
from IntervalOptimizationMethods import IntervalOptimizationMethods
import sympy as sp

if __name__ == '__main__':
    x = sp.symbols('x')
    f = x ** 4 / 20 + x / 4 + 1


    x_optimal_newton, best_function_value_newton, iterations_newton = PointOptimizationMethods.newtons_method(f, x_k=3)
    print("Newton's Method:")
    print("Optimal value (x):", x_optimal_newton)
    print("Best function value:", best_function_value_newton)
    print("Iterations:", iterations_newton)
    print()

    x_optimal_gradient, best_function_value_gradient, iterations_gradient = PointOptimizationMethods.gradient_method(
        f, uk=3)
    print("Gradient Descent Method:")
    print("Optimal value (x):", x_optimal_gradient)
    print("Best function value:", best_function_value_gradient)
    print("Iterations:", iterations_gradient)
    print()

    x_optimal_random, best_function_value_random, iterations_random = PointOptimizationMethods.random_search(f, x_k=3,
                                                                                                             shrink_step=True)
    print("Random Search Method:")
    print("Optimal value (x):", x_optimal_random)
    print("Best function value:", best_function_value_random)
    print("Iterations:", iterations_random)
    print()

    x_optimal_golden, best_function_value_golden, iterations_golden = IntervalOptimizationMethods.golden_ratio_optimization(
        f, a=-2, b=2)
    print("Golden Ratio Optimization Method:")
    print("Optimal value (x):", x_optimal_golden)
    print("Best function value:", best_function_value_golden)
    print("Iterations:", iterations_golden)
    print()

    minimum_fibonacci, x_fibonacci, iterations_fibonacci = IntervalOptimizationMethods.fibonacci_optimization(f,
                                                                                                              lower_bound=-2,
                                                                                                              upper_bound=2,
                                                                                                              tolerance=1e-6)
    print("Fibonacci Optimization Method:")
    print("Optimal value (x):", x_fibonacci)
    print("Best function value:", minimum_fibonacci)
    print("Iterations:", iterations_fibonacci)
    print()

    x_min_bisection, minimum_bisection, iterations_bisection = IntervalOptimizationMethods.bisection_optimization(f,
                                                                                                                  a=-2,
                                                                                                                  b=2,
                                                                                                                  delta=0.1,
                                                                                                                  epsilon=1e-6)
    print("Bisection Optimization Method:")
    print("Optimal value (x):", x_min_bisection)
    print("Best function value:", minimum_bisection)
    print("Iterations:", iterations_bisection)
