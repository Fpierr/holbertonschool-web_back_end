#!/usr/bin/env python3
"""LIFO Cache"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching system"""

    def __init__(self):
        """initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Assign an item to the cache using LIFO policy"""
        if key is None or item is None:
            return
        
        self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key =list(self.cache_data.keys())[-2]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
