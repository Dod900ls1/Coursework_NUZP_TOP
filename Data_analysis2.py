import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy.stats import shapiro
import ast


def parse_parameter(param):
    """
    Parse the parameter string to extract a single value.
    If the parameter is an interval, return the start of the interval.
    If the parameter is a single value, return it as a float.
    """
    try:
        parsed = ast.literal_eval(param)
        if isinstance(parsed, tuple) and len(parsed) == 2:
            return parsed[0]
        elif isinstance(parsed, (int, float)):
            return parsed
    except (ValueError, SyntaxError):
        return np.nan


def sort_data(filename: str) -> pd.DataFrame:
    """
    This function sorts the data, deletes all columns except for:
     - Precision
     - Iterations
     - Function Name
     - Parameter
    And removes all rows where the result is "Failure".

    :param filename: str: The name of the CSV file to process.
    :return: pd.DataFrame: The cleaned DataFrame.
    """
    # Read the CSV file
    df = pd.read_csv(filename)

    # Select only the necessary columns
    df = df[['Function Name', 'Parameter', 'Iterations', 'Precision', 'Result']]

    # Remove rows where the result is "Failure"
    df = df[df['Result'] != 'Failure']

    # Parse the 'Parameter' column
    df['Parameter'] = df['Parameter'].apply(parse_parameter)

    return df


def check_model_assumptions(model):
    """
    Check the assumptions of the linear regression model.
    """
    residuals = model.resid
    fitted = model.fittedvalues

    # Normality of Residuals
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(residuals, kde=True)
    plt.title('Histogram of Residuals')

    plt.subplot(1, 2, 2)
    sm.qqplot(residuals, line='s')
    plt.title('Q-Q Plot of Residuals')
    plt.show()

    # Shapiro-Wilk test for normality
    shapiro_test = shapiro(residuals)
    print(f'Shapiro-Wilk test: W={shapiro_test.statistic}, p-value={shapiro_test.pvalue}')

    # Homoscedasticity
    plt.figure(figsize=(10, 6))
    plt.scatter(fitted, residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Fitted values')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Fitted values')
    plt.show()

    # Breusch-Pagan test for homoscedasticity
    test_bp = het_breuschpagan(residuals, model.model.exog)
    print(f'Breusch-Pagan test: Lagrange multiplier statistic={test_bp[0]}, p-value={test_bp[1]}')


def build_and_plot_linear_model(df: pd.DataFrame):
    """
    This function builds a linear model with Precision as the response variable
    and Iterations, Function Name, and Parameter as predictor variables.
    It also plots the residuals and the fitted model.

    :param df: pd.DataFrame: The cleaned DataFrame.
    :return: None
    """
    # Encode 'Function Name' as a categorical variable
    df = pd.get_dummies(df, columns=['Function Name'], drop_first=True)

    # Define the dependent and independent variables
    X = df.drop(columns=['Precision', 'Result'])
    y = df['Precision']

    # Ensure all data is numeric
    X = X.apply(pd.to_numeric, errors='coerce')
    y = pd.to_numeric(y, errors='coerce')

    # Drop any rows with NaN values
    X = X.dropna()
    y = y[X.index]

    # Print data types to ensure they are numeric
    print(X.dtypes)
    print(y.dtypes)

    # Add a constant to the independent variables matrix
    X = sm.add_constant(X)

    # Fit the linear model
    model = sm.OLS(y, X).fit()

    # Print summary of the model
    print(model.summary())

    # Check model assumptions
    check_model_assumptions(model)


# Example usage
df_cleaned = sort_data('optimization_results2.csv')
build_and_plot_linear_model(df_cleaned)
