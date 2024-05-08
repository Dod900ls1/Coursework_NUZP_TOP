import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

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
        print(f"Shapiro-Wilk test for method {unique_methods[i-1]}: Statistic: {stat}, p-value: {p_value}")
        print("Data is normally distributed (fail to reject H0)\n" if p_value > 0.05 else "Data is not normally distributed (reject H0)\n")

def check_variances_homogeneity(data):
    stat, p_value = stats.bartlett(*data)
    print(f"Bartlett's test for homogeneity of variances: Statistic: {stat}, p-value: {p_value}")
    print("Variances are homogeneous (fail to reject H0)" if p_value > 0.05 else "Variances are not homogeneous (reject H0)")

def bootstrap(data, Nboot, statfun):
    resampled_stat = []
    for k in range(Nboot):
        index = np.random.randint(0, len(data), len(data))
        sample = data.iloc[index]
        resampled_stat.append(statfun(sample))
    return np.array(resampled_stat)

def create_bootstrap_dataframe(data, unique_methods):
    bootstrap_means_list = [bootstrap(method_data, 400, np.mean) for method_data in data]
    bootstrap_means_df = pd.DataFrame()
    for method, bootstrap_means in zip(unique_methods, bootstrap_means_list):
        method_df = pd.DataFrame({"Bootstrapped_Mean": bootstrap_means, "Method": method})
        bootstrap_means_df = pd.concat([bootstrap_means_df, method_df], ignore_index=True)
    return bootstrap_means_df

def plot_histograms(groups, unique_methods):
    plt.figure(figsize=(12, 6))
    for i, group_data in enumerate(groups):
        plt.subplot(1, len(groups), i + 1)
        plt.hist(group_data, bins=20, alpha=0.7)
        plt.title(unique_methods[i])
    plt.tight_layout()
    plt.savefig('histograms.png')
    plt.show()

def plot_boxplots(groups, unique_methods):
    plt.figure(figsize=(10, 6))
    plt.boxplot(groups, labels=unique_methods)
    plt.title('Comparison of Bootstrapped Means Across Methods')
    plt.ylabel('Bootstrapped Mean')
    plt.savefig('boxplots.png')
    plt.show()

def main():
    df = load_data("ANOVA_results.csv")
    if df is not None:
        unique_methods, data = preprocess_data(df)
        perform_shapiro_tests(data, unique_methods)
        check_variances_homogeneity(data)
        bootstrap_means_df = create_bootstrap_dataframe(data, unique_methods)
        groups = [bootstrap_means_df[bootstrap_means_df['Method'] == method]['Bootstrapped_Mean'].values for method in unique_methods]
        plot_histograms(groups, unique_methods)
        plot_boxplots(groups, unique_methods)

if __name__ == "__main__":
    main()
