#!/usr/bin/python3
"""LRU Caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU cache system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.order:
            self.order.move_to_end(key)

        self.order[key] = item
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.order.popitem(last=False)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.order.move_to_end(key)
        return self.cache_data[key]
