"""
Test goes here

"""
from main import readfile


def test_readfile():
    file_path = "/Users/tinayiluo/Desktop/Duke_23_Fall/Data_Engineering/emails.csv"
    result = readfile(file_path)
    print(result)


if __name__ == "__main__":
    test_readfile()
