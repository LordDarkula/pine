"""
Scalable Tree is stored as an N dimensional list

         A [0]
        / \
[1][0] B   C [2][0]
      /
     D [1][1][0]


[A, [B, [D]], [C]]

[nth child of root][mth child of child n][rth child of child m] . . . [0]

Only the first element of each list is a non-list element
The rest of the elements are lists that contain it's children
"""

from copy import copy as cp


class Tree:
    def __init__(self, root):
        self.tree = [root]

    def select(self, index):
        element = self.tree

        for level in index:
            element = self.tree[level]

        return element

    def parent(self, index):
        my_index = cp(index)
        my_index.pop(len(my_index) - 2)
        return self.select(my_index), my_index

    def child(self, child_num, index):
        my_index = cp(index)
        my_index.pop()
        my_index.extend([child_num, 0])
        return self.select(my_index), my_index

    def add_child(self, child=None, index=0):
        if index == 0:
            my_index = [0]
        else:
            my_index = cp(index)
        if my_index[len(my_index) - 1] == 0:
            my_index.pop()

        self.select(my_index).append([child])
        my_index.append(len(self.select(index)) - 1)
        return my_index

    def chain(self, items, index=0):
        my_index = cp(index)
        for item in items:
            my_index = self.add_child(index, item)

        return my_index

    def branch(self, items, index=0):
        indexes = []
        for item in items:
            indexes.append(self.add_child(index, item))

        return indexes
