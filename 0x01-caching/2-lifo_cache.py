#!/usr/bin/env python3
""" LIFO Caching in python
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Creates a class LIFOCache that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the parent class
        """
        super().__init__()

    def put(self, key, item):
        """ Muat assign to dictionary
        """
        if not key or not item:
            return

        new_element = True if key in self.cache_data.keys() else False

        self.cache_data[key] = item

        if new_element:
            self.updated_key = key
            return

        element = list(self.cache_data.keys())

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            try:
                del self.cache_data[self.updated_key]
                print(f'DISCARD: {self.updated_key}')
            except Exception:
                del self.cache_data[element[-2]]
                print(f'DISCARD: {element[-2]}')

    def get(self, key):
        """ Return the value in self.cache_data
        """
        return self.cache_data.get(key)
