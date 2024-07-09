#!/usr/bin/env python3
"""
Async Generator
"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Async Generator function
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.random() * 10
