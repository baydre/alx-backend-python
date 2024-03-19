#!/usr/bin/env python3
"""
Task_0: async_generator coroutine
that takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times asynchronously, wait 1 seconds
    and then yields a random number between 0 - 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
