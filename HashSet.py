from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0
    N: int = 8

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hashed = 0
        for i in range(len(word)):
            hashed += ord(word[i])
        hashed %= self.N
        return hashed

    # Doubles size of bucket list
    def rehash(self):
        buckets = self.buckets
        self.N = self.N * 2
        self.buckets = []
        self.buckets = [[] for i in range(self.N)]
        for bucket in buckets:
            for word in bucket:
                self.add(word)

    # Adds a word to set if not already added
    def add(self, word):
        hashed = self.get_hash(word)
        i = hashed
        while self.buckets[i] != [] and word not in self.buckets[i]:
            if i == self.N - 1:
                i = 0
            else:
                i += 1
            # if word in self.buckets[i]:
            #     break

        if self.buckets[i] == []:
            self.buckets[i].append(word)
            self.size += 1
        else:
            pass
        
        if self.size == self.N:
            self.size = 0
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        string = '{ '
        for bucket in self.buckets:
            if bucket != []:
                for i in bucket:
                    string += str(i) + ' '
        string += '}'
        return string

    # Returns current number of elements in set
    def get_size(self):
        n = 0
        for bucket in self.buckets:
            if bucket != []:
                n += 1
        return n

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hashed = self.get_hash(word)
        if word not in self.buckets[hashed]:
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        size = len(self.buckets)
        return size

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hashed = self.get_hash(word)
        if word not in self.buckets[hashed]:
            self.buckets[hashed] = []
            self.size -= 1
        else:
            pass

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        n = 0
        for bucket in self.buckets:
            if len(bucket) > n:
                n = len(bucket)
        return n
