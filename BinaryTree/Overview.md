# Binary Tree in Python
---
![My Screenshot](https://github.com/Prabhat-Chaubey/Compy_Coding/blob/main/Untitled-2024ss-10-07-1413.png)
---
## DFS - (Depth First Search)
- Preorder
- Inorder
- PostOrder
![DFS Tree](https://github.com/Prabhat-Chaubey/Compy_Coding/blob/main/Untitled-2024aa-10-07-1413.png)
### Preorder
- Process the `Node` , then process the `left` the process the `Right`
- [1,2,4,5,3,10]

### Inorder
- Process the `left` , then process the `Node` the process the `Right`
- [4,2,5,1,10,3]

### Postorder
- Process the `Left` , then process the `Right` the process the `Node`
- [4,5,2,10,3,1]


## BFS - (Breadth First Search)
 - We travel the breadth wise
 - [1,2,3,4,5,10]
---
#### We use Stack for DFS
#### We use Queue for BFS
---
## Binary Search Tree
- The Binary Search tree is a tree when all the left side is smaller than the node and right side is greater than the node.

---
## Table of Contents
- [BasicTree](#basictree)
- [Preorder Traversal](#Preorder-Traversal)
- [Inorder Traversal](#Inorder-Traversal)
- [Postorder Traversal](#Postorder-Traversal)
- [BFS](#bfs)
---
## BasicTree
   ```python
 class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Simple tree structure:
#         1
#        / \
#       2   3
#      / \
#     4   5

   ```

## Preorder Traversal
- Visit the root node first, then the left subtree, then the right subtree.
- 🔍 Used for copying trees, expression tree prefix notation, etc.
 ```python
def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

 ```

## Inorder Traversal
 - Visit the left subtree first, then the root, then the right subtree.
 - 🔍 In binary search trees (BST), this returns values in sorted order.
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)
```

## Postorder Traversal
 - Visit the left and right subtrees first, then the root.
 - 🔍 Useful for deleting a tree, evaluating expression trees (postfix).
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')
```
## BFS
- BFS explores all nodes level by level, from top to bottom, left to right.
```python
def bfs_traversal(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        print(current.value, end=' ')

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

```
