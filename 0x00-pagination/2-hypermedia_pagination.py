#!/usr/bin/env python3
"""
Pagination module
"""
from typing import Tuple, List, Dict, Optional
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the range of indexing"""

    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function to return the appropriate page of the dataset"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        if self.dataset() is None:
            return []

        indexRange = index_range(page, page_size)

        return self.dataset()[indexRange[0]:indexRange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Pagination data"""

        data = self.get_page(page, page_size)

        dataSet = self.__dataset

        length = len(dataSet) if data else 0

        total_pages = math.ceil(length / page_size) if dataSet else 0

        page_size = len(data) if data else 0

        prev_page = page - 1 if page > 1 else None

        next_page = page + 1 if page < total_pages else None

        hyperMedia = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
        }

        return hyperMedia
