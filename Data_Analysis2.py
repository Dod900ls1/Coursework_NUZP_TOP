import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict


def read_and_filter_csv(file_path: str) -> pd.DataFrame:
    """
    Read the CSV file and filter the rows where the result is 'Success'.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Filtered DataFrame.
    """
    df = pd.read_csv(file_path)
    return df[df["Result"] == "Success"]


def compute_correlations(df: pd.DataFrame) -> Dict[str, float]:
    """
    Compute the correlation between iterations and precision for each unique method in the DataFrame.

    Args:
    - df (pd.DataFrame): The DataFrame containing optimization results.

    Returns:
    - Dict[str, float]: Dictionary of correlations for each method.
    """
    methods = df['Method'].unique()
    correlations = {}

    for method in methods:
        method_df = df[df['Method'] == method]
        correlation = method_df['Iterations'].corr(method_df['Precision'], method="spearman")
        correlations[method] = correlation

    return correlations


def plot_scatter_plots(df: pd.DataFrame) -> None:
    """
    Plot scatter plots of iterations vs. precision for each method.

    Args:
    - df (pd.DataFrame): The DataFrame containing optimization results.
    """
    methods = df['Method'].unique()

    for index, method in enumerate(methods):
        method_df = df[df['Method'] == method]
        plt.scatter(method_df['Iterations'], method_df['Precision'], label='Data Points')

        plt.title(f'Scatter Plot for Method: {method}')
        plt.xlabel('Iterations')
        plt.ylabel('Precision')
        plt.legend()
        plt.savefig(f'images/Plots{index}')
        plt.show()


def main(file_path: str) -> None:
    """
    Main function to read CSV, compute correlations, plot scatter plots, and print correlations.

    Args:
    - file_path (str): Path to the CSV file.
    """
    df = read_and_filter_csv(file_path)
    correlations = compute_correlations(df)
    plot_scatter_plots(df)

    for method, correlation in correlations.items():
        print(f'Method: {method}, Correlation: {correlation}')


if __name__ == '__main__':
    main('optimization_results2.csv')
