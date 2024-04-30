from PointOptimizationMethods import PointOptimizationMethods
import sympy as sp


if __name__ == '__main__':
    x = sp.symbols('x')
    f = x**4 / 20 + x / 4 + 1  # Symbolic function for Newton's method
    def fun(x):
        return x**4 / 20 + x / 4 + 1  # Regular Python function for gradient descent

    # Newton's optimization method
    print(PointOptimizationMethods.newtons_method(f, x_k=3))

    # Gradient optimization method
    print(PointOptimizationMethods.gradient_method(fun, uk=3))

    # Random search optimization method
    print(PointOptimizationMethods.random_search(f, x_k=3))
