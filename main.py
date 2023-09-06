"""
Main code
"""
import pandas as pd


def readfile(file_path):
    data = pd.read_csv(file_path)
    summary_stats = data.describe()
    return summary_stats
