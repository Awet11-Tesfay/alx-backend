#!/usr/bin/env python3
""" FIFOCache that inherits form BaseCaching
"""
from base_caching import BaseCaching


class FIFICache(BaseCaching):
    """ Use self.cache_data dictionary from the parent class
    """

    def __init__(slef):
        """ Initializing overload but do not forget call parent class
        """
        super().__init__()

    def put(self, key, item):
        """ Must assign to self.cache_data the item for key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            element = list(self.cache_data.keys())
            del self.cache_data[element[0]]
            print(f'DISCARD: {element[0]}')

    def get(self, key):
        """ Return self.cache_data
        """
        return self.cache_data.get(key)
