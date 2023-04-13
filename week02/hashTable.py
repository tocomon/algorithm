class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add_value(self, key, value):
        hash_value = self.hash_function(key)
        for i in range(len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i] = (key, value)
                return
        self.table[hash_value].append((key, value))

    def get_value(self, key):
        hash_value = self.hash_function(key)
        for i in range(len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                return self.table[hash_value][i][1]
        return None

    def remove_value(self, key):
        hash_value = self.hash_function(key)
        for i in range(len(self.table[hash_value])):
            if self.table[hash_value][i][0] == key:
                del self.table[hash_value][i]
                return


hash_table = HashTable(10)

hash_table.insert('apple', 1500)
hash_table.insert('banana', 2000)
hash_table.insert('cherry', 3000)

print(hash_table.search('apple')) # 1500
print(hash_table.search('banana')) # 2000
print(hash_table.search('cherry')) # 3000

hash_table.delete('banana')
print(hash_table.search('banana')) # None
