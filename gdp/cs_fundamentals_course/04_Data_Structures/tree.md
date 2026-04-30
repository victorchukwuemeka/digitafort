# Trees — Basics Course

---

## Lesson 1 — What Is a Tree?

A tree is a **hierarchical data structure** made up of nodes connected by edges. Unlike the trees outside, computer trees grow downward — the root is at the top and the leaves are at the bottom.

Every node in a tree holds a value and may point to one or more **child nodes**. Except for the root, every node has exactly one **parent**.

```
        10        ← root (no parent)
       /  \
      5    15     ← children of 10
     / \     \
    3   7     20  ← leaves (no children)
```

> Trees are everywhere in computing: your file system is a tree, a website's HTML is a tree, and every time you make a decision in code (`if/else`), you're thinking in a tree-like structure.

---

## Lesson 2 — Key Terminology

| Term      | Meaning                                              |
|-----------|------------------------------------------------------|
| Root      | The top node — has no parent                         |
| Parent    | A node that has at least one child                   |
| Child     | A node that descends from a parent                   |
| Leaf      | A node with no children                              |
| Edge      | The connection between a parent and a child          |
| Depth     | Distance from the root (root itself has depth 0)     |
| Height    | Longest path from a node down to a leaf              |
| Subtree   | A node and all of its descendants                    |

### Applied to the example above

```
        10          depth 0  (root)
       /  \
      5    15       depth 1
     / \     \
    3   7     20    depth 2  (leaves)
```

- **Root:** `10`
- **Leaves:** `3`, `7`, `20`
- **Parent of 7:** `5`
- **Children of 10:** `5` and `15`
- **Height of the tree:** 2

---

## Lesson 3 — Binary Search Tree (BST)

A **Binary Search Tree** is the most important and commonly used type of tree. Two rules define it:

1. Every node has **at most two children** (left and right)
2. For any node:
   - all values in its **left** subtree are **smaller**
   - all values in its **right** subtree are **larger**

```
        10
       /  \
      5    15
     / \     \
    3   7     20
```

Check the rule at node `10`: everything to the left (`5, 3, 7`) is less than 10. Everything to the right (`15, 20`) is greater than 10. 

Check at node `5`: left is `3` (less than 5), right is `7` (greater than 5). 

### Why this rule is powerful

Because values are arranged in order, you can **eliminate half the tree at each step** when searching — just like binary search on a sorted list.

```
Search for 7 in the tree above:

Start at 10 → 7 < 10, go left
Arrive at 5  → 7 > 5,  go right
Arrive at 7  → found! 

Only 3 steps, not 6.
```

---

## Lesson 4 — Core BST Operations

### Search — O(log n) average

```python
def search(node, target):
    if node is None:
        return False          # not found
    if target == node.value:
        return True           # found
    elif target < node.value:
        return search(node.left, target)   # go left
    else:
        return search(node.right, target)  # go right
```

### Insert — O(log n) average

New values always land at a leaf. You walk down the tree following the BST rule until you find an empty spot.

```python
def insert(node, value):
    if node is None:
        return Node(value)           # empty spot found
    if value < node.value:
        node.left  = insert(node.left,  value)
    elif value > node.value:
        node.right = insert(node.right, value)
    return node
```

```
Insert 6 into the tree:

Start at 10 → 6 < 10, go left
Arrive at 5  → 6 > 5,  go right
Arrive at 7  → 6 < 7,  go left
Empty spot   → place 6 here 

        10
       /  \
      5    15
     / \     \
    3   7     20
       /
      6   ← newly inserted
```

### Time complexity summary

| Operation | Average  | Worst case (unbalanced) |
|-----------|----------|--------------------------|
| Search    | O(log n) | O(n)                     |
| Insert    | O(log n) | O(n)                     |
| Delete    | O(log n) | O(n)                     |

> The worst case happens when values are inserted in sorted order (e.g. 1, 2, 3, 4…), making the tree a straight line. Balanced trees like AVL or Red-Black trees fix this — but that's an advanced topic.

---

## Lesson 5 — When to Use a Tree

Use a tree when:

- You need to represent a **hierarchy** — file systems, org charts, folder structures
- You need **fast search, insert, and delete** on sorted data (BST)
- You're building features like **autocomplete** or **spell-check** (Trie, a type of tree)
- You need to evaluate **expressions** like `(3 + 5) * 2` (expression tree)
- You're implementing a **priority queue** (heap, a type of tree)

Don't reach for a tree when:

- Your data is flat with no hierarchy — a list or hash table is simpler
- You just need fast key-based lookup — a hash table is O(1), a BST is O(log n)
- Insertion order matters more than sorted order — use a list or queue

---

## Quick Reference

```
BST Rules
─────────────────────────────────────
Left child  < parent  < right child
─────────────────────────────────────

Vocabulary
  root    → top node, no parent
  leaf    → bottom node, no children
  depth   → steps from root (root = 0)
  height  → steps from node to deepest leaf

Operations (balanced BST)
  search  → O(log n)
  insert  → O(log n)
  delete  → O(log n)
```

---

## Quiz — Test Yourself

**Q1.** In a Binary Search Tree, where do smaller values go?

- A) To the right of the parent
- B) To the left of the parent
- C) It doesn't matter

>  **B** — Smaller values always go to the left subtree. Larger values go to the right.

---

**Q2.** What is a leaf node?

- A) The root of the tree
- B) A node with exactly two children
- C) A node with no children

> **C** — A leaf is any node that has no children. It's the "bottom" of that branch.

---

**Q3.** You insert the values `5, 3, 7, 1` into an empty BST in that order. What is the root?

- A) 1
- B) 3
- C) 5

>  **C** — The first value inserted becomes the root. All subsequent values are placed relative to it.

---

**Q4.** What is the depth of the root node?

- A) 1
- B) 0
- C) Depends on the tree size

>  **B** — The root always has depth 0. Its children have depth 1, their children depth 2, and so on.

---

**Q5.** Why can searching a BST be faster than scanning a plain list?

- A) BSTs use hashing under the hood
- B) Each comparison eliminates an entire half of the remaining tree
- C) BSTs store items in random order

> **B** — Because of the left/right ordering rule, each step cuts the remaining search space in half — giving O(log n) instead of O(n).

---

*End of course. You now understand what trees are, how Binary Search Trees are structured and searched, and when to reach for them.*