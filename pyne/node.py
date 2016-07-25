from abc import ABCMeta, abstractmethod

class Node:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def contains(self, elem):
        pass
    
    @abstractmethod
    def incl(self, elem):
        pass

class Empty(Node):
    def __init__(self):
        super(Empty, self).__init__(self)

    def contains(self, elem): return False

    def incl(self, elem): return NonEmpty(elem, Empty(), Empty())


class NonEmpty(Node):
    def __init__(self, elem, left, right):
        self.elem = elem
        self.left = left
        self.right = right
        super(NonEmpty, self).__init__(self)

    def contains(self, elem):
        if self.elem is elem: return elem
        else: self.left.contains(elem) or self.right.contains(elem)

    def incl(self, elem):
        if len(elem) < len(self.elem): return NonEmpty(self.elem, self.left.incl(elem), self.right)
        else: return NonEmpty(self.left, self.elem, self.right.incl(elem))
