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


def perform_shapiro_tests(data, unique_methods):
    for i, method_data in enumerate(data, 1):
        stat, p_value = stats.shapiro(method_data)
        print(f"Shapiro-Wilk test for method {unique_methods[i - 1]}: Statistic: {stat}, p-value: {p_value}")
        print(
            "Data is normally distributed (fail to reject H0)\n" if p_value > 0.05 else "Data is not normally distributed (reject H0)\n")


def check_variances_homogeneity(data):
    stat, p_value = stats.bartlett(*data)
    print(f"Bartlett's test for homogeneity of variances: Statistic: {stat}, p-value: {p_value}")
    print(
        "Variances are homogeneous (fail to reject H0)" if p_value > 0.05 else "Variances are not homogeneous (reject H0)\n")


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


def games_howell_posthoc(data_dict):
    data = []
    labels = []
    for k, v in data_dict.items():
        data.extend(v)
        labels.extend([k] * len(v))

    comp = multi.MultiComparison(data, labels)
    posthoc_results = comp.tukeyhsd(alpha=0.05)

    print("Games-Howell Post-Hoc Test Results:")
    return posthoc_results.summary()


def main():
    filename = 'optimization_results2.csv'
    df = load_data(filename)
    if df is not None:
        unique_methods, data = preprocess_data(df)
        perform_shapiro_tests(data, unique_methods)
        check_variances_homogeneity(data)
        if perform_kruskal_wallis_test(df) < 0.05:
            print(perform_games_howell_test(df))


if __name__ == "__main__":
    main()
