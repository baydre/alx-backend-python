#!/usr/bin/env python3
"""
"""
import asyncio
from typing import List


async def wait_random(max_delay: int) -> float:
    await asyncio.sleep(max_delay)
    return max_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []

    tasks = [wait_random(max_delay)for _ in range(n)]
    results = await asyncio.gather(*tasks)

    delays = sorted(results)

    return delays


async def main():
    n = 5
    max_delay = 3
    delays = await wait_n(n, max_delay)
    print(f"Delays: {delays}")

if __name__ == "__main__":
    asyncio.run(main())
