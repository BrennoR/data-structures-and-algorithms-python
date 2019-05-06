class Node:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash_function(key)
        curr = self.buckets[hash_key]
        if not curr:
            self.buckets[hash_key] = Node(key, value)
            return

        while True:
            if curr.pair[0] == key:
                curr.pair = (key, value)
                return
            if not curr.next:
                break
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        hash_key = self.hash_function(key)
        curr = self.buckets[hash_key]
        while curr is not None:
            if curr.pair[0] == key:
                return curr.pair[1]
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash_function(key)
        curr = self.buckets[hash_key]
        prev = None
        while curr is not None:
            if curr.pair[0] == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.buckets[hash_key] = curr.next
                return
            else:
                curr, prev = curr.next, curr

    def hash_function(self, key: int) -> int:
        return key % self.size
