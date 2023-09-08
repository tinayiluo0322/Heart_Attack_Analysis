"""
Test goes here

"""
from main import readfile


# test cases
def test_readfile():
    file_path = "emails.csv"
    result = readfile(file_path)
    # mean value of first column in emails.csv
    mean_first_column = result.iloc[:, 0]["mean"]
    assert mean_first_column == 6.640564578499613
    # min value of first column in emails.csv
    min_first_column = result.iloc[:, 0]["min"]
    assert min_first_column == 0.0
    # max value of first column in emails.csv
    max_first_column = result.iloc[:, 0]["max"]
    assert max_first_column == 210.0


if __name__ == "__main__":
    test_readfile()
