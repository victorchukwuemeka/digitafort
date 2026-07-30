# Insertion Sort Lesson

## What is Insertion Sort?

Insertion Sort works like sorting playing cards. You pick up one card at a time and put it in the right spot among the cards you already sorted.

## How it Works (The Simple Version)

1. Start at the second item in the list
2. Save that item as "key"
3. Look at the items before it
4. If an item is bigger than key, move it to the right
5. Keep moving left until you find where key belongs
6. Put key in that spot
7. Repeat for the next item

## A Walkthrough

Let's sort: `[5, 2, 4, 6, 1, 3]`

**Step 1: Look at 2 (index 1)**
- Is 2 smaller than 5? Yes
- Move 5 to the right
- Put 2 in the first spot
- Result: `[2, 5, 4, 6, 1, 3]`

**Step 2: Look at 4 (index 2)**
- Is 4 smaller than 5? Yes
- Move 5 to the right
- Is 4 smaller than 2? No
- Put 4 after 2
- Result: `[2, 4, 5, 6, 1, 3]`

**Step 3: Look at 6 (index 3)**
- Is 6 smaller than 5? No
- Don't move anything
- Result: `[2, 4, 5, 6, 1, 3]`

**Step 4: Look at 1 (index 4)**
- 1 is smaller than 6, 5, 4, 2
- Move them all right
- Put 1 in the first spot
- Result: `[1, 2, 4, 5, 6, 3]`

**Step 5: Look at 3 (index 5)**
- 3 is smaller than 6, 5, 4
- Move them right
- 3 is bigger than 2, so stop
- Put 3 after 2
- Result: `[1, 2, 3, 4, 5, 6]`

Done. The list is sorted.

## The Code

```python
def insertion_sort(arr):
    # Go through each item starting from the second one
    for i in range(1, len(arr)):
        
        # Save the current item
        key = arr[i]
        
        # Start comparing with the item before it
        j = i - 1
        
        # Move items right while they are bigger than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift right
            j -= 1               # Move left
        
        # Put key in the right spot
        arr[j + 1] = key
    
    return arr

# Try it
my_list = [5, 1, 4, 2, 8]
print(insertion_sort(my_list))
# Output: [1, 2, 4, 5, 8]
```

## What Each Part Does

- `i` - keeps track of which item we are working on
- `key` - the item we are trying to place
- `j` - the position we are comparing against
- `arr[j + 1] = arr[j]` - moves an item one spot to the right
- `j -= 1` - moves one spot to the left to keep comparing
- `arr[j + 1] = key` - puts key in its correct spot

## When to Use Insertion Sort

Use it when:
- You have a small list (less than 50 items)
- The list is already almost sorted
- You are learning how sorting works

Do not use it when:
- You have a large list
- You need the fastest possible sort

## Classwork

### Part 1: Trace the Algorithm

Sort this list step by step. Write down what the list looks like after each item is placed.

`[8, 3, 5, 1, 9, 2]`

Starting state: `[8, 3, 5, 1, 9, 2]`

After placing 3: ___________________

After placing 5: ___________________

After placing 1: ___________________

After placing 9: ___________________

After placing 2: ___________________

Final sorted list: ___________________

---

### Part 2: Fill in the Blanks

Complete the code by filling in what is missing:

```python
def insertion_sort(arr):
    for i in range(1, _________):
        key = _________
        j = _________
        
        while j >= 0 and key _________ arr[j]:
            arr[j + 1] = _________
            j = j - _________
        
        arr[j + 1] = _________
    return arr
```

---

### Part 3: Fix the Errors

This code does not work. Find and fix the mistakes:

```python
def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i + 1
        
        while j >= 0 and key < arr[j]:
            arr[j] = arr[j + 1]
            j = j + 1
        
        arr[j] = key
    return arr
```

What is wrong? List each error:

1. ___________________

2. ___________________

3. ___________________

4. ___________________

---

### Part 4: Sort Strings

Change the function so it sorts words in alphabetical order. It should ignore capital letters (so "apple" and "Apple" are treated the same).

```python
def insertion_sort_words(arr):
    # Write your code here
    pass

words = ["banana", "Apple", "cherry", "date"]
print(insertion_sort_words(words))
# Should print: ['Apple', 'banana', 'cherry', 'date']
```

---

### Part 5: Sort Backwards

Change the function so it sorts from biggest to smallest (descending order).

```python
def insertion_sort_biggest_first(arr):
    # Write your code here
    pass

numbers = [5, 1, 4, 2, 8]
print(insertion_sort_biggest_first(numbers))
# Should print: [8, 5, 4, 2, 1]
```

---

### Part 6: Questions

1. If a list has 5 items and is already sorted, how many times will the while loop run?

2. If a list has 5 items in reverse order (biggest to smallest), how many times will the while loop run in total?

3. Why do we start the loop at index 1 instead of index 0?

---

## Homework

Complete these problems at home. Show your work.

---

### Problem 1: Trace the Algorithm

Sort this list step by step. Write down what the list looks like after each item is placed.

`[7, 4, 1, 8, 3, 6]`

Starting state: `[7, 4, 1, 8, 3, 6]`

After placing 4: ___________________

After placing 1: ___________________

After placing 8: ___________________

After placing 3: ___________________

After placing 6: ___________________

Final sorted list: ___________________

---

### Problem 2: Write the Code from Memory

Write the insertion sort function from memory. Do not look at your notes.

```python
def insertion_sort(arr):

    # Your code here

    return arr
```

---

### Problem 3: Sort These Lists

Run your insertion sort function on these lists. Write the sorted result.

List A: `[15, 3, 9, 1, 12]`
Sorted: ___________________

List B: `[100, 50, 75, 25, 60]`
Sorted: ___________________

List C: `["mango", "apple", "grape", "banana"]`
Sorted: ___________________

---

### Problem 4: Trace This List

This list is almost sorted. Trace through insertion sort and count how many times the while loop runs.

`[1, 2, 4, 3, 5]`

- After placing 2: Did the while loop run? _________
- After placing 4: Did the while loop run? _________
- After placing 3: Did the while loop run? _________ How many times? _________
- After placing 5: Did the while loop run? _________

Total times while loop ran: _________

---

### Problem 5: Write the Code for Descending Order

Write a function that sorts from biggest to smallest.

```python
def insertion_sort_biggest_first(arr):

    # Your code here

    return arr

# Test it
print(insertion_sort_biggest_first([10, 2, 8, 4, 6]))
# Should print: [10, 8, 6, 4, 2]
```

---

### Problem 6: Explain in Your Own Words

Answer each question in 2-3 sentences.

1. What is the "key" in insertion sort? Why do we need it?

   _________________________________

   _________________________________

   _________________________________

2. What does the while loop do? When does it stop?

   _________________________________

   _________________________________

   _________________________________

3. Why is insertion sort slow for large lists?

   _________________________________

   _________________________________

   _________________________________

---

### Problem 7: Trace a Different List

Sort this list and write the state after each pass.

`[9, 7, 5, 3, 1]`

After placing 7: ___________________

After placing 5: ___________________

After placing 3: ___________________

After placing 1: ___________________

How many total comparisons did you make? _________

---


