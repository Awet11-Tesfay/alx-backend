#!/usr/bin/env python3
""" FIFOCache hat inherits form BaseCaching
"""
from base_caching import BaseCaching


class FIFICache(BaseCaching):
    """ Use self.cache_data dictionary from the parent class
        your can overload def __init__(self)
        but don't forget to call the parent init
    """

    def __init__(slef):
        """ Initializing class
        """
        super().__init__()

    def put(self, key, item):
        """ Must assign to self.cache_data the item for key
            if key or item is none not do nothing
            if the number of items in self.cache_data is higher
            that BaseCaching.MAX_ITEMS
            you must discard the first item
            you must print DISCARD with key
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
        if key is not None and key in self.cache_data:
            return self.cache_data.get[key]
        return None
