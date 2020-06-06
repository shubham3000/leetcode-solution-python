class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

    def get(self, key: int) -> int:
        v = self.cache.get(key,-1)
        if not v is -1:
            self.cache.pop(key)
            self.cache[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            self.cache.pop(next(iter(self.cache)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)