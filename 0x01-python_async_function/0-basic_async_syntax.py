#!/usr/bin/env python3
"""
The basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random amount of time.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay that was used.

    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
