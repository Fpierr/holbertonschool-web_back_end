#!/usr/bin/python3
"""MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU cache system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.order:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

        if key not in self.order:
            self.order.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """Move element to the last index"""
        length = len(self.order)
        if self.order[length - 1] != item:
            self.order.remove(item)
            self.order.append(item)
