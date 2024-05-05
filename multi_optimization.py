import time
import sympy as sp
from PointOptimizationMethods import PointOptimizationMethods
from IntervalOptimizationMethods import IntervalOptimizationMethods
import matplotlib.pyplot as plt
import numpy as np
import csv

# Define the test functions
x = sp.symbols('x')
test_functions = {
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
    'Exponential 1': sp.exp(x**2),
    'Exponential 2': 2 ** x - x ** 2,
    'Exponential 3': 2 ** x * 9*x**2,
    'Logarithmic 1': sp.log(sp.exp(x**2) + x + 1),
    'Logarithmic 2': x * sp.log(x) - x ** 0.5,
    'Logarithmic 3': x*sp.log(x) + x ** 2
}

function_types = {
    'Quadratic': ['Quadratic 1', 'Quadratic 2', 'Quadratic 3', 'Quadratic 4', 'Quadratic 5'],
    'Cubic': ['Cubic 1', 'Cubic 2', 'Cubic 3', 'Cubic 4', 'Cubic 5'],
    'Quartic': ['Quartic 1', 'Quartic 2', 'Quartic 3', 'Quartic 4', 'Quartic 5'],
    'Exponential': ['Exponential 1', 'Exponential 2', 'Exponential 3'],
    'Logarithmic': ['Logarithmic 1', 'Logarithmic 2', 'Logarithmic 3']
}


# Define initial intervals and parameters for interval optimization
initial_intervals = [(0, 1), (1, 2), (2, 3)]
interval_precision = 1e-6

# Define initial points and parameters for point optimization
initial_points = [0, 1, 2]
point_precision = 1e-6
max_iterations = 1000

# Test each function with each optimization method
interval_results = {}
point_results = {}

for name, func in test_functions.items():
    interval_results[name] = {}
    point_results[name] = {}

    # Interval Optimization
    for interval in initial_intervals:
        interval_results[name][interval] = {}

        start_time = time.time()
        x_opt, f_val, iterations = IntervalOptimizationMethods.golden_ratio_optimization(func, *interval,
                                                                                         interval_precision)
        elapsed_time = time.time() - start_time
        interval_results[name][interval]['GoldenRatio'] = (x_opt, f_val, iterations, elapsed_time)

        start_time = time.time()
        x_opt, f_val, iterations = IntervalOptimizationMethods.fibonacci_optimization(func, *interval,
                                                                                      interval_precision)
        elapsed_time = time.time() - start_time
        interval_results[name][interval]['Fibonacci'] = (x_opt, f_val, iterations, elapsed_time)

        start_time = time.time()
        x_opt, f_val, iterations = IntervalOptimizationMethods.bisection_optimization(func, *interval, delta=0.1,
                                                                                      epsilon=interval_precision)
        elapsed_time = time.time() - start_time
        interval_results[name][interval]['Bisection'] = (x_opt, f_val, iterations, elapsed_time)

    # Point Optimization
    for point in initial_points:
        point_results[name][point] = {}

        start_time = time.time()
        x_opt, f_val, iterations = PointOptimizationMethods.newtons_method(func, point, point_precision, max_iterations)
        elapsed_time = time.time() - start_time
        point_results[name][point]['Newton'] = (x_opt, f_val, iterations, elapsed_time)

        start_time = time.time()
        x_opt, f_val, iterations = PointOptimizationMethods.gradient_method(func, point, max_iterations,
                                                                            point_precision)
        elapsed_time = time.time() - start_time
        point_results[name][point]['Gradient'] = (x_opt, f_val, iterations, elapsed_time)

        start_time = time.time()
        x_opt, f_val, iterations = PointOptimizationMethods.random_search(func, point, point_precision, 1,
                                                                          max_iterations, True)
        elapsed_time = time.time() - start_time
        point_results[name][point]['Random'] = (x_opt, f_val, iterations, elapsed_time)


# Initialize dictionary to store average times for interval optimization
interval_average_times = {ftype: {'GoldenRatio': 0, 'Fibonacci': 0, 'Bisection': 0} for ftype in function_types}

# Aggregate the times for each method across functions of the same type for interval optimization
for ftype, fnames in function_types.items():
    num_intervals = len(initial_intervals)
    for fname in fnames:
        for interval in interval_results[fname]:
            for method in interval_results[fname][interval]:
                interval_average_times[ftype][method] += interval_results[fname][interval][method][3] / num_intervals

# Initialize dictionary to store average times for point optimization
point_average_times = {ftype: {'Newton': 0, 'Gradient': 0, 'Random': 0} for ftype in function_types}

# Aggregate the times for each method across functions of the same type for point optimization
for ftype, fnames in function_types.items():
    num_points = len(initial_points)
    for fname in fnames:
        for point in point_results[fname]:
            for method in point_results[fname][point]:
                point_average_times[ftype][method] += point_results[fname][point][method][3] / num_points


def save_optimization_results():
    with open('optimization_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Optimization Type', 'Function Name', 'Parameter', 'Method', 'Optimal x', 'Function Value', 'Iterations',
             'Time'])

        # Write interval optimization results
        for func_name, intervals in interval_results.items():
            for interval, methods in intervals.items():
                for method, result in methods.items():
                    writer.writerow(
                        ['Interval', func_name, f"Interval {interval}", method, result[0], result[1], result[2],
                         result[3]])

        # Write point optimization results
        for func_name, points in point_results.items():
            for point, methods in points.items():
                for method, result in methods.items():
                    writer.writerow(
                        ['Point', func_name, f"Point {point}", method, result[0], result[1], result[2], result[3]])


# Call function to save results to CSV
save_optimization_results()

# Plotting for interval optimization
fig, ax = plt.subplots()
index = np.arange(len(function_types))
bar_width = 0.2
opacity = 0.8

# Create bars for each method for interval optimization
for i, method in enumerate(['GoldenRatio', 'Fibonacci', 'Bisection']):
    execution_times = [interval_average_times[ftype][method] for ftype in function_types]
    ax.bar(index + i * bar_width, execution_times, bar_width, alpha=opacity, label=method)

# Labeling and aesthetics for interval optimization
ax.set_xlabel('Function Type')
ax.set_ylabel('Average Execution Time (s)')
ax.set_title('Average Optimization Execution Time (Interval Optimization)')
ax.set_xticks(index + bar_width / 2 * (len(interval_average_times) - 1))
ax.set_xticklabels(function_types.keys())
ax.legend()

fig.tight_layout()
plt.show()

# Plotting for point optimization
fig, ax = plt.subplots()
index = np.arange(len(function_types))
bar_width = 0.25
opacity = 0.8

# Create bars for each method for point optimization
for i, method in enumerate(['Newton', 'Gradient', 'Random']):
    execution_times = [point_average_times[ftype][method] for ftype in function_types]
    ax.bar(index + i * bar_width, execution_times, bar_width, alpha=opacity, label=method)

# Labeling and aesthetics for point optimization
ax.set_xlabel('Function Type')
ax.set_ylabel('Average Execution Time (s)')
ax.set_title('Average Optimization Execution Time (Point Optimization)')
ax.set_xticks(index + bar_width / 2 * (len(point_average_times) - 1))
ax.set_xticklabels(function_types.keys())
ax.legend()

fig.tight_layout()
plt.show()
