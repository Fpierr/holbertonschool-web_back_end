#!/bin/usr/env python3
"""Run time for four parallel comprehensions"""

import asyncio
from time import perf_counter
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime for four parallel async comprehensions."""
    start_time = perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = perf_counter()
    return end_time - start_time
