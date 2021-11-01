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
        self.size = 0
        self.buckets = [[] for i in range(self.N)]
        for bucket in buckets:
            if bucket != []:
                for entry in bucket:
                    i = self.get_hash(entry[0])
                    self.buckets[i].append(entry)
                    self.size += 1

    # Adds a word to set if not already added
    def add(self, word):
        i = self.get_hash(word)
        bucket = self.buckets[i]
        check = False
        if bucket != []:
            for entry in bucket:
                if entry[0] == word:
                    entry[1] += 1
                    check = False
                    break
                else:
                    check = True
            if check is True:
                bucket.append([word, 1])
                self.size += 1
        else:
            bucket.append([word, 1])
            self.size += 1

        if self.size == self.N:
            self.size = 0
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        string = '{ '
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    string += entry[0] + ' '

        string += '}'
        return string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        i = self.get_hash(word)
        for entry in self.buckets[i]:
            if entry[0] == word:
                result = True
                break
            else:
                result = False
        return result

    # Returns current size of bucket list
    def bucket_list_size(self):
        size = len(self.buckets)
        return size

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        i = self.get_hash(word)
        bucket = self.buckets[i]
        for entry in bucket:
            if entry[0] == word:
                bucket.remove(entry)
                self.size -= 1
                break

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        n = 0
        for bucket in self.buckets:
            if bucket != []:
                if len(bucket) > n:
                    n = len(bucket)
        return n
