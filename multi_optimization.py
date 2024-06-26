import time
import sympy as sp
from PointOptimizationMethods import PointOptimizationMethods
from IntervalOptimizationMethods import IntervalOptimizationMethods
import csv


# Define the test functions
def define_functions():
    x = sp.symbols('x')
    return {
        'Quadratic 1': x ** 2 - 8 * x + 8,
        'Quadratic 2': x ** 2 + 4 * x + 4,
        'Quadratic 3': 3 * x ** 2 - 3 * x + 1,
        'Quadratic 4': x ** 2 + 2 * x - 1,
        'Quadratic 5': 0.5 * x ** 2 - 5 * x + 12,
        'Cubic 1': x ** 3 - 3 * x - 1,
        'Cubic 2': -x ** 3 + 6 * x ** 2 - 9 * x + 4,
        'Cubic 3': 2 * x ** 3 - 6 * x ** 2 + 4 * x,
        'Cubic 4': x ** 3 + x ** 2 - 4 * x - 4,
        'Cubic 5': 4 * x ** 3 - 12 * x ** 2 + 9 * x - 2,
        'Quartic 1': x ** 4 - 4 * x ** 3 + 6 * x ** 2 - 4 * x + 1,
        'Quartic 2': -2 * x ** 4 + 8 * x ** 3 - 12 * x ** 2 + 8 * x - 2,
        'Quartic 3': 0.5 * x ** 4 - x ** 3 - 3.5 * x ** 2 + 2 * x + 10,
        'Quartic 4': x ** 4 + 2 * x ** 3 - 13 * x ** 2 + 14 * x - 24,
        'Quartic 5': 3 * x ** 4 - 6 * x ** 3 + 3 * x ** 2 - 6 * x + 2,
        'Exponential 1': sp.exp(x ** 2),
        'Exponential 2': 2 ** x - x ** 2,
        'Exponential 3': 2 ** x * 9 * x ** 2,
        'Logarithmic 1': sp.log(sp.exp(x ** 2) + x + 1),
        'Logarithmic 2': x * sp.log(x) - x ** 0.5,
        'Logarithmic 3': x * sp.log(x) + x ** 2
    }


def define_function_types():
    return {
        'Quadratic': ['Quadratic 1', 'Quadratic 2', 'Quadratic 3', 'Quadratic 4', 'Quadratic 5'],
        'Cubic': ['Cubic 1', 'Cubic 2', 'Cubic 3', 'Cubic 4', 'Cubic 5'],
        'Quartic': ['Quartic 1', 'Quartic 2', 'Quartic 3', 'Quartic 4', 'Quartic 5'],
        'Exponential': ['Exponential 1', 'Exponential 2', 'Exponential 3'],
        'Logarithmic': ['Logarithmic 1', 'Logarithmic 2', 'Logarithmic 3']
    }


def perform_optimizations(test_functions, initial_intervals, initial_points, precisions, max_iterations):
    interval_results, point_results = {}, {}
    for precision in precisions:
        for name, func in test_functions.items():
            interval_results.setdefault(name, {})
            point_results.setdefault(name, {})
            run_interval_optimizations(func, interval_results[name], initial_intervals, precision)
            run_point_optimizations(func, point_results[name], initial_points, precision, max_iterations)
    return interval_results, point_results


def run_interval_optimizations(func, results_dict, intervals, precision):
    for interval in intervals:
        results_dict[interval] = {}
        results_dict[interval]['GoldenRatio'] = run_optimization(func,
                                                                 IntervalOptimizationMethods.golden_ratio_optimization,
                                                                 *interval, tolerance=precision)
        results_dict[interval]['Fibonacci'] = run_optimization(func, IntervalOptimizationMethods.fibonacci_optimization,
                                                               *interval, tolerance=precision)
        results_dict[interval]['Bisection'] = run_optimization(func, IntervalOptimizationMethods.bisection_optimization,
                                                               *interval, delta=0.1, tolerance=precision)


def run_point_optimizations(func, results_dict, points, tolerance, max_iterations):
    for point in points:
        results_dict[point] = {}
        results_dict[point]['Newton'] = run_optimization(func, PointOptimizationMethods.newtons_method, point,
                                                         tolerance, max_iterations)
        results_dict[point]['Gradient'] = run_optimization(func, PointOptimizationMethods.gradient_method, point,
                                                           max_iterations, tolerance)
        results_dict[point]['Random'] = run_optimization(func, PointOptimizationMethods.random_search, point, tolerance,
                                                         1, max_iterations)


def run_optimization(func, method, *args, **kwargs):
    start_time = time.time()
    result = method(func, *args, **kwargs)  # Ensure args are correctly passed
    elapsed_time = time.time() - start_time
    return result + (elapsed_time,)


def save_optimization_results(all_interval_results, all_point_results, filename='optimization_results.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Optimization Type', 'Function Name', 'Parameter', 'Method', 'Optimal x', 'Function Value', 'Iterations',
             'Result', 'Time', 'Precision'])
        for precision, interval_results in all_interval_results.items():
            for func_name, results_by_name in interval_results.items():
                for param, methods in results_by_name.items():
                    for method, results in methods.items():
                        writer.writerow(['Interval', func_name, param, method] + list(results) + [precision])
        for precision, point_results in all_point_results.items():
            for func_name, results_by_name in point_results.items():
                for param, methods in results_by_name.items():
                    for method, results in methods.items():
                        writer.writerow(['Point', func_name, param, method] + list(results) + [precision])


def write_results(writer, optimization_type, results, precision):
    for func_name, params in results.items():
        for param, methods in params.items():
            for method, result in methods.items():
                writer.writerow(
                    [optimization_type, func_name, f"{optimization_type} {param}", method] + list(result) + [precision])


def main():
    test_functions = define_functions()
    initial_intervals = [(-2, 2), (-4, 4), (-8, 8)]
    initial_points = [0, 1, 2]
    precisions = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]  # List of precisions
    max_iterations = 1000

    all_interval_results = {}
    all_point_results = {}
    for precision in precisions:
        interval_results, point_results = perform_optimizations(test_functions, initial_intervals, initial_points,
                                                                [precision], max_iterations)
        all_interval_results[precision] = interval_results
        all_point_results[precision] = point_results

    save_optimization_results(all_interval_results, all_point_results, 'optimization_results2.csv')


if __name__ == "__main__":
    main()
