from pyne.binary_tree import Binary
from pyne.tree import Tree

my_tree = Tree(0)
my_tree.add_child(1)
sec = my_tree.add_child(child=2)
my_tree.add_child(child=3, index=sec)

print(my_tree.select())