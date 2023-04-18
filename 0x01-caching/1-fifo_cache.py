#!/usr/bin/env python3
""" Fifo caching in python
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseicCache that inherits from BaseCaching """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            keys_list = list(self.cache_data.keys())
            del self.cache_data[keys_list[0]]
            print(f'DISCARD: {keys_list[0]}')

    def get(self, key):
        """ return  the value in self.cache_data """
        return self.cache_data.get(key)
