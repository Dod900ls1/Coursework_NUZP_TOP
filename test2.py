import time
import sympy as sp
from PointOptimizationMethods import PointOptimizationMethods
from IntervalOptimizationMethods import IntervalOptimizationMethods
import matplotlib.pyplot as plt
import numpy as np


# Define the test functions
x = sp.symbols('x')
test_functions = {
    'Quadratic 1': x ** 2 - 8 * x + 8,
    'Quadratic 2': x ** 2 + 4 * x + 4,
    'Quadratic 3': 3 * x ** 2 - 3 * x + 1,
    'Quadratic 4': -x ** 2 + 2 * x - 1,
    'Quadratic 5': 0.5 * x ** 2 - 5 * x + 12,
    'Cubic 1': x ** 3 - 3 * x ** 2 + 3 * x - 1,
    'Cubic 2': -x ** 3 + 6 * x ** 2 - 9 * x + 4,
    'Cubic 3': 2 * x ** 3 - 6 * x ** 2 + 4 * x,
    'Cubic 4': x ** 3 + x ** 2 - 4 * x - 4,
    'Cubic 5': 4 * x ** 3 - 12 * x ** 2 + 9 * x - 2,
    'Quartic 1': x ** 4 - 4 * x ** 3 + 6 * x ** 2 - 4 * x + 1,
    'Quartic 2': -2 * x ** 4 + 8 * x ** 3 - 12 * x ** 2 + 8 * x - 2,
    'Quartic 3': 0.5 * x ** 4 - x ** 3 - 3.5 * x ** 2 + 2 * x + 10,
    'Quartic 4': x ** 4 + 2 * x ** 3 - 13 * x ** 2 + 14 * x - 24,
    'Quartic 5': 3 * x ** 4 - 6 * x ** 3 + 3 * x ** 2 - 6 * x + 2
}

function_types = {
    'Quadratic': ['Quadratic 1', 'Quadratic 2', 'Quadratic 3', 'Quadratic 4', 'Quadratic 5'],
    'Cubic': ['Cubic 1', 'Cubic 2', 'Cubic 3', 'Cubic 4', 'Cubic 5'],
    'Quartic': ['Quartic 1', 'Quartic 2', 'Quartic 3', 'Quartic 4', 'Quartic 5']
}


# Define initial intervals and parameters
initial_intervals = [(0, 1), (1, 2), (2, 3)]
precision = 1e-6

# Test each function with each optimization method
results = {}
for name, func in test_functions.items():
    results[name] = {}
    for interval in initial_intervals:
        results[name][interval] = {}

        # Golden Ratio Optimization
        start_time = time.time()
        x_opt, f_val, iterations = IntervalOptimizationMethods.golden_ratio_optimization(func, *interval, precision)
        elapsed_time = time.time() - start_time
        results[name][interval]['GoldenRatio'] = (x_opt, f_val, iterations, elapsed_time)

        # Fibonacci Optimization
        start_time = time.time()
        x_opt, f_val, iterations = IntervalOptimizationMethods.fibonacci_optimization(func, *interval, precision)
        elapsed_time = time.time() - start_time
        results[name][interval]['Fibonacci'] = (x_opt, f_val, iterations, elapsed_time)

        # Bisection Optimization
        start_time = time.time()
        x_opt, f_val, iterations = IntervalOptimizationMethods.bisection_optimization(func, *interval, delta=0.1, epsilon=precision)
        elapsed_time = time.time() - start_time
        results[name][interval]['Bisection'] = (x_opt, f_val, iterations, elapsed_time)

# Display results
for func_name, intervals in results.items():
    print(f"Results for {func_name}:")
    for interval, methods in intervals.items():
        print(f"  Starting interval {interval}:")
        for method, result in methods.items():
            print(
                f"    {method}: Optimal x = {result[0]}, Function value = {result[1]}, Iterations = {result[2]}, Time = {result[3]:.4f}s")


# Define function types
function_types = {
    'Quadratic': ['Quadratic 1', 'Quadratic 2', 'Quadratic 3', 'Quadratic 4', 'Quadratic 5'],
    'Cubic': ['Cubic 1', 'Cubic 2', 'Cubic 3', 'Cubic 4', 'Cubic 5'],
    'Quartic': ['Quartic 1', 'Quartic 2', 'Quartic 3', 'Quartic 4', 'Quartic 5']
}

# Initialize dictionary to store average times
average_times = {ftype: {'GoldenRatio': 0, 'Fibonacci': 0, 'Bisection': 0}
                 for ftype in function_types}

# Aggregate the times for each method across functions of the same type
for ftype, fnames in function_types.items():
    num_intervals = len(initial_intervals)
    for fname in fnames:
        for interval in results[fname]:
            for method in results[fname][interval]:
                average_times[ftype][method] += results[fname][interval][method][3] / num_intervals

# Plotting
fig, ax = plt.subplots()
index = np.arange(len(function_types))
bar_width = 0.2
opacity = 0.8

# Create bars for each method
for i, method in enumerate(['GoldenRatio', 'Fibonacci', 'Bisection']):
    execution_times = [average_times[ftype][method] for ftype in function_types]
    ax.bar(index + i * bar_width, execution_times, bar_width, alpha=opacity, label=method)

# Labeling and aesthetics
ax.set_xlabel('Function Type')
ax.set_ylabel('Average Execution Time (s)')
ax.set_title('Average Optimization Execution Time by Function Type and Method')
ax.set_xticks(index + bar_width / 2 * (len(average_times) - 1))
ax.set_xticklabels(function_types.keys())
ax.legend()

fig.tight_layout()
plt.show()
