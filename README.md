# pyne
Implementation of trees uaing different methods.

## Introduction
I originally created these trees as practice, but they may be useful
to anyone who needs a simple way to create trees in their project.

## Installation
> Not yet on PyPI

Once this becomes a package, I will fill out this section.

## Tree
Scalable Tree is stored as an N dimensional list. 
It is a mutable structure.
```
         A [0]
        / \
[1][0] B   C [2][0]
      /
     D [1][1][0]


[A, [B, [D]], [C]]

[nth child of root][mth child of child n][rth child of child m] . . . [0]
```
Only the first element of each list is a non-list element
The rest of the elements are lists that contain it's children

### Usage
Trees must be initialized with a root, which can be any object
```python
from pyne import Tree

# Creating a tree with a string root
my_tree = Tree("my root")

```

Children can be added to the root using add_child()
```python

#Adds 2 children (child1, child2) to root and stores their 
indexes in index1, index2 respectively.
index1 = my_tree.add_child("child1")
index2 = my_tree.add_child("child2")

```

index1, index2 are the indexes of children1, children2. 
They can be give them children.
```python

#Adds a child to child1 and child2.
index3 = my_tree.add_child("childOfChild1", index=index1)
index4 = my_tree.add_child("childOfChild2", index=index2)

```
> As you can see, to add a child to a particular node, you need that node's index.

Lets say I have a list of objects which I want to chain to childOfChild1.
By chain I mean add the first item in the list as a child of childOfChild1,
and add each successive item in the list as a child of the previous item.
```python

chain_list = [1, 2, 3, 4]

#index5 points to the last node in the chain
index5 = my_tree.chain(chain_list, index=index3)

```

Now lets say we have another list, and I want to add all the items in the 
list as children to childOfChild2
```python

branch_list = [5, 6]

#indexes is a list that contains indexes of all the newly added nodes in branch_list
indexes = my_tree.branch(branch_list, index=index4)

```

After everything we did, my_tree will have the following structure
```
               "my root"
                 /   \
           "child1" "child2"
              /         \
     "childOfChild1"   "childOfChild2"
          /               /      \
         1               5        6
        /
       2
      /
     3
    /
   4

```

