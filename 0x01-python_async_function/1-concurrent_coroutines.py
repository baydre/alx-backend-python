#!/usr/bin/env python3
"""
Task_1: multiple coroutines at
the same time with async.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns list of all delays (float values).
    """
    delays = []

    tasks = [wait_random(max_delay)for _ in range(n)]
    results = await asyncio.gather(*tasks)

    delays = sorted(results)

    return delays
