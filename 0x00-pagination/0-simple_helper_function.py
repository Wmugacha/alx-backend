#!/usr/bin/env python3
"""
Module of a pagination helper funtion
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the range of indexing"""

    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return (start_index, end_index)
