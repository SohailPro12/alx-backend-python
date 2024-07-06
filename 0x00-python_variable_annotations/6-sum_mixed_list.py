#!/usr/bin/env python3
"""
sum_mixed_list function
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of floats and integers.

    Args:
        mxd_lst (List[Union[int, float]]): A list of floats and integers.

    Returns:
        float: The sum of the mxd_lst.

    Examples:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        678.13
        >>> sum_mixed_list([0.5, 1.5, 2.5, 3.5])
        8.0
    """
    return sum(mxd_lst)
