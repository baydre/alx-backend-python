#!/usr/bin/env python3
"""
Task_2: measure_runtime coroutine that
execute async_comprehension 4-times
parallel asyncio.gather.
"""
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """
    returns the total runtime measurement.
    """
    start_time = asyncio.get_event_loop().time()

    # execute async_comprehension four-times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
