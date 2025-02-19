#!/usr/bin/python3
"""FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache following FIFO policy """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the first key inserted (FIFO order)
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        return self.cache_data.get(key, None)
