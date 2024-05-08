import pandas as pd
import matplotlib.pyplot as plt


def read_and_process_data(filename):
    """Reads data from a CSV file and filters successful optimizations."""
    data = pd.read_csv(filename)
    return data[data['Result'] == 'Success']


def compute_average_times(data, function_types):
    """Computes average times for each method and function type."""
    avg_results_by_function = {}
    for method_name, method_data in data.groupby('Method'):
        avg_results_by_function[method_name] = {
            function_type: method_data[method_data['Function Name'].str.startswith(function_type)]['Time'].mean()
            for function_type in function_types
        }
    return avg_results_by_function


def plot_results(df, methods, plot_title, file_name):
    """Plots and saves bar charts of the results."""
    plt.figure(figsize=(8, 6))
    df[methods].plot(kind='bar', ax=plt.gca())
    plt.title(plot_title)
    plt.xlabel('Function Type')
    plt.ylabel('Average Time')
    plt.xticks(rotation=45)
    plt.legend(title='Method')
    plt.tight_layout()
    plt.savefig(file_name)
    plt.show()


def load_and_plot_histograms(filename):
    """Loads data and plots histograms for each method."""
    df = pd.read_csv(filename)
    unique_methods = df['Method'].unique()
    data = [df[df['Method'] == method]['Time'] for method in unique_methods]

    plt.figure(figsize=(12, 6))
    for i, method_data in enumerate(data, 1):
        plt.subplot(2, 3, i)
        plt.hist(method_data, bins=10, edgecolor='black')
        plt.title(f"{unique_methods[i - 1]}")
        plt.xlabel("Time")
        plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("3.png")
    plt.show()

    return data, unique_methods

def plot_boxplots(data, unique_methods):
    """Plots boxplots for the given data."""
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=unique_methods)
    plt.title("Boxplot of Execution Times by Method")
    plt.xlabel("Method")
    plt.ylabel("Time")
    plt.savefig("2.png")
    plt.show()


def main():
    function_types = ['Quadratic', 'Cubic', 'Quartic', 'Exponential', 'Logarithmic']
    optimization_data = read_and_process_data('optimization_results.csv')
    avg_results_by_function = compute_average_times(optimization_data, function_types)

    df = pd.DataFrame(avg_results_by_function)
    methods_plot1 = ['Bisection', 'Fibonacci', 'GoldenRatio', 'Random']
    methods_plot2 = [method for method in df.columns if method not in methods_plot1]

    plot_results(df, methods_plot1, 'Bisection, Fibonacci, GoldenRatio', "5.png")
    plot_results(df, methods_plot2, 'Other Methods', "4.png")

    data, unique_methods = load_and_plot_histograms("ANOVA_results.csv")

    plot_boxplots(data, unique_methods)


if __name__ == "__main__":
    main()
