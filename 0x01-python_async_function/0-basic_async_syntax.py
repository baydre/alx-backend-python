#!/usr/bin/env python3
"""
Task_0: async basics, coroutine
that takes in an integer argument.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
