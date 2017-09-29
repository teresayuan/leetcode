# LeetCode - LRU Cache
#
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.cache_dict:
            return -1
        else:
            value = self.cache_dict.pop(key)
            # re-add most recently used element to end of ordered dict
            self.cache_dict[key] = value

        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.cache_dict:
            self.cache_dict.pop(key)
        elif self.capacity == len(self.cache_dict):
            # oldest is at front of ordered dic
            self.cache_dict.popitem(last=False)

        self.cache_dict[key] = value

        return


if __name__ == '__main__':
    # 1, -1, -1, 3, 4
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print cache.get(1)
    # cache.put(3, 3)
    # print cache.get(2)
    # cache.put(4, 4)
    # print cache.get(1)
    # print cache.get(3)
    # print cache.get(4)

    # -1, -1, 2, 6
    cache = LRUCache(2)
    print cache.get(2)
    cache.put(2, 6)
    print cache.get(1)
    cache.put(1, 5)
    cache.put(1, 2)
    print cache.get(1)
    print cache.get(2)