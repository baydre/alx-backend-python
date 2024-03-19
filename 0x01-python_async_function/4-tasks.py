#!usr/bin/env python3
"""
Task_4: alter "wait_n" into "task_wait_n"
and call task_wait_random.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns list of all delayed tasks.
    """
    delays = []

    tasks = [task_wait_random(max_delay)for _ in range(n)]
    results = await asyncio.gather(*tasks)

    delays = sorted(results)

    return delays
