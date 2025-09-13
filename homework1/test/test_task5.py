import pytest
from src.task5 import bookList, gptDatabase

# More info on parameterizing https://docs.pytest.org/en/stable/how-to/parametrize.html
@pytest.mark.parametrize("index,expected_book", [
    (0, 'Audie Murphy: To Hell and Back'),
    (1, 'F. Scott Fitzgerald: The Great Gatsby'),
    (2, 'William Shakesphere: MacBeth'),
    (3, 'Authur Miller: The Cruicible'),
    (4, 'Harper Lee: To Kill a Mocking Bird'),
])
def test_bookList(index, expected_book):
    assert bookList[index] == expected_book

# More info on parameterizing https://docs.pytest.org/en/stable/how-to/parametrize.html
@pytest.mark.parametrize("id,expected_name", [
    (101, 'Alice Johnson'),
    (102, 'Brandon Lee'),
    (103, 'Chloe Martinez'),
    (104, 'Daniel Kim'),
    (105, 'Emily Carter'),
])
def test_gptDatabase(id, expected_name):
    assert id in gptDatabase
    assert gptDatabase[id] == expected_name