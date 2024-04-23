#!/usr/bin/env python3
"""mplex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Calculates the sum of a list of integers and floats"""
    return sum(mxd_lst)
