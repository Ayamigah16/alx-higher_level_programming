#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list of lists, 
    containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with each element divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists or contains
    elements other than integers or floats.
        TypeError: If the rows of the matrix have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
