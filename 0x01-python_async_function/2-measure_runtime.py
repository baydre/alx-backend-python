#!/usr/bin/env python3
"""
Task_2: measure the runtime.
"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total
    execution time.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    average_time = total_time / n

    return average_time
