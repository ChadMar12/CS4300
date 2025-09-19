'''
Use pip package manager to add a Python package of your choice to your project (e.g., requests,
numpy, matplotlib). Create a new file named task7.py and write a Python script that demonstrates
how to use the chosen package to perform a specific task or function. Implement pytest test cases
to verify the correctness of your code when using the package.
'''
import numpy as np 

# Example from How to Reverse an array at the website below 
# https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-reverse-an-array
def reverse2D_array(test_arr):

    arr_2d = np.flip(test_arr)

    return arr_2d