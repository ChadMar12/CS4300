from src.task3 import isPos, primeNumbers, sumOfNums

def test_pos_number():
    pos_num = 5
    assert isPos(pos_num) == True

def test_isPrime():
    assert primeNumbers() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum():
    assert sumOfNums() == 5050