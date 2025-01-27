import random

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.p = 10**9 + 7
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
    def _hash(self, key):
        if not isinstance(key, int):
            key = self._string_to_int(key)
        return ((self.a * key + self.b) % self.p) % self.size

    def _string_to_int(self, key):
        hash_val = 0
        p = 31
        m = self.p
        for char in key:
            hash_val = (hash_val * p + ord(char)) % m
        return hash_val

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
if __name__ == "__main__":
    ht = HashTable(size=7)
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    ht.insert(15, 25)
    ht.insert("grape", 50)

    print("Hash Table after insertions:")
    ht.display()

    print("\nSearch for 'apple':", ht.search("apple"))
    print("Search for 'banana':", ht.search("banana"))
    print("Search for 'orange':", ht.search("orange"))

    print("\nDeleting 'banana':", ht.delete("banana"))
    print("Deleting 'orange':", ht.delete("orange"))

    print("\nHash Table after deletions:")
    ht.display()
