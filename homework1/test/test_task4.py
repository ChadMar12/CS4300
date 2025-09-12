import pytest
from src.task4 import calculate_discount

# Pytest parametrize allows us to make multiple test case and test them in one go doc is here https://docs.pytest.org/en/stable/how-to/parametrize.html for future use
@pytest.mark.parametrize('price,discount,total', [
    (100, 0.10, 90.0),       
    (50.25, 0.15, 42.7125),  
    (200, 0.25, 150.0),      
    (99.99, 0, 99.99),       
    (80, 1, 0.0),            
    (123.45, 0.20, 98.76)
])
def test_discount(price, discount, total):
    assert calculate_discount(price, discount) == total
