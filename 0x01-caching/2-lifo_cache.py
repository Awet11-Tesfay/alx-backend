#!/usr/bin/env python3
""" LIFO Caching in python
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Creates a class LIFOCache that inherits from BaseCaching
    """

    def __init__(self):
        super.__init__()

    def put(self, key, item):
        """ Muat assign to dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            element = list(self.cache_data.keys())
            del self.cache_data[element[0]]
            print(f'DISCARD: {element[0]}')

    def get(self, key):
        """ Return the value in self.cache_data
        """
        return self.cache_data.get(key)
