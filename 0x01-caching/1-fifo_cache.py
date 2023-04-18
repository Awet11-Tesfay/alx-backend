#!/usr/bin/env python3
""" Fifo caching in python """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ BaseicCache that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the from the parent class"""
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            element = list(self.cache_data.keys())
            del self.cache_data[element[0]]
            print(f'DISCARD: {element[0]}')

    def get(self, key):
        """ return  the value in self.cache_data """
        return self.cache_data.get(key)
