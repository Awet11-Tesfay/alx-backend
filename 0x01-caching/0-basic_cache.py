#!/usr/bin/env python3
""" Caching
"""

from base import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching class
    """

    def put(self, key, item):
        """ Assign to dictionary value of the key
          - if key or item is None
          - the method should not be do anything
        """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data
        """
        return self.cache_data.get(key)
