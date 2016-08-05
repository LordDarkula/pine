# pyne
Implementation of trees uaing different methods.

## Introduction
I originally created these trees as practice, but they may be useful
to anyone who needs a simple way to create trees in their project.

## Installation
> Not yet on PyPI

Once this becomes a package, I will fill out this section.

##Tree
Scalable Tree is stored as an N dimensional list
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
