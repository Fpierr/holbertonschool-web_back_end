#!/usr/bin/env python3
"""Filtered logger"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """filter obfuscate data in a log message"""
    for field in fields:
        message = re.sub(field + r"=[^" + separator + r"]*",
                         field + "=" + redaction, message)
    return message
