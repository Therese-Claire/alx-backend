#!/usr/bin/env python3
"""Task 0 Module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """calculates the start index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters.
    Args:
        page(int): page number
        page_size(int): size of single page
    Return:
        tuple: a tuple of start and end index
    """
    start_index = (page - 1) * page_size
    return (start_index, start_index + page_size)
