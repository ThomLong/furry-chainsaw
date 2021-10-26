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
            word = bucket[0]
            v = bucket[1]
            self.add(word)
            i = self.search(word)
            if self.buckets[i][1] != v:
                self.buckets[i][1] = v

    # Adds a word to set if not already added
    def add(self, word):
        i = self.get_hash(word)
        while self.buckets[i] != [] and word not in self.buckets[i]:
            if i == self.N - 1:
                i = 0
            else:
                i += 1
        bucket = self.buckets[i]
        if bucket == []:
            bucket.append(word)
            bucket.append(1)
            self.size += 1
        else:
            bucket[1] += 1

        if self.size == self.N:
            self.size = 0
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        string = '{ '
        for bucket in self.buckets:
            if bucket != []:
                string += bucket[0] + ' '
        string += '}'
        return string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        i = self.search(word)
        if i is False:
            return False
        else:
            return True

    # Returns current size of bucket list
    def bucket_list_size(self):
        size = len(self.buckets)
        return size

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        i = self.search(word)
        if i is False:
            pass
        else:
            self.buckets[i] = []
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        n = 0
        for bucket in self.buckets:
            if bucket != []:
                if bucket[1] > n:
                    n = bucket[1]
        return n

    def search(self, word):
        i = self.get_hash(word)
        while word not in self.buckets[i] and self.buckets[i] != []:
            if i == self.N - 1:
                i = 0
            else:
                i += 1

        if self.buckets[i] == []:
            return False
        else:
            return i
