#!/usr/bin/env python3
""" write a function named index_range and takes two arguments """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Return a tuple """
    return ((page * page_size) - page_size, page_size * page)
