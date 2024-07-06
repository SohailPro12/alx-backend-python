#!/usr/bin/env python3
"""
safely_get_value function
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
r = Union[Any, T]
d = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Any = None) -> Any:
    """
    Safely retrieves the value associated with the given key
    from the dictionary.
        Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Any, optional): The default value to return
        if the key is not found. Defaults to None.
    Returns:
        Any: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
