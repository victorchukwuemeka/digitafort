# Selection Sort Lesson

## What is Selection Sort?

Selection Sort is like organizing a hand of cards. You look through all your cards, pick the smallest one, and put it first. Then you look through the rest, pick the next smallest, and put it second. You repeat this until everything is in order.

Selection Sort is **simple** but **slow** for big lists. It's great for learning how sorting works.

## How it Works (The Simple Version)

1. Look at the whole list, find the smallest item
2. Swap it with the first item
3. Now the first item is sorted — ignore it
4. Look at the remaining items, find the smallest
5. Swap it with the second item
6. Keep doing this until only one item is left

## A Walkthrough

Let's sort: `[43, 41, 23, 57, 45, 12]`

### Pass 1 — Find the smallest in the whole list

```
[43, 41, 23, 57, 45, 12]
  ↑   ↑
 43 > 41? Yes → smallest so far is 41
```

```
[43, 41, 23, 57, 45, 12]
      ↑  ↑
     41 > 23? Yes → smallest so far is 23
```

```
[43, 41, 23, 57, 45, 12]
          ↑   ↑
         23 > 57? No → smallest is still 23
```

```
[43, 41, 23, 57, 45, 12]
              ↑   ↑
             23 > 45? No → smallest is still 23
```

```
[43, 41, 23, 57, 45, 12]
                  ↑   ↑
                 23 > 12? Yes → smallest is 12 ✅
```

**Smallest is 12 at index 5 → swap with first item (43)**

```
Before: [43, 41, 23, 57, 45, 12]
After:  [12, 41, 23, 57, 45, 43]
         --- sorted
```

### Pass 2 — Find the smallest in [41, 23, 57, 45, 43]

```
[12, 41, 23, 57, 45, 43]
     ↑   ↑
    41 > 23? Yes → smallest so far is 23
```

```
[12, 41, 23, 57, 45, 43]
         ↑   ↑
        23 > 57? No
```

```
[12, 41, 23, 57, 45, 43]
             ↑   ↑
            23 > 45? No
```

```
[12, 41, 23, 57, 45, 43]
                 ↑   ↑
                23 > 43? No → smallest is 23 ✅
```

**Swap 23 with 41 (second item)**

```
Before: [12, 41, 23, 57, 45, 43]
After:  [12, 23, 41, 57, 45, 43]
         ------ sorted
```

### Pass 3 — Find the smallest in [41, 57, 45, 43]

41 is already the smallest here, so it stays put.

```
After:  [12, 23, 41, 57, 45, 43]
         --------- sorted
```

### Pass 4 — Find the smallest in [57, 45, 43]

Smallest is 43. Swap with 57.

```
Before: [12, 23, 41, 57, 45, 43]
After:  [12, 23, 41, 43, 45, 57]
         ------------ sorted
```

### Pass 5 — Find the smallest in [45, 57]

45 is already the smallest. Done.

```
Final:  [12, 23, 41, 43, 45, 57]
         ---------------- sorted ✅
```

## The Code

```python
def selection_sort(arr):
    # Go through each position in the list
    for i in range(len(arr)):
        # Assume the first unsorted item is the smallest
        min_idx = i
        
        # Check the rest of the list for something smaller
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j  # Found a new smallest!
        
        # Swap the smallest item into its correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Try it
my_list = [64, 25, 12, 22, 11]
print(selection_sort(my_list))
# Output: [11, 12, 22, 25, 64]
```

## What Each Part Does

| Part | What it does |
|------|-------------|
| `i` | Points to where the next smallest item should go |
| `min_idx` | Remembers where the current smallest item is |
| Inner `for` loop | Scans the unsorted section looking for something smaller |
| `arr[i], arr[min_idx] = arr[min_idx], arr[i]` | Swaps the smallest item into its correct spot |

## Visual Analogy: The Trophy Case 🏆

Imagine you have a row of trophies of different heights:

```
[ 🏆🏆🏆🏆🏆🏆 ]
```

1. Walk down the row, find the SHORTEST trophy
2. Move it all the way to the left (first position)
3. Now ignore the first one, look at the rest
4. Find the next shortest, move it to the second position
5. Repeat until all trophies are in order from shortest to tallest

That's Selection Sort.

## When to Use Selection Sort

**Use it when:**
- You have a small list
- Memory is very limited (it only needs 1 extra variable)
- You want the fewest possible swaps (at most n-1 swaps)
- You are learning how sorting works

**Don't use it when:**
- You have a large list — it's slow (O(n²))
- You need a stable sort (it can reorder equal items)

## Time & Space

| Metric | Value |
|--------|-------|
| Best case | O(n²) — checks everything even if already sorted |
| Average case | O(n²) |
| Worst case | O(n²) |
| Space | O(1) — sorts in place, no extra memory needed |
| Swaps | n-1 at most — very few compared to Bubble Sort |

**Fun fact:** Even if the list is already sorted, Selection Sort still does ALL the comparisons (O(n²)). It has no "early exit" like Bubble Sort does.

## Classwork

### Part 1: Trace the Algorithm

Trace Selection Sort on `[29, 10, 14, 37, 13]`. Write the list after each swap.

```
Start: [29, 10, 14, 37, 13]

After pass 1: _________________

After pass 2: _________________

After pass 3: _________________

After pass 4: _________________

Final: _________________
```

### Part 2: Fill in the Blanks

```python
def selection_sort(arr):
    for i in range(_________):
        min_idx = _________
        for j in range(_________, len(arr)):
            if arr[min_idx] > arr[_________]:
                min_idx = _________
        arr[i], arr[_________] = arr[min_idx], arr[_________]
    return arr
```

### Part 3: Fix the Errors

```python
def selection_sort(arr):
    for i in range(1, len(arr)):
        min_idx = i + 1
        for j in range(i, len(arr)):
            if arr[min_idx] < arr[j]:
                min_idx = j
        arr[min_idx], arr[j] = arr[j], arr[min_idx]
    return arr
```

What is wrong? List each error:

1. ___________________

2. ___________________

3. ___________________

4. ___________________

---

### Part 4: Sort Words by Length

Write a function that sorts a list of words from shortest to longest.

```python
def sort_by_length(words):
    # Write your code here
    pass

words = ["cat", "elephant", "dog", "snake"]
print(sort_by_length(words))
# Should print: ['cat', 'dog', 'snake', 'elephant']
```

---

### Part 5: Sort Descending

Change the function so it sorts from biggest to smallest.

```python
def selection_sort_descending(arr):
    # Write your code here
    pass

numbers = [5, 1, 4, 2, 8]
print(selection_sort_descending(numbers))
# Should print: [8, 5, 4, 2, 1]
```

---

### Part 6: Questions

1. Why does the outer loop go from 0 to n-1 instead of n?

   _________________________________

2. After 3 passes of Selection Sort on a 10-item list, how many items are definitely in their final sorted position?

   _________________________________

3. In Selection Sort, the inner loop is finding the _________ item in the unsorted section.

4. How is Selection Sort different from Bubble Sort? Which one does more swaps?

   _________________________________

---

## Homework

### Problem 1: Trace the Algorithm

Sort `[7, 4, 1, 8, 3, 6]` with Selection Sort. Write the list after each pass.

```
Start: [7, 4, 1, 8, 3, 6]

Pass 1 (i=0): _________________

Pass 2 (i=1): _________________

Pass 3 (i=2): _________________

Pass 4 (i=3): _________________

Pass 5 (i=4): _________________
```

---

### Problem 2: Count Comparisons

How many comparisons does Selection Sort make on a list of 6 items?

Formula for total comparisons: (n-1) + (n-2) + (n-3) + ... + 1 = n(n-1)/2

For n=6: __________

---

### Problem 3: Write from Memory

Write the `selection_sort` function without looking at your notes.

```python
def selection_sort(arr):

    # Your code here

    return arr
```

---

### Problem 4: Sort These Lists

Work out the sorted result for each list.

List A: `[15, 3, 9, 1, 12]`
Sorted: _________________

List B: `[100, 50, 75, 25, 60]`
Sorted: _________________

List C: `["mango", "apple", "grape", "banana"]`
Sorted: _________________

---

### Problem 5: Sort Tuples

Use Selection Sort to sort a list of tuples by the **second** value.

```python
def sort_tuples(tuples):
    # Write your code here
    pass

data = [('a', 3), ('b', 1), ('c', 2)]
print(sort_tuples(data))
# Should print: [('b', 1), ('c', 2), ('a', 3)]
```

---

### Problem 6: Explain in Your Own Words

1. What does `min_idx` store? Why do we need it?

   _________________________________

   _________________________________

2. What happens during the swap step?

   _________________________________

   _________________________________

3. Why is Selection Sort slow for large lists?

   _________________________________

   _________________________________

4. How many swaps does Selection Sort make in total for a list of n items?

   _________________________________

---

### Problem 7: Trace a Worst-Case List

Trace Selection Sort on a reverse-sorted list: `[9, 7, 5, 3, 1]`

```
Start: [9, 7, 5, 3, 1]

Pass 1 (i=0): _________________

Pass 2 (i=1): _________________

Pass 3 (i=2): _________________

Pass 4 (i=3): _________________

How many total comparisons? _________

How many swaps? _________
```
