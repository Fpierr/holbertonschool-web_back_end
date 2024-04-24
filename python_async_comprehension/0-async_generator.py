#!/usr/bin/env python3
"""Async Generator"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that generate 10 random number enter 0 to 10."""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
