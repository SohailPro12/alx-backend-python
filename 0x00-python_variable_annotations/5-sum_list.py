#!/usr/bin/env python3
"""
sum_list function
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the input_list.

    Examples:
        >>> sum_list([1.5, 2.5, 3.5])
        7.5
        >>> sum_list([0.5, 1.5, 2.5, 3.5])
        8.0
    """
    return sum(input_list)
