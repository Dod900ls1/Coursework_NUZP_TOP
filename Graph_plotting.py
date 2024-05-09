import pandas as pd
import matplotlib.pyplot as plt

def read_and_process_data(filename):
    """Reads data from a CSV file."""
    return pd.read_csv(filename)

def compute_average_times(data, function_types):
    """Computes average times for each method, function type, and precision."""
    avg_results = {}
    for precision, precision_data in data.groupby('Precision'):
        avg_results[precision] = {}
        for method_name, method_data in precision_data.groupby('Method'):
            avg_results[precision][method_name] = {
                function_type: method_data[method_data['Function Name'].str.startswith(function_type)]['Time'].mean()
                for function_type in function_types
            }
    return avg_results

def plot_results(avg_results_by_function, function_types, title_prefix, file_prefix):
    """Plots bar charts for each precision and combined."""
    for precision, results in avg_results_by_function.items():
        df = pd.DataFrame(results).fillna(0)
        df.plot(kind='bar', figsize=(10, 6))
        plt.title(f'{title_prefix} - Precision {precision}')
        plt.xlabel('Function Type')
        plt.ylabel('Average Time')
        plt.xticks(rotation=45)
        plt.legend(title='Method')
        plt.tight_layout()
        plt.savefig(f"images/{file_prefix}_{precision}.png")
        plt.show()

    # Combine all precision results
    combined_results = {method: pd.DataFrame().from_dict({precision: data[method] for precision, data in avg_results_by_function.items()}).mean(axis=1) for method in avg_results_by_function[list(avg_results_by_function.keys())[0]].keys()}
    pd.DataFrame(combined_results).plot(kind='bar', figsize=(10, 6))
    plt.title(f'{title_prefix} - All Precisions Combined')
    plt.xlabel('Function Type')
    plt.ylabel('Average Time')
    plt.xticks(rotation=45)
    plt.legend(title='Method')
    plt.tight_layout()
    plt.savefig(f"images/{file_prefix}_combined.png")
    plt.show()

def load_and_plot_histograms(data, file_prefix):
    """Loads data and plots histograms for each method by precision and combined."""
    for precision, precision_data in data.groupby('Precision'):
        methods = precision_data['Method'].unique()
        plt.figure(figsize=(12, 6))
        for i, method in enumerate(methods, 1):
            plt.subplot(2, 3, i)
            plt.hist(precision_data[precision_data['Method'] == method]['Time'], bins=10, edgecolor='black')
            plt.title(f"{method} - Precision {precision}")
            plt.xlabel("Time")
            plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(f"images/{file_prefix}_histograms_{precision}.png")
        plt.show()

    # Combine all precision data for histograms
    plt.figure(figsize=(12, 6))
    for i, method in enumerate(methods, 1):
        combined_data = [data[data['Method'] == method]['Time'] for precision, data in data.groupby('Precision')]
        plt.subplot(2, 3, i)
        plt.hist(combined_data, bins=10, edgecolor='black', stacked=True)
        plt.title(f"{method} - Combined")
        plt.xlabel("Time")
        plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"images/{file_prefix}_histograms_combined.png")
    plt.show()

def plot_boxplots(data, file_prefix):
    """Plots boxplots for each method by precision and combined."""
    for precision, precision_data in data.groupby('Precision'):
        plt.figure(figsize=(10, 6))
        precision_data.boxplot(by='Method', column='Time', grid=False)
        plt.title(f"Boxplots by Method - Precision {precision}")
        plt.suptitle('')
        plt.xlabel("Method")
        plt.ylabel("Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"images/{file_prefix}_boxplots_{precision}.png")
        plt.show()

    # Combined boxplots
    plt.figure(figsize=(10, 6))
    data.boxplot(by='Method', column='Time', grid=False)
    plt.title("Boxplots by Method - All Precisions Combined")
    plt.suptitle('')
    plt.xlabel("Method")
    plt.ylabel("Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"images/{file_prefix}_boxplots_combined.png")
    plt.show()

def main():
    function_types = ['Quadratic', 'Cubic', 'Quartic', 'Exponential', 'Logarithmic']
    optimization_data = read_and_process_data('optimization_results2.csv')
    optimization_data = optimization_data[optimization_data['Result'] == 'Success']  # Filter successful optimizations

    avg_results_by_function = compute_average_times(optimization_data, function_types)
    plot_results(avg_results_by_function, function_types, 'Optimization Method Comparison', 'optimization_plots')

    load_and_plot_histograms(optimization_data, 'optimization_data')
    plot_boxplots(optimization_data, 'optimization_data')

if __name__ == "__main__":
    main()
