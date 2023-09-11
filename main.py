"""
Main code
"""
import pandas as pd
import matplotlib.pyplot as plt


# read the Dataframe heart.csv.
def readfile(a):
    df = pd.read_csv(a)
    return df


# generates summary statistics for the numeric columns in the DataFrame heart.csv.
def summary(a):
    df = readfile(a)
    summary_stats = df.describe()
    return summary_stats


# Calculate the median value for each column in heart.csv
def median(a):
    df = readfile(a)
    median_values = df.median()
    return median_values


# Generate histogram for each column in heart.csv
def histogram(a):
    df = readfile(a)
    columns = df.columns

    for column in columns:
        plt.figure(figsize=(8, 4))  # Create a new figure for each column
        plt.hist(df[column])
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {column}")
        plt.grid(True)
        plt.show()  # Display the histogram for the current column


# Generate scatter plot for the 4th column(resting blood pressure) and the 1st column (age) in heart.csv
def scatter_age_blood_pressure(a):
    df = readfile(a)
    x = df.iloc[:, 0]  # 1st column (age)
    y = df.iloc[:, 3]  # 4th column (resting blood pressure)
    plt.scatter(x, y, alpha=0.5, label="Data Points")
    plt.xlabel("Age")
    plt.ylabel("Resting Blood Pressure (mm Hg)")
    plt.title("Scatter Plot: Age vs. Resting Blood Pressure")
    plt.grid(True)
    # plt.legend()
    plt.show()


# if __name__ == "__main__":
# readfile("heart.csv")
# summary("heart.csv")
# histogram("heart.csv")
# scatter_age_blood_pressure("heart.csv")
