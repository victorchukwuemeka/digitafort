# Merge Sort Lesson

Merge Sort is an efficient, comparison-based, and stable sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. It is a divide and conquer algorithm.

## How it Works

Merge Sort works by recursively breaking down a list into several sub-lists until each sub-list contains a single element, and then merging those sub-lists in a manner that results into a sorted list.

1.  **Divide:** The unsorted list is divided into `n` sublists, each containing one element (a list of one element is considered sorted).
2.  **Conquer (Merge):** Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

The merging process is the core of the algorithm:
- Create an empty list.
- Compare the first elements of the two sublists you are merging.
- Add the smaller of the two to the empty list.
- Repeat until one of the sublists is empty.
- Add the remaining elements from the non-empty sublist to the end of the new list.

## Diagram

Here is a visual representation of Merge Sort.

![Merge Sort Diagram](02_Merge_Sort_Diagram.gif)

## Pseudocode

```
procedure mergeSort(list)
  if length(list) > 1
    mid = length(list) / 2
    leftHalf = list[0...mid]
    rightHalf = list[mid...length(list)]

    mergeSort(leftHalf)
    mergeSort(rightHalf)

    i = 0
    j = 0
    k = 0

    while i < length(leftHalf) and j < length(rightHalf)
      if leftHalf[i] < rightHalf[j]
        list[k] = leftHalf[i]
        i = i + 1
      else
        list[k] = rightHalf[j]
        j = j + 1
      end if
      k = k + 1
    end while

    while i < length(leftHalf)
      list[k] = leftHalf[i]
      i = i + 1
      k = k + 1
    end while

    while j < length(rightHalf)
      list[k] = rightHalf[j]
      j = j + 1
      k = k + 1
    end while
  end if
end procedure
```

## Python Implementation

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage:
my_list = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [5, 6, 7, 11, 12, 13]
```

## Detailed Step-by-Step Walkthrough on Real Data

Let's become human debuggers and trace Merge Sort on a real list, number by number, using the list `[38, 27, 43, 3, 9, 82, 10]`.

### The Whole Story in One Picture

Merge Sort has two phases:

1. **DIVIDE** — recursion *descends*, splitting until every segment is a single element (a single element is trivially sorted).
2. **CONQUER (MERGE)** — recursion *unwinds*, and on the way back up each pair of sorted halves is merged back into one sorted segment.

The magic is that merging **mutates the original `arr` in place** while reading from the two copies `L` and `R`.

### The "i j k" Pointers

Three pointers, each on a different list:

- `i` — walks through **`L`** (the left half)
- `j` — walks through **`R`** (the right half)
- `k` — walks through **`arr`** (the segment being rebuilt — where we *write* the next sorted element)

`i = j = k = 0` means "all three start at the front."

### Phase 1 — The Divide (recursion goes DOWN)

```
merge_sort([38, 27, 43, 3, 9, 82, 10])          depth 0
├── merge_sort([38, 27, 43])                    depth 1   (L of top)
│   ├── merge_sort([38])                        depth 2   ← base case, returns immediately
│   └── merge_sort([27, 43])                    depth 2
│       ├── merge_sort([27])                    depth 3   ← base case
│       └── merge_sort([43])                    depth 3   ← base case
└── merge_sort([3, 9, 82, 10])                  depth 1   (R of top)
    ├── merge_sort([3, 9])                      depth 2
    │   ├── merge_sort([3])                     depth 3   ← base case
    │   └── merge_sort([9])                     depth 3   ← base case
    └── merge_sort([82, 10])                    depth 2
        ├── merge_sort([82])                    depth 3   ← base case
        └── merge_sort([10])                    depth 3   ← base case
```

### Phase 2 — The Merge (recursion comes back UP)

Merges happen in this order: **A, B, C, D, E, F**. Each table shows the state *right before* that write. To read each row: check the comparison, take the winner, write it at `arr[k]`, then advance the pointer of the side that won, and advance `k`.

#### Merge A — `[27] + [43]` → `[27, 43]`

| step | i | j | k | compare | winner | arr after |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | `27 < 43` → **T** | `27` → arr[0] | `[27, 43]` |
| main loop exits (i=1 not < 1) → leftover loop copies `43` → arr[1] | | | | | | `[27, 43]` |

#### Merge B — `[38] + [27, 43]` → `[27, 38, 43]`

| step | i | j | k | compare | winner | arr after |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | `38 < 27` → **F** | `27` → arr[0] | `[27, 27, 43]` |
| 2 | 0 | 1 | 1 | `38 < 43` → **T** | `38` → arr[1] | `[27, 38, 43]` |
| leftover loop copies `43` → arr[2] | | | | | | `[27, 38, 43]` |

#### Merge C — `[3] + [9]` → `[3, 9]`

| step | i | j | k | compare | winner | arr after |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | `3 < 9` → **T** | `3` → arr[0] | `[3, 9]` |
| leftover loop copies `9` → arr[1] | | | | | | `[3, 9]` |

#### Merge D — `[82] + [10]` → `[10, 82]`

| step | i | j | k | compare | winner | arr after |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | `82 < 10` → **F** | `10` → arr[0] | `[10, 10]` |
| leftover loop copies `82` → arr[1] | | | | | | `[10, 82]` |

> Note: this is why `[10, 10]` briefly appears — the old `82` at index 1 hasn't been overwritten yet. Totally normal.

#### Merge E — `[3, 9] + [10, 82]` → `[3, 9, 10, 82]`

| step | i | j | k | compare | winner | arr after |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | `3 < 10` → **T** | `3` → arr[0] | `[3, 9, 82, 10]` |
| 2 | 1 | 0 | 1 | `9 < 10` → **T** | `9` → arr[1] | `[3, 9, 82, 10]` |
| main loop exits (i=2 not < 2) → leftover loop copies `10` → arr[2], then `82` → arr[3] | | | | | | `[3, 9, 10, 82]` |

#### Merge F — `[27, 38, 43] + [3, 9, 10, 82]` → the big final one

| step | i | j | k | compare | winner | arr after |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | `27 < 3` → **F** | `3` → arr[0] | `[3, 27, 43, 3, 9, 82, 10]` |
| 2 | 0 | 1 | 1 | `27 < 9` → **F** | `9` → arr[1] | `[3, 9, 43, 3, 9, 82, 10]` |
| 3 | 0 | 2 | 2 | `27 < 10` → **F** | `10` → arr[2] | `[3, 9, 10, 3, 9, 82, 10]` |
| 4 | 0 | 3 | 3 | `27 < 82` → **T** | `27` → arr[3] | `[3, 9, 10, 27, 9, 82, 10]` |
| 5 | 1 | 3 | 4 | `38 < 82` → **T** | `38` → arr[4] | `[3, 9, 10, 27, 38, 82, 10]` |
| 6 | 2 | 3 | 5 | `43 < 82` → **T** | `43` → arr[5] | `[3, 9, 10, 27, 38, 43, 10]` |
| main loop exits (i=3 not < 3) → leftover loop copies `82` → arr[6] | | | | | | `[3, 9, 10, 27, 38, 43, 82]` |

### The "Physical Mutation" Insight

When you see `arr = [3, 9, 10, 27, 9, 82, 10]` — that `9`, `82`, `10` sitting in the tail are **garbage from before**, not mistakes. `L` and `R` still hold the real values (`[27, 38, 43]` and `[3, 9, 10, 82]`), so we can safely overwrite old slots. That is exactly why the two leftover loops (`while i < len(L)` / `while j < len(R)`) exist — they flush whatever is left in `L` or `R` into the remaining slots of `arr`.

### Stability Bonus

The comparison `if L[i] < R[j]` uses a strictly `<`. When values are equal, we take from `R`, and since `R` elements always come from positions *after* `L` elements in the original list, equal values keep their original order → **stable sort**. Change `<` to `<=` and you would break stability.

## Exercise

1.  Manually trace the Merge Sort algorithm on the list `[38, 27, 43, 3, 9, 82, 10]`. Draw the tree of recursive calls and the merging steps.
2.  Merge Sort has a time complexity of O(n log n). Why is it generally faster than O(n^2) algorithms like Bubble Sort for large lists?
3.  Merge Sort requires additional memory to create the sublists. How much extra space does it need? This is known as its space complexity.
