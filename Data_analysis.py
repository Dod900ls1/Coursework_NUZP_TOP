import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv("ANOVA_results.csv")
unique_methods = df["Method"].unique()
data = []

for method in unique_methods:
    method_data = df[df["Method"] == method]["Time"]
    data.append(method_data)

for i, method_data in enumerate(data, 1):
    # Shapiro-Wilk test for normality
    shapiro_stat, shapiro_p_value = stats.shapiro(method_data)
    print(f"Shapiro-Wilk test for method {unique_methods[i-1]}:")
    print("Test statistic:", shapiro_stat)
    print("p-value:", shapiro_p_value)
    if shapiro_p_value > 0.05:
        print("Data is normally distributed (fail to reject H0)\n")
    else:
        print("Data is not normally distributed (reject H0)\n")
"""
This cycle showed that 4 out of 6 data groups were not normally distributed
"""

# Check homogeneity of variances assumption
bartlett_stat, bartlett_p_value = stats.bartlett(*data)
print("\nBartlett's test for homogeneity of variances:")
print("Test statistic:", bartlett_stat)
print("p-value:", bartlett_p_value)
if bartlett_p_value > 0.05:
    print("Variances are homogeneous (fail to reject H0)")
else:
    print("Variances are not homogeneous (reject H0)")
"""
This one shows that our variances are not homogeneous.
Thus - we do bootstrap to compare means.
"""

def bootstrap(x, Nboot, statfun):
    resampled_stat = []
    for k in range(Nboot):
        index = np.random.randint(0, len(x), len(x))
        sample = x.iloc[index]
        bstats = statfun(sample)
        resampled_stat.append(bstats)

    return np.array(resampled_stat)

bootstrap_means_list = []
for i in range(len(data)):
    bootstrap_means = bootstrap(data[i], 400, np.mean)
    bootstrap_means_list.append(bootstrap_means)

bootstrap_means_df = pd.DataFrame()
for i, method in enumerate(unique_methods):
    method_bootstrap_means = bootstrap_means_list[i]
    method_df = pd.DataFrame({
        "Bootstrapped_Mean": method_bootstrap_means,
        "Method": method
    })
    # Ensuring no all-NA columns exist, you can include any specific checks or handling here if needed
    bootstrap_means_df = pd.concat([bootstrap_means_df, method_df], ignore_index=True)

groups = []
for method in unique_methods:
    groups.append(bootstrap_means_df[bootstrap_means_df['Method'] == method]['Bootstrapped_Mean'].values)
for data, method in zip(groups, unique_methods):
    shapiro_stat, shapiro_p_value = stats.shapiro(data)
    print(f"Shapiro-Wilk test for {method} - Statistic: {shapiro_stat}, P-value: {shapiro_p_value}")

bartlett_stat, bartlett_p_value = stats.bartlett(*groups)
print(f"Bartlett's test - Statistic: {bartlett_stat}, P-value: {bartlett_p_value}")



# Plotting
plt.figure(figsize=(12, 6))
for i, group_data in enumerate(groups):
    plt.subplot(1, len(groups), i + 1)
    plt.hist(group_data, bins=20, alpha=0.7)
    plt.title(unique_methods[i])
plt.tight_layout()
plt.show()

# Boxplot for visualizing variances
plt.figure(figsize=(10, 6))
plt.boxplot(groups, labels=unique_methods)
plt.title('Comparison of Bootstrapped Means Across Methods')
plt.ylabel('Bootstrapped Mean')
plt.show()
# Performing ANOVA
# anova_result = stats.f_oneway(*groups)
# print(anova_result)


