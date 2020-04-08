
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"<{self.key}, {self.value}>"

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, key):
        pass

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash_mod(key)

        # Check if a pair already exists in the bucket
        pair = self.storage[index]
        if pair is not None:
            # If so, overwrite the key/value and throw a warning
            if pair.key != key:
                print("Warning: Overwriting value")
                pair.key = key
            pair.value = value
        else:
            # If not, create a new LinkedPair and place it in the bucket
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        index = self._hash_mod(key)

        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, remove that pair
            self.storage[index] = None
        else:
            # Else print warning
            print("Warning: Key does not exist")

    def retrieve(self, key):
        # Get the index from hashmod
        index = self._hash_mod(key)

        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, return the value
            return self.storage[index].value
        else:
            # Else return None
            return None

    def resize(self):
        pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")

    print(ht.storage)
    
    print("")

    #Test storing beyond capacity
    print(ht.retrieve("line_1"))