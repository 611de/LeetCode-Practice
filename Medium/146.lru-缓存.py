#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.cache_map = {}
        self.order_cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.order_cache:
            return -1
        self.move_head(key)
        return self.cache_map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.order_cache:
            self.cache_map[key] = value
            self.move_head(key)
            return
        self.cache_map[key] = value
        self.order_cache.insert(0, key)
        if len(self.order_cache)>self.capacity:
            self.remove(self.order_cache[-1])
    
    def remove(self, key):
        self.order_cache.remove(key)
        self.cache_map.pop(key)
    
    def move_head(self, key):
        self.order_cache.remove(key)
        self.order_cache.insert(0, key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

