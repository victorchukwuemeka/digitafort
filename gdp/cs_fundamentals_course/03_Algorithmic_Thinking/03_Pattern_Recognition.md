# Pattern Recognition in Algorithmic Thinking

## What Is Pattern Recognition?

Pattern recognition means **spotting similarities, trends, or rules** that repeat in data.

Your brain does this naturally. If you see `[2, 4, 6, 8, ?]` — you know the next number is `10`. That's pattern recognition.

In computing, we teach machines to do the same thing — but at massive scale and speed.

---

## Why Does It Matter?

| Benefit | Example |
|--------|---------|
| **Simplify problems** | Instead of solving 100 cases, find the pattern and solve once |
| **Predict outcomes** | If a pattern repeats, we can guess what comes next |
| **Find errors** | Unusual patterns often reveal bugs or fraud |
| **Optimize code** | Repeated patterns can be extracted into loops or functions |

---

## Types of Patterns

### 1. Sequence Patterns

The most common type — numbers or items following a **progression**.

```
Arithmetic:  3, 6, 9, 12, 15 → always adding 3
Geometric:   2, 6, 18, 54 → always multiplying by 3
Fibonacci:   0, 1, 1, 2, 3, 5, 8 → each number = sum of previous two
```

**How to detect:**
- Look at **differences** between consecutive items
- If differences are constant → arithmetic pattern
- If differences are changing proportionally → geometric

**Simple check:**
```python
data = [3, 6, 9, 12, 15]
diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
# diffs = [3, 3, 3, 3] → all same → arithmetic pattern
```

**Try it:**
```python
def find_difference(data):
    return [data[i+1] - data[i] for i in range(len(data)-1)]

print(find_difference([2, 4, 6, 8]))      # [2, 2, 2]
print(find_difference([3, 9, 27, 81]))    # [6, 18, 54] → not arithmetic
```

---

### 2. Structural Patterns

These are patterns in **how data is organized**, not what the values are.

```
Palindromes:  "racecar" → same forwards and backwards
Balanced:     [1, 2, 3, 2, 1] → mirrors around center
Nested:       [1, [2, [3]]] → structure repeats at deeper levels
```

**Key insight:** The structure itself carries meaning. A palindrome reads the same both ways — that's the pattern.

**Try it:**
```python
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("madam"))    # True
```

---

### 3. Frequency Patterns

**How often** things appear can reveal a pattern.

```
Text: "cat dog cat bird cat"
       cat → 3 times (most common)
       dog → 1 time
       bird → 1 time
```

**Common frequency distributions:**
- **Uniform** — everything appears equally often
- **Skewed** — a few items dominate (like Zipf's law in language)

**Try it:**
```python
def count_frequency(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

words = "cat dog cat bird cat".split()
print(count_frequency(words))  # {'cat': 3, 'dog': 1, 'bird': 1}
```

---

### 4. Repetition Patterns (Cycles)

Something **repeats in a loop**.

```
[1, 2, 3, 1, 2, 3, 1, 2, 3] → pattern [1, 2, 3] repeats 3 times
Mon, Tue, Wed, Mon, Tue, Wed → weekly cycle
```

**How to detect:**
- Try dividing the sequence by different lengths
- If a segment repeats evenly, you found the cycle

**Try it:**
```python
def find_repeating_pattern(data, pattern_len):
    pattern = data[:pattern_len]
    return pattern * (len(data) // pattern_len) == data

print(find_repeating_pattern([1,2,3,1,2,3,1,2,3], 3))  # True
print(find_repeating_pattern([1,2,3,1,2,3,1,2,4], 3))  # False
```

---

## Real-World Applications

### Stock Price Trends

Moving averages smooth out noise to reveal the underlying trend:

```
Raw prices:  100, 102, 98, 105, 103, 110, 108, 115
             ↓   ↓   ↓   ↓    ↓    ↓    ↓    ↓
Moving avg:     100   101    105      109
```

**Interpretation:**
- Average going **up** → upward trend
- Average going **down** → downward trend
- Flat → sideways/stable

---

### Spam Detection

Spam has recognizable patterns:

```
SPAM signals:
- ALL CAPS: "URGENT!!! ACT NOW!!!"
- Money words: "free money", "you won"
- Excessive punctuation: "!!!!!!!"
- Pressure language: "limited time", "hurry"

LEGITIMATE signals:
- Normal capitalization
- Neutral language
- Few exclamation marks
```

By counting these signals, we can classify emails.

---

### Image Pattern Recognition

Even simple grids reveal patterns:

```
Diagonal:        Symmetry:
· · █ · ·       █ · █
· · · █ ·       · █ ·
· · · · █       █ · █
```

**What to look for:**
- Lines (horizontal, vertical, diagonal)
- Mirror symmetry (left = right, top = bottom)
- Repeated shapes

---

### Text Pattern Matching (Regex)

Regular expressions find patterns in text:

```
Email:    user@domain.com    → has @ and .
Phone:    555-123-4567       → 3 digits, dash, 3 digits, dash, 4 digits
URL:      https://site.com  → starts with http, has ://
```

Regex gives us a **language to describe patterns** concisely.

---

## Pattern Recognition in Machine Learning

ML is essentially **automated pattern recognition**.

```
Training data:
  Apple:  weight=150g, sweet=yes
  Orange: weight=200g, sweet=no

New fruit: weight=155g, sweet=yes → probably an apple!
```

The algorithm learns the pattern from examples, then applies it to new data.

---

## Step-by-Step Approach

When facing data, ask yourself:

1. **Look at the values** — Do they increase, decrease, or stay steady?
2. **Check differences** — Are they constant (arithmetic) or proportional (geometric)?
3. **Count frequencies** — What appears most often?
4. **Find repetitions** — Does anything cycle?
5. **Check structure** — Is it symmetric, nested, or hierarchical?
6. **Test your pattern** — Does it hold for all data, or just part of it?

---

## Exercises

### Exercise 1: Detect Arithmetic Pattern

Write a function that checks if a list is an arithmetic sequence.

```python
def is_arithmetic(data):
    # your code here
    pass

print(is_arithmetic([5, 10, 15, 20]))  # True
print(is_arithmetic([5, 10, 15, 22]))  # False
```

<details><summary>Solution</summary>

```python
def is_arithmetic(data):
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    return len(set(diffs)) == 1
```

</details>

---

### Exercise 2: Count Vowels

Count how many vowels appear in a string.

```python
def count_vowels(text):
    # your code here
    pass

print(count_vowels("hello world"))  # 3
```

<details><summary>Solution</summary>

```python
def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")
```

</details>

---

### Exercise 3: Find the Next Number

Complete the function that finds the next number in an arithmetic sequence.

```python
def next_number(data):
    # your code here
    pass

print(next_number([2, 4, 6, 8]))  # 10
```

<details><summary>Solution</summary>

```python
def next_number(data):
    diff = data[1] - data[0]
    return data[-1] + diff
```

</details>

---

### Exercise 4: Find Repeating Pattern

Check if a list has a repeating pattern.

```python
def has_pattern(data):
    # your code here
    pass

print(has_pattern([1,2,3,1,2,3]))  # True
print(has_pattern([1,2,3,4,5]))    # False
```

<details><summary>Solution</summary>

```python
def has_pattern(data):
    for length in range(1, len(data)//2 + 1):
        pattern = data[:length]
        if pattern * (len(data)//length) == data:
            return True
    return False
```

</details>

---

## Key Takeaways

| Concept | Remember |
|---------|----------|
| Pattern = similarity | Something that repeats or follows a rule |
| Start simple | Look for basic patterns first |
| Verify | Always check if the pattern holds for ALL data |
| Patterns enable prediction | Identify → Understand → Predict |
| Real patterns have exceptions | No pattern is perfect in the real world |

---

## Practice Problems

**Problem 1:** Find the pattern: `5, 10, 20, 40, 80, ?`
<details><summary>Answer</summary>Multiply by 2 each time → next is 160</details>

**Problem 2:** Is `[1, 3, 5, 7, 9]` arithmetic or geometric?
<details><summary>Answer</summary>Arithmetic — differences are all 2</details>

**Problem 3:** What's the repeating pattern in `A, B, C, A, B, C, A, B, ?`
<details><summary>Answer</summary>Pattern is [A, B, C] → next is C</details>

---

## Further Learning

- **Regular expressions** — powerful pattern matching for text
- **Statistical methods** — for finding patterns in numerical data
- **Machine learning** — automated pattern discovery
- **Time series analysis** — patterns that unfold over time

---

**Bottom line:** Pattern recognition is about training your eye (and your code) to see the structure hiding in data. The better you get at this, the better you become at solving problems efficiently.
