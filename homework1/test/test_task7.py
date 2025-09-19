import pytest
from src.task7 import reverse2D_array
import numpy as np

@pytest.mark.parametrize("input_array, expected_output", [
    (np.array([[1,2,3],[4,5,6]]), np.array([[6,5,4],[3,2,1]])),
    (np.array([[7,8],[9,10]]), np.array([[10,9],[8,7]])),
    (np.array([[1,3,5,7]]), np.array([[7,5,3,1]]))
])
def test_reverse2D_array(input_array, expected_output):
    assert np.array_equal(reverse2D_array(input_array), expected_output)
