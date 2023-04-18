#!/usr/bin/env python3
""" Caching in python
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseicCache that inherits from BaseCaching """

    def put(self, key, item):
        """ Assign to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
