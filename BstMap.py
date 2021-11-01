from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if key == self.key:
            return
        if key < self.key:
            if self.left:
                self.left.put(key, value)
            else:
                self.left = Node(key, value, None, None)
        if key > self.key:
            if self.right:
                self.right.put(key, value)
            else:
                self.right = Node(key, value, None, None)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        res = ""
        if self.left:
            res += "(" + self.left.key + "," + str(self.left.value) + ")"
        else:
            pass
        res += "(" + self.key + "," + str(self.value) + ")"
        if self.right:
            res += "(" + self.right.key + "," + str(self.right.value) + ")"
        else:
            pass
        self.left.to_string()
        return res

    def count(self):
        if self.left is None and self.right is None:
            return 0
        return 1 + count(self.left) + count(self.right)

    def get(self, key):
        if self.left is None:
            return None
        elif self.left is not None:
            return self.left.get(key)
        elif self.right is None:
            return None
        elif self.right is not None:
            return self.right.get(key)

    def max_depth(self):
        if self.left is None:
            return 0
        elif self.left is not None:
            return self.left.max_depth()
        elif self.right is None:
            return 0
        elif self.right is not None:
            return self.right.max_depth()

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self):
        lst = []
        if self.left:
            lst += self.left + self.left.as_list()
        lst.append(self.key)
        if self.right:
            lst += self.left + self.right.as_list()


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    # def as_list(self):
    #     lst = []
    #     if self.root is None:
    #         return lst
    #     else:
    #         return self.root.as_list(lst)
