#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy and returns the result as a list.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The result of matrix multiplication as a list.

    Raises:
        None.
    """
    result = np.matmul(m_a, m_b)
    return result.tolist()
