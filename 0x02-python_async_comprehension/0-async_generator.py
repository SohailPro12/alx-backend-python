#!/usr/bin/env python3
"""
Async Generator
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
