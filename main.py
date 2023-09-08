"""
Main code
"""
import pandas as pd


# generates summary statistics for the numeric columns in a DataFrame.
def readfile(file_path):
    data = pd.read_csv(file_path)
    summary_stats = data.describe()
    return summary_stats
