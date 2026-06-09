class LRUCache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)