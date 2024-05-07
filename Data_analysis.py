import pandas as pd
from scipy.stats import f_oneway
from scipy.stats import shapiro
from scipy.stats import levene


# Load data from CSV file
df = pd.read_csv("ANOVA_results.csv")

# Extract unique method names
unique_methods = df["Method"].unique()

# Initialize a list to store data for each method
data = []

# Iterate over unique method names
for method in unique_methods:
    method_data = df[df["Method"] == method]["Time"]
    data.append(method_data)

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(*data)

# Display ANOVA results
print("ANOVA F-statistic:", f_statistic)
print("ANOVA p-value:", p_value)
