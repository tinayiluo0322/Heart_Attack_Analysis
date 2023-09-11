"""
Test goes here

"""
from main import readfile, summary, median


# test cases
def test_readfile():
    file_path = "heart.csv"
    summary_result = summary(file_path)
    # mean value of the fourth column resting blood pressure
    mean_4_column = summary_result.iloc[:, 3]["mean"]
    # print(mean_4_column)
    assert mean_4_column == 131.62376237623764
    # standard deviation value of fourth column resting blood pressure
    std_4_column = summary_result.iloc[:, 3]["std"]
    # print(std_4_column)
    assert std_4_column == 17.5381428135171


def test_median():
    file_path = "heart.csv"
    median_result = median(file_path)
    # Calculate the median for the fourth column resting blood pressure
    median_4_column = median_result["trtbps"]
    # print(median_4_column)
    assert median_4_column == 130.0


if __name__ == "__main__":
    test_readfile()
    test_median()
