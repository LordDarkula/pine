
left = 1
right = 2

class Binary:
    def __init__(self, root):
        self.tree = [root]
        self.index = [0]

    def current(self):
        element = self.tree

        for level in self.index:
            element = self.tree[level]

        self.index.pop()
        return element

    def parent(self):
        child_num = self.index[len(self.index) - 2]
        self.index.pop()
        parent = self.current()
        self.index.append(child_num)
        return parent

    def add_child(self, child, direction):
        if not direction == 1 and not direction == 2:
            raise TypeError
        
        self.index.pop()
        if direction == 2:
            self.current().append(None)

        self.current().append([child])
        self.index.append(direction)
        self.index.append(0)


