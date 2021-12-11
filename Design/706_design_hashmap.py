class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map.get(key) != None:
            return self.map[key]
        return -1

    def remove(self, key: int) -> None:
        if self.map.get(key) != None:
            del self.map[key]
