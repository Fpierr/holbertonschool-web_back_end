#!/usr/bin/env python3
"""LRU Cache"""

from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRU Cache system that inherits from BaseCaching"""
    
    
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = OrderedDict()
    
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        
        if key in self.order:
            self.order.move_to_end(key)
        
        self.order[key] = item
        self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            """Remove the first item"""
            lru_key, _ = self.order.popitem(last=False)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
    
    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed item to the end
        self.order.move_to_end(key)
        return self.cache_data[key]
