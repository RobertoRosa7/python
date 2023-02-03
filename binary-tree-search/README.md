# Binary Tree Search Python

## Why would I use a binary search tree?

[Source of Documentation](https://blog.boot.dev/computer-science/binary-search-tree-in-python/)

Binary Trees are useful for storing data in an organized manner so that it can be quickly
retrieved, inserted, updated and deleted

### Step 1 - BSTNode Class

Out implementation won't use a `Tree` class, but instead just a `Node` class. Binary trees
are really just a pointer to a root that in turn connects to each child node, so we'll run
with that idea.

```python
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
```

We'll allow a value, which will also act as the key, to be provided. If one *isn't* provided
we'll just set it to `None`. We'll also initialize both children of the new node to `None`

### Step 2 Insert Method

<pre><code>  10                                10
 /   \        Insert 5            /    \
 2    60    ---------&gt;           2     60
/  \                            /  \
1   3                           1   3
                                     \
                                      5
</code></pre>

We need a way to insert new data into the tree. Inserting a new node should append it as a
`lead node` in the proper spot.

```python
def insert(self, val):
    if not self.val:
        self.val = val
        return
    if self.val == val:
        return
    if self.val > val:
        if self.left:
            self.left.insert(val)
            return
        self.left = BSTNode(val)
        return
    if self.right:
        self.right.insert(val)
        return
    self.right = BSTNode(val)
```

If the node doesn't yet have a value, we can just set the given value and `return`. If we
every try to insert a value that also exists, we can also simply return as this can be
considered a `no-op`.

### Step 3 Min and Max Values

`getMin` and `getMax` are useful helper functions, and they're easy to write. They are simple
recursive functions that traverse the edges of the tree to find the smaller or largest value.

```python
def get_min(self):
    current = self
    while current.left is not None:
        current = current.left
    return current.val


def get_max(self):
    current = self
    while current.right is not None:
        current = current.right
    return current.val
```

### Step 4 Delete

The delete operation is one of the more complex ones. It is a recursive functions as well,
but it also returns the new state of the given node after performing the delete operation.
This allows parent whose child has been deleted to property set it's `left` or `right` data

```python
def delete(self, val):
    if self is None:
        return self
    if val < self.val:
        self.left = self.left.delete(val)
        return self
    if val > self.val:
        self.right = self.right.delete(val)
        return self
    if self.right is None:
        return self.left
    if self.left is None:
        return self.right
    min_larger_node = self.right
    while min_larger_node.left:
        min_larger_node = min_larger_node.left
    self.val = min_larger_node.val
    self.right = self.right.delete(min_larger_node.val)
    return self
```

### Step 5 - Exists

The exists function is another simple recursive function that returns True or False
depending on whether a given value already exists in the tree.

```python
def exists(self, val):
    if val is self.val:
        return True
    if val < self.val:
        if self.left is None:
            return False
        return self.left.exists(val)
    if self.right is None:
        return False
    return self.right.exists(val)
```

### Step 6 - Inorder

It’s useful to be able to print out the tree in a readable format.
The inorder method print’s the values in the tree in the order of their keys.

```python
def inorder(self, vals):
    if self.left is not None:
        self.left.inorder(vals)
    if self.val is not None:
        vals.append(self.val)
    if self.right is not None:
        self.right.inorder(vals)
    return vals
```

### Step 7 - Preorder

```python
def preorder(self, vals):
    if self.val is not None:
        vals.append(self.val)
    if self.left is not None:
        self.left.preorder(vals)
    if self.right is not None:
        self.right.preorder(vals)
    return vals
```

### Step 8 - Postorder

```python
def postorder(self, vals):
    if self.left is not None:
        self.left.postorder(vals)
    if self.right is not None:
        self.right.postorder(vals)
    if self.val is not None:
        vals.append(self.val)
    return vals
```

### How to use

```python

def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18, 2, 20]
    bst = BSTNode()

    for num in nums:
        bst.insert(num)

    print("Pre Order:")
    print(bst.preorder([]))
    print('#')

    print("Post Order:")
    print(bst.postorder([]))
    print('#')

    print("In Order:")
    print(bst.inorder([]))
    print('#')

    nums = [2, 6, 20]
    print("deleting: " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")

    print('4 exists:')
    print(bst.exists(4))
    print('2 exists:')
    print(bst.exists(2))
    print('12 exists:')
    print(bst.exists(12))
    print('18 exists:')
    print(bst.exists(18))
    print('6 exists:')
    print(bst.exists(6))

    print("min: " + str(bst.get_min()))
    print("max: " + str(bst.get_max()))


if __name__ == "__main__":
    main()
```