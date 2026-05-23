class LRUCache:

    def __init__(self, capacity: int):
        # OrderedDict() maintain the insertion order
        # recent used item is at the end
        # least recent used item is at the front
        self.cache = OrderedDict()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # when you get a key, you move to end(recent used)
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        # similarly, put exist key to the end
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


        
