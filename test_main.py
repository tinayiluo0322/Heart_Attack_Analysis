"""
Test goes here

"""
from main import readfile


def test_readfile():
    file_path = "/Users/tinayiluo/Desktop/emails.csv"
    result = readfile(file_path)
    print(result)


if __name__ == "__main__":
    test_readfile()
