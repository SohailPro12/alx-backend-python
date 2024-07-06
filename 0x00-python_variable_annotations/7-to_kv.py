#!/usr/bin/env python3
"""
to_kv function
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and a number `v` and returns a tuple with `k` as the first element and the square of `v` as the second element.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number value.

    Returns:
        Tuple[str, float]: A tuple with `k` as the first element and the square of `v` as the second element.
    """
    return (k, v**2)
