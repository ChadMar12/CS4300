from src.task2 import intTest, floatTest, stringTest, boolTest

def testing_int():
    assert intTest() == 5

def test_float():
    assert floatTest() == 35.28

def test_string():
    assert stringTest() == 'Today is a good day.'

def test_bool():
    assert boolTest() == True