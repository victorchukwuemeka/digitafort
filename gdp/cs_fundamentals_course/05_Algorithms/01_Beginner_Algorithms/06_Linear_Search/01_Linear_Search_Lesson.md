# Linear Search Lesson

Linear Search (also called **Sequential Search**) is the simplest search algorithm. It works by checking every element in a list one by one from the beginning until the target element is found or the end of the list is reached.

While not very efficient for large datasets, Linear Search is easy to understand, works on **unsorted** lists, and has several useful variants that optimize for different scenarios.

## How it Works

1.  **Start at the first element:** Begin at index 0 of the list.
2.  **Compare:** Compare the current element with the target value.
3.  **Check for Match:** If the current element matches the target, return its index.
4.  **Move to next:** If it doesn't match, move to the next index in the list.
5.  **Repeat:** Repeat steps 2-4 until the target is found or you reach the end of the list.
6.  **End of list:** If you reach the end without finding the target, return a value indicating the element is not present (usually -1).

## Pseudocode

```
procedure linearSearch(list, target)
  for each index i from 0 to length(list) - 1
    if list[i] == target
      return i
    end if
  end for
  return -1
end procedure
```

## Python Implementation — Basic Form

Here is the standard implementation of the Linear Search algorithm in Python:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
my_list = [10, 5, 20, 15, 30]
target_val = 20
result = linear_search(my_list, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
# Output: Element found at index: 2
```

### Step-by-Step Walkthrough

Searching for `20` in `[10, 5, 20, 15, 30]`:

```
Step 1: Compare arr[0]=10 with target 20 → No match
Step 2: Compare arr[1]=5  with target 20 → No match
Step 3: Compare arr[2]=20 with target 20 → Match! Return index 2
```

Total comparisons made: **3**

---

## Variant 1: Sentinel Linear Search

In standard linear search, we check two conditions at every step: (1) have we reached the end of the array? and (2) does the current element match? Sentinel search eliminates the first check by placing the target value at the end of the array (the "sentinel" position), so we only need to check for a match each iteration.

### How it Works

1. Place the target value at the last position of the array.
2. Start comparing from index 0.
3. At each step, only compare the current element with the target (no bounds check needed).
4. When a match is found, check if it is the sentinel position or a real element.

### Pseudocode

```
procedure sentinelSearch(list, target)
  lastIndex = length(list) - 1
  lastElement = list[lastIndex]

  // Place sentinel
  list[lastIndex] = target

  i = 0
  while list[i] != target
    i = i + 1
  end while

  // Restore original last element
  list[lastIndex] = lastElement

  if i < lastIndex or list[lastIndex] == target
    return i
  end if
  return -1
end procedure
```

### Python Implementation

```python
def sentinel_search(arr, target):
    n = len(arr)
    last = arr[n - 1]

    # Place sentinel
    arr[n - 1] = target

    i = 0
    while arr[i] != target:
        i += 1

    # Restore original last element
    arr[n - 1] = last

    if i < n - 1 or arr[n - 1] == target:
        return i
    return -1

# Example:
data = [10, 5, 20, 15, 30]
result = sentinel_search(data, 20)
print(f"Found at index: {result}")  # Output: Found at index: 2
```

### Why Use It?

- In each loop iteration, only **one comparison** is made instead of two (element match + bounds check).
- This reduces the number of comparisons by roughly **50%**.
- Best suited when the array is large and search is frequent.

> **Note:** Sentinel search modifies the original array temporarily. It is not suitable for read-only arrays or concurrent access scenarios.

---

## Variant 2: Recursive Linear Search

Instead of using a loop, linear search can be written recursively. The function calls itself with the next index until the target is found or the base case (end of array) is reached.

### Pseudocode

```
procedure recursiveLinearSearch(list, target, index)
  if index >= length(list)
    return -1
  end if
  if list[index] == target
    return index
  end if
  return recursiveLinearSearch(list, target, index + 1)
end procedure
```

### Python Implementation

```python
def recursive_linear_search(arr, target, index=0):
    # Base case: reached end of array
    if index >= len(arr):
        return -1

    # Base case: found the target
    if arr[index] == target:
        return index

    # Recursive case: search next index
    return recursive_linear_search(arr, target, index + 1)

# Example:
my_list = [10, 5, 20, 15, 30]
result = recursive_linear_search(my_list, 20)
print(f"Found at index: {result}")  # Output: Found at index: 2
```

### Why Use It?

- Useful for teaching recursion and understanding the call stack.
- In practice, the iterative version is preferred because recursive calls add overhead (stack frames) and risk **stack overflow** for very large arrays.

---

## Variant 3: Finding All Occurrences (Find All)

Sometimes you need to find **every** occurrence of a target, not just the first. This version collects all matching indices.

### Pseudocode

```
procedure findAllLinearSearch(list, target)
  results = empty list
  for each index i from 0 to length(list) - 1
    if list[i] == target
      append i to results
    end if
  end for
  return results
end procedure
```

### Python Implementation

```python
def find_all_linear_search(arr, target):
    results = []
    for i in range(len(arr)):
        if arr[i] == target:
            results.append(i)
    return results

# Example:
my_list = [3, 7, 3, 10, 3, 15]
indices = find_all_linear_search(my_list, 3)
print(f"Found at indices: {indices}")  # Output: Found at indices: [0, 2, 4]
```

### Why Use It?

- Common in database lookups, text search, and duplicate detection.
- Time complexity is always O(n) since every element must be checked.

---

## Variant 4: Linear Search with Early Exit on Sorted Data

When you know the array is **sorted**, you can stop the search early if you encounter a value greater than the target. This is a simple optimization that avoids unnecessary comparisons.

### Pseudocode

```
procedure sortedLinearSearch(sortedList, target)
  for each index i from 0 to length(sortedList) - 1
    if sortedList[i] == target
      return i
    end if
    if sortedList[i] > target
      return -1       // No point continuing — target can't appear later
    end if
  end for
  return -1
end procedure
```

### Python Implementation

```python
def sorted_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            return -1  # Early exit — remaining elements are all larger
    return -1

# Example:
sorted_list = [5, 10, 15, 20, 25]
result = sorted_linear_search(sorted_list, 18)
print(f"Found at index: {result}")  # Output: Found at index: -1
```

### Why Use It?

- When you can't use binary search but know the data is sorted, this saves time.
- In the best case, it exits after just one comparison (target is smaller than the first element).

---

## Variant 5: Find Minimum and Maximum

Linear search is also the basis for finding the **minimum** or **maximum** element in an unsorted list — a one-pass operation.

### Python Implementation

```python
def find_min(arr):
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

def find_max(arr):
    maximum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

# Example:
data = [14, 3, 27, 8, 21]
print(f"Min: {find_min(data)}")  # Output: Min: 3
print(f"Max: {find_max(data)}")  # Output: Max: 27
```

### Why Include This?

- Finding min/max in an unsorted list **always requires O(n)** — you must look at every element.
- This is the foundation of **tournament-style** comparisons used in sorting algorithms.

---

## Comparison of All Variants

| Variant | Time (Best) | Time (Average) | Time (Worst) | Space | Modifies Array? | Extra Use Case |
|---|---|---|---|---|---|---|
| Basic | O(1) | O(n) | O(n) | O(1) | No | General-purpose search |
| Sentinel | O(1) | O(n) | O(n) | O(1) | **Yes** (temp) | Frequent searches, fewer comparisons |
| Recursive | O(1) | O(n) | O(n) | O(n) stack | No | Learning recursion |
| Find All | O(n) | O(n) | O(n) | O(k) k=matches | No | Duplicate detection |
| Sorted Early Exit | O(1) | O(n) | O(n) | O(1) | No | Semi-sorted data |
| Find Min/Max | O(n) | O(n) | O(n) | O(1) | No | Extremes in unsorted data |

---

## Time & Space Complexity

- **Best Case:** O(1) — the target is the first element.
- **Average Case:** O(n) — on average, you check half the elements.
- **Worst Case:** O(n) — the target is the last element or not present.
- **Space Complexity:** O(1) — iterative versions use no extra space.

> **Key Insight:** Linear Search is always O(n) for min/max and Find All, because every element must be examined regardless of the target's position.

---

## When to Use Linear Search

- The list is **unsorted** and small to medium sized.
- You need to search only **once or a few times** (binary search setup cost isn't worth it).
- The data is stored in a **linked list** (binary search requires random access).
- You need to find **all occurrences** or perform a one-pass scan for min/max.

---

## When NOT to Use Linear Search

- The list is **sorted** and large — use **Binary Search** (O(log n)) instead.
- You perform **many searches** on the same dataset — consider sorting once then using binary search.
- The dataset is so large that O(n) scans are too slow — consider **hash tables** (O(1) average).

---

## Exercises

1.  **Trace Execution:** Given the list `[4, 8, 15, 16, 23, 42]`, trace the Basic Linear Search for target `23`. How many comparisons were made? What about for target `99`?

2.  **Sentinel Search:** Implement Sentinel Search for the list `[7, 2, 9, 1, 5]` searching for `9`. How many comparisons does it make compared to Basic Linear Search?

3.  **Recursive Depth:** For a list of 1000 elements, what is the maximum recursion depth that `recursive_linear_search` would reach when the target is at the last position? What risk does this pose?

4.  **Find All:** Given the list `[1, 3, 5, 3, 7, 3, 9]`, how many indices does `find_all_linear_search` return for target `3`? Trace each comparison.

5.  **Sorted Early Exit:** Given the sorted list `[2, 5, 8, 12, 16, 23, 38]`, how many comparisons does `sorted_linear_search` make for target `10`? At which point does it exit early?

6.  **Find Min/Max:** Trace `find_min` and `find_max` on `[14, 3, 27, 8, 21]`. How many comparisons does each make?

7.  **Complexity Analysis:** Explain why the best case for finding a specific element is O(1), but the best case for finding the minimum element is always O(n).

8.  **Design Challenge:** Given a circularly sorted array (e.g., `[15, 16, 23, 42, 5, 10, 12]` — sorted but rotated), can you use linear search with early exit? Why or why not? What modification would you need?
