#!/usr/bin/env python3
"""LRU Cache"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU Caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assign an item to the cache using LRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Met à jour l'ordre d'utilisation
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item  # Ajoute l'élément

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_used_key, _ = self.cache_data.popitem(
                last=False)  # Supprime le moins récemment utilisé
            print(f"DISCARD: {least_used_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Marque l'élément comme récemment utilisé
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
