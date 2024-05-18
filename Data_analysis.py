import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.stats.multicomp as multi

def load_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("File not found. Please check the filename or path.")
        return None

def preprocess_data(df):
    unique_methods = df["Method"].unique()
    data = []
    for method in unique_methods:
        method_data = df[df["Method"] == method]["Time"]
        data.append(method_data)
    return unique_methods, data

def perform_kruskal_wallis_test(df):
    groups = [group['Time'].values for name, group in df.groupby('Method')]
    kruskal_result = stats.kruskal(*groups)
    print(f"Kruskal-Wallis Test: H-statistic = {kruskal_result.statistic}, p-value = {kruskal_result.pvalue}")
    return kruskal_result.pvalue

def perform_games_howell_test(df):
    comp = multi.MultiComparison(df['Time'], df['Method'])
    result = comp.tukeyhsd()
    summary = pd.DataFrame(data=result._results_table.data[1:], columns=result._results_table.data[0])
    print("Games-Howell Post-Hoc Test Results:")
    return summary

def main():
    filename = 'optimization_results2.csv'
    df = load_data(filename)
    if df is not None:
        unique_methods, data = preprocess_data(df)
        if perform_kruskal_wallis_test(df) < 0.05:
            print(perform_games_howell_test(df))

if __name__ == "__main__":
    main()