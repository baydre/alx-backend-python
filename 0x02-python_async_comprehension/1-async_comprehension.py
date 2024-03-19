#!/usr/bin/env python3
"""
Task_1: async_comprehension coroutine
that collects random numbers.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    returns 10 random numbers using
    async comprehensing over async_generator
    """
    return [_ async for _ in async_generator()]
