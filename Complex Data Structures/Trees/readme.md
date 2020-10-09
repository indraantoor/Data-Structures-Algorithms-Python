# Trees
Trees are an essential data structure for storing hierarchical data with a directed flow.

Similar to linked lists and graphs, trees are composed of nodes which hold data.

Nodes also store references to zero or more other tree nodes. Data moves down from node to node.

Trees are often displayed with a single node at the top and connected nodes branching downwards.

## Varietals
Trees come in various shapes and sizes depending on the dataset modeled.

Some are **wide**, with parent nodes referencing many child nodes.

Some are **deep**, with many parent-child relationships.

Trees can be **both wide** and **deep**, but each node will only ever have at most one parent; otherwise, they wouldn’t be trees.

Each time we move from a parent to a child, we’re moving down a level. 

Depending on the orientation we refer to this as the **depth** (counting levels down from the root node) or **height** (counting levels up from a leaf node).

## Binary Search Tree
A **binary tree** is a type of tree where each parent can have **no more than two children**, known as the _left child_ and _right child_.

Further constraints make a binary search tree:

- Left child values must be lesser than their parent.
- Right child values must be greater than their parent.

The constraints of a binary search tree allow us to search the tree efficiently.
At each node, we can discard half of the remaining possible values.

## Keywords You Should Know
1. **Root**: A node which has no parent. One per tree.
2. **Parent**: A node which references other nodes.
3. **Child**: Nodes referenced by other nodes.
4. **Sibling**: Nodes which have the same parent.
5. **Leaf**: Nodes which have no children.
6. **Level**: The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.