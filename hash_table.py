class HashTable(object):
    """ Simple hash table that creates hash values from the first two letters in a string """
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        key = self.calculate_hash_value(string)
        self.table[key] = string

    def lookup(self, string):
        key = self.calculate_hash_value(string)
        if self.table[key]:
            if string in self.table[key]:
                return key
        else:
            return -1

    @staticmethod
    def calculate_hash_value(string):
        key = ord(string[0])*100 + ord(string[1])
        return key
