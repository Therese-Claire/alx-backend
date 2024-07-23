#!/usr/bin/env python3
"""defines functions and class for handling pagination of a csv file"""
import csv
import math
from typing import List, Tuple, Dict, Union


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """innitializes a Server object"""
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
        """Use index_range to find the correct indexes to paginate the
        dataset correctly and return the appropriate page of the dataset
        (i.e. the correct list of rows)
        Args:
            page(int): page number
            page_size(int): size of a page
        Returns: list of paginated rows
        """
        assert ((type(page) is int) and (type(page_size) is int))
        assert (page > 0 and page_size > 0)

        start, stop = index_range(page, page_size)
        return self.dataset()[start:stop]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """provides details about the pagination
        Args:
            page(int): page number
            page_size(int): size of a page
        Returns: Divt containing the details
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
