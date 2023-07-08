#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The result of matrix multiplication.

    Raises:
        TypeError: If m_a is not a list or contains elements other than lists.
        TypeError: If m_b is not a list or contains elements other than lists.
        TypeError: If m_a contains elements other than integers or floats.
        TypeError: If m_b contains elements other than integers or floats.
        ValueError: If m_a is empty or contains empty rows.
        ValueError: If m_b is empty or contains empty rows.
        ValueError: If the number of columns in m_a is not equal to the number of rows in m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)
    return result
