import pandas as pd
import matplotlib.pyplot as plt

# Function types
function_types = ['Quadratic', 'Cubic', 'Quartic', 'Exponential', 'Logarithmic']

# Read data from CSV file
data = pd.read_csv('optimization_results.csv')

# Dictionary to store average results by function
avg_results_by_function = {}

# Function to calculate average time
def calculate_average_time(results):
    success_results = results[results['Result'] == 'Success']
    if len(success_results) == 0:
        return 0
    return success_results['Time'].mean()

# Iterate over each method
for method_name, method_data in data.groupby('Method'):
    avg_results_by_function[method_name] = {}
    # Iterate over each function type
    for function_type in function_types:
        # Filter data for the current function type
        function_data = method_data[method_data['Function Name'].str.startswith(function_type)]
        # Calculate average time for the current function type
        avg_time = calculate_average_time(function_data)
        # Store the average time in the dictionary
        avg_results_by_function[method_name][function_type] = avg_time

# Convert dictionary to DataFrame
df = pd.DataFrame(avg_results_by_function)

# Separate methods for two plots
methods_plot1 = ['Bisection', 'Fibonacci', 'GoldenRatio']
methods_plot2 = [method for method in df.columns if method not in methods_plot1]

# Plotting the bar chart for methods Bisection, Fibonacci, and GoldenRatio
plt.figure(figsize=(8, 6))
df[methods_plot1].plot(kind='bar', ax=plt.gca())
plt.title('Bisection, Fibonacci, GoldenRatio')
plt.xlabel('Function Type')
plt.ylabel('Average Time')
plt.xticks(rotation=45)
plt.legend(title='Method')
plt.tight_layout()
plt.savefig('methods_bisection_fibonacci_goldenratio.png')  # Save the plot as an image
plt.show()

# Plotting the bar chart for the rest of the methods
plt.figure(figsize=(8, 6))
df[methods_plot2].plot(kind='bar', ax=plt.gca())
plt.title('Other Methods')
plt.xlabel('Function Type')
plt.ylabel('Average Time')
plt.xticks(rotation=45)
plt.legend(title='Method')
plt.tight_layout()
plt.savefig('methods_other.png')  # Save the plot as an image
plt.show()
