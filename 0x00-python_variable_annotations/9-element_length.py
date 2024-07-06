#!/usr/bin/env python3
"""
element_length function
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given list.

    Args:
        lst: A list of sequences.

    Returns:
        A list of tuples, where each tuple contains
        a sequence from the input list
        and its corresponding length.

    Example:
        >>> element_length(['apple', 'banana', 'cherry'])
        [('apple', 5), ('banana', 6), ('cherry', 6)]
    """
    return [(i, len(i)) for i in lst]
