# Binary Search Lesson

Binary Search is a more efficient search algorithm than Linear Search. It works by repeatedly dividing the search space in half until the target element is found or the search space becomes empty.

**Crucially, Binary Search only works on lists that are already sorted.**

## How it Works

We keep track of the search space using two pointers:

- `low` → the first index of the current search space
- `high` → the last index of the current search space

Then we repeat until the space is empty:

1.  **Start at the middle:** Find the middle element: `mid = (low + high) // 2`.
2.  **Compare:** Compare the middle element with the target value.
3.  **Check for Match:** If the middle element matches the target, return its index.
4.  **Narrow the search:**
    - If the target is **greater** than the middle element, it must be in the right half of the list. Set `low = mid + 1`.
    - If the target is **less** than the middle element, it must be in the left half of the list. Set `high = mid - 1`.
5.  **Repeat:** Repeat steps 1-4 with the new half-sized search area.
6.  **End of list:** If `low` passes `high`, the search space is empty — return `-1`.

> **Key invariant:** Because the list is sorted, comparing against the middle element lets us *guarantee* which half the target must be in (or that it isn't there at all). That's what makes throwing away half the list safe.

## Real-World Intuition: The Guessing Game 

Imagine I pick a number between 1 and 100 and you have to guess it. After each guess, I tell you "higher" or "lower".

**Bad strategy:** guess 1, 2, 3, ... (Linear Search — up to 100 guesses)

**Smart strategy (Binary Search):**

| Guess | Response | What we now know | Remaining range |
| :---: | :---: | :--- | :---: |
| 50 | "Higher" | Number is in 51–100 | 50 numbers |
| 75 | "Lower" | Number is in 51–74 | 24 numbers |
| 62 | "Higher" | Number is in 63–74 | 12 numbers |
| 68 | "Higher" | Number is in 69–74 | 6 numbers |
| 71 | "Lower" | Number is in 69–70 | 2 numbers |
| 69 | Correct! | Found it | 0 |

Only **6 guesses** instead of up to 100. Each answer cuts the range in half — that's exactly how Binary Search works on a sorted array. The array values play the role of the number line; the sorted order plays the role of the "higher/lower" hints.

The same idea applies to finding a word in a physical dictionary: you don't read page by page — you open near the middle and decide which half to look at next.

## Example Walkthroughs

### Example 1: Target Found

Searching for `20` in `[1, 5, 8, 12, 15, 20, 25, 30]`:

```text
Step 1: [1, 5, 8, 12, 15, 20, 25, 30]  (low=0, high=7)
                   ^ mid=3 (val=12)
         Target 20 > 12, search right half.

Step 2: [15, 20, 25, 30] (low=4, high=7)
               ^ mid=5 (val=20)
         Target 20 == 20, Match Found! Return index 5.
```

As a trace table:

| Step | low | high | mid = (low+high)//2 | arr[mid] | Comparison | Action |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| 1 | 0 | 7 | 3 | 12 | 12 < 20 | `low = mid + 1` → 4 |
| 2 | 4 | 7 | 5 | 20 | 20 == 20 | **return 5** |

### Example 2: Target Not Found

Searching for `9` in `[1, 5, 8, 12, 15, 20, 25, 30]`:

| Step | low | high | mid | arr[mid] | Comparison | Action |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| 1 | 0 | 7 | 3 | 12 | 12 > 9 | `high = mid - 1` → 2 |
| 2 | 0 | 2 | 1 | 5 | 5 < 9 | `low = mid + 1` → 2 |
| 3 | 2 | 2 | 2 | 8 | 8 < 9 | `low = mid + 1` → 3 |
| 4 | 3 | 2 | — | — | `low > high` → loop ends | **return -1** |

Notice how the loop terminates: once `low` moves past `high`, there is no search space left, so the target cannot exist in the list.

### Example 3: Target at the Very End

Searching for `30` in `[1, 5, 8, 12, 15, 20, 25, 30]`:

| Step | low | high | mid | arr[mid] | Comparison | Action |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| 1 | 0 | 7 | 3 | 12 | 12 < 30 | `low = mid + 1` → 4 |
| 2 | 4 | 7 | 5 | 20 | 20 < 30 | `low = mid + 1` → 6 |
| 3 | 6 | 7 | 6 | 25 | 25 < 30 | `low = mid + 1` → 7 |
| 4 | 7 | 7 | 7 | 30 | 30 == 30 | **return 7** |

This is close to the worst case: even when the target sits at the boundary, Binary Search only needs $\log_2 n$ steps.

### Example 4: Duplicates

Binary Search finds *an* index of the target — not necessarily the first one.

Searching for `7` in `[3, 7, 7, 7, 9, 11]` returns index `2` (a valid match), even though another `7` lives at index `1`. If you need the *first* occurrence, keep searching the left half after a match (`high = mid - 1`) and remember the best index found so far.

## Why is it Logarithmic?
Every step in Binary Search reduces the search area by half. If you have $n$ elements, after one step you have $n/2$, then $n/4$, then $n/8$, and so on. The number of steps required to reach 1 is the power to which 2 must be raised to get $n$. This is the definition of $\log_2 n$.

- For **1,000** elements: ~10 steps
- For **1,000,000** elements: ~20 steps
- For **1,000,000,000** elements: ~30 steps

This is incredibly powerful!

## Pseudocode

```
procedure binarySearch(sortedList, target)
  low = 0
  high = length(sortedList) - 1
  
  while low <= high
    mid = (low + high) / 2
    if sortedList[mid] == target
      return mid
    else if sortedList[mid] < target
      low = mid + 1
    else
      high = mid - 1
    end if
  end while
  
  return -1
end procedure
```

## Python Implementation

Here is how you can implement the Binary Search algorithm in Python:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If the element is found at mid
        if arr[mid] == target:
            return mid
        # If the target is greater than mid, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        # If the target is smaller than mid, ignore the right half
        else:
            high = mid - 1
            
    # If the element is not found, return -1
    return -1

# Example usage:
my_sorted_list = [1, 5, 8, 12, 15, 20, 25, 30]
target_val = 20
result = binary_search(my_sorted_list, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
# Output: Element found at index: 5
```

## Complexity Analysis

Binary Search is significantly faster than Linear Search for large datasets.

### Time Complexity
- **Best Case: $O(1)$** - The target element is found at the middle of the array on the very first try.
- **Average Case: $O(\log n)$** - On average, the search space is halved $\log_2 n$ times.
- **Worst Case: $O(\log n)$** - The target element is at the far ends of the array or not present at all.

### Space Complexity
- **Iterative Approach: $O(1)$** - Only a few variables (`low`, `high`, `mid`) are used regardless of the input size.
- **Recursive Approach: $O(\log n)$** - Due to the call stack depth in recursion.

## Binary Search vs. Linear Search

| Feature | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **Prerequisite** | None (can be unsorted) | Must be **Sorted** |
| **Worst-case Time** | $O(n)$ | $O(\log n)$ |
| **Best-case Time** | $O(1)$ | $O(1)$ |
| **Approach** | Sequential | Divide and Conquer |
| **Efficiency** | Better for small lists | Better for large lists |

## Recursive Implementation

While the iterative version is often preferred for its space efficiency, the recursive version is a classic example of the "Divide and Conquer" strategy.

```python
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage:
# result = binary_search_recursive(my_list, target, 0, len(my_list) - 1)
```

## Line-by-Line Breakdown of the Iterative Version

Let's dissect every line and understand *why* it exists:

```python
def binary_search(arr, target):
    low = 0                    # ① leftmost index still under consideration
    high = len(arr) - 1        # ② rightmost index still under consideration

    while low <= high:         # ③ loop while the search space is non-empty
        mid = (low + high) // 2  # ④ middle index (floor division rounds down)

        if arr[mid] == target: # ⑤ luck! direct hit
            return mid
        elif arr[mid] < target:# ⑥ everything at/before mid is too small
            low = mid + 1      # ⑦ discard left half INCLUDING mid
        else:                  # ⑧ arr[mid] > target: everything at/after mid is too big
            high = mid - 1     # ⑨ discard right half INCLUDING mid

    return -1                  # ⑩ space exhausted → target isn't there
```

**Detailed explanations:**

- **①② Why `len(arr) - 1` and not `len(arr)`?** We treat `low` and `high` as **inclusive** bounds: both endpoints are still valid candidates. Since valid indices run from `0` to `len(arr) - 1`, starting `high` at `len(arr)` would immediately index out of range when the array has one element.
- **③ Why `<=` and not `<`?** The condition `low <= high` means "there is still at least one element between the pointers". When `low == high` exactly one candidate remains — we must be allowed to check it. With `<`, that last element is silently skipped.
- **④ Why `// 2`?** Regular division gives a float like `3.5`; indices must be integers. Floor division `(low + high) // 2` rounds down, which always lands inside `[low, high]`.
- **⑥⑦ Why `mid + 1` and not `mid`?** We already *know* `arr[mid] != target` (we're in the `elif`). Keeping `mid` in the range would re-examine a proven-dead element forever — that's the recipe for an infinite loop. Eliminating it shrinks the space by at least one every iteration, guaranteeing termination.
- **⑩ Why can we safely give up?** Every element excluded so far was excluded by proof: if `arr[mid] < target`, then *all* elements left of `mid` are also `< target` (sorted!). So when the pointers cross, no unexamined element remains.

## More Snippets: Useful Variants (With Explanations)

### Variant 1 — First Occurrence (handles duplicates)

Plain binary search returns *any* matching index. To get the **leftmost** match, don't stop when you find one — record it, then keep hunting to the left:

```python
def find_first(arr, target):
    low, high = 0, len(arr) - 1
    result = -1                        # default: not found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid               # remember this hit…
            high = mid - 1             # …but an earlier one may exist → go left
        elif arr[mid] < target:
            low = mid + 1              # target is somewhere to the right
        else:
            high = mid - 1             # target is somewhere to the left

    return result

nums = [3, 7, 7, 7, 9, 11]
print(find_first(nums, 7))   # Output: 1  (not 2!)
```

**Why it works:** the moment we see the target we have a *valid answer*, but possibly not the best one. Setting `high = mid - 1` keeps searching strictly-left territory. Any later match found there overwrites `result` with a smaller index. When the loop ends, `result` holds the smallest index seen — which, because we always moved left after a hit, is guaranteed to be the very first occurrence. Cost: still $O(\log n)$, just without early exit.

### Variant 2 — Last Occurrence & Counting Duplicates

Flip one line and you get the **rightmost** match:

```python
def find_last(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1              # mirror image: keep searching RIGHT
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def count_occurrences(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return 0
    return find_last(arr, target) - first + 1

nums = [3, 7, 7, 7, 9, 11]
print(find_last(nums, 7))          # Output: 3
print(count_occurrences(nums, 7))  # Output: 3
print(count_occurrences(nums, 5))  # Output: 0
```

**Why counting works:** in a sorted array every copy of the target sits in one contiguous block. If the block spans indices `[first, last]`, its size is simply `last - first + 1`. Two $O(\log n)$ searches beat scanning the block linearly ($O(n)$) when duplicates are millions long.

### Variant 3 — Insertion Point ("where would it go?")

A tiny twist turns the search into `bisect_left`: even if the target is absent, report where it *should* be inserted to keep the list sorted:

```python
def insertion_point(arr, target):
    low, high = 0, len(arr)          # note: high starts at len(arr),
                                     # because inserting AT THE END is legal
    while low < high:                # different flavor: half-open range [low, high)
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1            # insertion point is right of mid
        else:
            high = mid               # arr[mid] >= target → mid itself may be the spot

    return low                       # low == high == final position

data = [10, 20, 30, 50]
print(insertion_point(data, 35))  # Output: 3  → insert between 30 and 50
print(insertion_point(data, 5))   # Output: 0  → new front element
print(insertion_point(data, 99))  # Output: 4  → append at end
```

**What changed and why:**

- We now search for a **boundary**, not a value, so there is no early `return`. The loop narrows until `low == high`, and either pointer is the answer.
- `high = len(arr)` (not `len(arr) - 1`) because "after the last element" is a legitimate insertion slot.
- The comparison collapses into two cases: elements smaller than the target can't affect the answer (`mid + 1`), everything else might be it (`high = mid` — safe here because the loop condition uses `<`, so no infinite loop).
- This exact pattern powers `list.sort()` + insert pipelines and is what Python's `bisect.bisect_left` does.

### Variant 4 — Binary Search Without an Array (on "the answer" itself!)

The deepest insight about binary search: **it never needed the array.** It needs anything where a yes/no question splits the world cleanly in two. Example: find $\lfloor\sqrt{n}\rfloor$ using only comparisons:

```python
def integer_sqrt(n):
    """Largest whole number x such that x*x <= n."""
    if n < 2:
        return n                 # sqrt(0)=0, sqrt(1)=1

    low, high = 1, n // 2        # sqrt(n) always fits in [1, n//2] for n >= 2
    answer = 1

    while low <= high:
        mid = (low + high) // 2
        squared = mid * mid      # our "probe", playing the role of arr[mid]

        if squared == n:
            return mid           # perfect square — exact hit
        elif squared < n:
            answer = mid         # mid qualifies… but a bigger one might too
            low = mid + 1        # …so look right
        else:
            high = mid - 1       # overshoot — look left

    return answer                # largest value whose square stayed <= n

print(integer_sqrt(16))   # Output: 4
print(integer_sqrt(17))   # Output: 4  (floor of 4.123…)
print(integer_sqrt(99))   # Output: 9
```

**Why it works:** imagine the infinite sequence `1·1, 2·2, 3·3, 4·4, …`. It's *monotonically increasing* — exactly the property a sorted array has. "Is `x² ≤ n`?" answers `True` for a prefix of that sequence and `False` afterward, so binary search can locate the boundary. For `n = 10¹⁸` this needs ~60 iterations instead of ~10¹⁸ probes. This "search on the answer space" trick solves a huge family of interview problems (capacity to ship packages, minimum eating speed, split-array-largest-sum…).

### Variant 5 — It Works on Any Comparable Type (e.g., Strings)

Nothing requires numbers. Anything supporting `<` works, including strings (compared alphabetically):

```python
words = ["banana", "cherry", "date", "apple"]   # ← NOT sorted yet!
words.sort()                                    # prerequisite: ["apple","banana","cherry","date"]

idx = binary_search(words, "cherry")   # reuse the original function!
print(idx)                             # Output: 2
print(binary_search(words, "fig"))     # Output: -1 (absent)
```

Python compares strings character-by-character (lexicographic order), so `"apple" < "banana"` is `True` — and that's all binary search asks for. Same trick works for tuples, dates, or your own objects once you define `__lt__`.

### Variant 6 — Don't Roll Your Own: Python's `bisect` Module

In production Python, use the battle-tested standard library version:

```python
import bisect

nums = [3, 7, 7, 7, 9, 11]

i = bisect.bisect_left(nums, 7)        # leftmost insertion point → 1
j = bisect.bisect_right(nums, 7)       # rightmost insertion point → 4

found = i < len(nums) and nums[i] == 7 # standard idiom for "is it present?"
print(i, j, found)                     # Output: 1 4 True

bisect.insort(nums, 8)                 # insert 8 keeping the list sorted
print(nums)                            # [3, 7, 7, 7, 8, 9, 11]
```

**Notes:**

- `bisect_left` returns where the target *starts* (first occurrence); `bisect_right` where it *ends+1*. Their difference is the count: `count = bisect_right(...) - bisect_left(...)` — same math as Variant 2!
- Both run in $O(\log n)$; they assume the list is already sorted (they never sort for you).
- `insort` inserts in place in $O(n)$ time overall (the shift dominates) but keeps code short and correct.

## Common Pitfalls (Read Before Coding!)

### 1. Forgetting the list must be sorted

Binary Search on `[30, 5, 20, 8, ...]` gives **wrong answers silently** — no error, just incorrect results. If you must search an unsorted list, either sort it first ($O(n \log n)$) or use Linear Search ($O(n)$).

### 2. Wrong loop condition: `while low < high` vs `while low <= high`

- With `<=`, the loop still runs when `low == high` (a one-element search space). This is what we want — a single remaining element can still be the target.
- With `<`, you skip checking that last element and can miss it. Example: searching for `30` in Example 3 above ends with `low = high = 7`; using `<` would exit early and wrongly return `-1`.

### 3. Mid calculation mistakes

```python
mid = low + high // 2   # WRONG: this is low + (high // 2) due to precedence!
mid = (low + high) // 2 # CORRECT
```

In Python, integer overflow isn't a concern, but in languages like Java/C++ `(low + high)` can overflow for huge arrays; there the safe form is:

```
mid = low + (high - low) / 2
```

Worth knowing for interviews!

### 4. Off-by-one when narrowing

After comparing with `arr[mid]`, mid itself is *eliminated* — so move to `mid + 1` or `mid - 1`, never just `mid`. Using `low = mid` can cause an **infinite loop**.

### 5. Returning the wrong thing for "not found"

Returning `None`, `0`, or raising an exception inconsistently confuses callers. The common convention is `-1` (or in Python, sometimes `None`) — just be consistent and document it.

## Quick Self-Check

Try answering before looking back at the lesson:

1. What are the two pointer variables that define the current search space?
2. After one comparison, roughly what fraction of the search space remains?
3. In a list of 16 elements, what is the maximum number of comparisons Binary Search needs?
4. Why does `low > high` mean the target is definitely absent?

<details>
<summary>Answers</summary>

1. `low` (start index) and `high` (end index).
2. Half of it.
3. 4 comparisons (since $\log_2 16 = 4$).
4. The pointers have crossed, meaning every element has been excluded by some earlier comparison — the sorted order guarantees none of them could be the target.
</details>

## Exercise

1.  Given the sorted list `[10, 20, 30, 40, 50, 60, 70, 80, 90]`, trace the Binary Search for target `70`. Write down the values of `low`, `high`, and `mid` for each step. *(Answers: Step 1: low=0, high=8, mid=4; Step 2: low=5, high=8, mid=6 → found at index 6)*
2.  Trace the search for target `35` in the same list. How do you know it's not there? *(Step 1: mid=4 (val=50) → go left; Step 2: low=0, high=3, mid=1 (val=20) → go right; Step 3: low=2, high=3, mid=2 (val=30) → go right; Step 4: low=3, high=3, mid=3 (val=40) → go left; now low=3, high=2 → return -1)*
3.  What is the time complexity of Binary Search in the best, average, and worst cases? (Hint: How many times can you halve a number before it reaches 1?)
4.  Why can't Binary Search be used on an unsorted list?
5.  **Challenge:** Modify `binary_search` so that when duplicates exist, it returns the index of the **first** occurrence of the target. E.g., for `[3, 7, 7, 7, 9]` and target `7`, it should return `1`, not `2`.
6.  **Challenge (interview classic):** Given a sorted list that has been **rotated** at an unknown pivot (e.g., `[40, 50, 60, 10, 20, 30]`), can you still find a target in $O(\log n)$? Hint: at any `mid`, at least one half of the array is still sorted — figure out which one contains the target.
