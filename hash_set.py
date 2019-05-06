class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [[]] * self.size

    def add(self, key: int) -> None:
        hash_key = self.hash_function(key)
        if key not in self.buckets[hash_key]:
            self.buckets[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash_function(key)
        if self.contains(key):
            self.buckets[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self.hash_function(key)
        if self.buckets[hash_key] and key in self.buckets[hash_key]:
            return True
        else:
            return False

    def hash_function(self, key: int) -> int:
        return key % self.size
