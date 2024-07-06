#!/usr/bin/env python3
"""
zoom_array function
"""

from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given list by
    repeating each element a certain number of times.

    Args:
        lst (Tuple): The input list to zoom in on.
        factor (int, optional): The factor by which to zoom in.
        Defaults to 2.

    Returns:
        List: The zoomed-in list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
