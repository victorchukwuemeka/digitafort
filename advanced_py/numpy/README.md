# NumPy — Numerical Computing in Python

NumPy is the foundation of every data library in Python. Pandas, scikit-learn, matplotlib — they all sit on top of it. If you learn NumPy well, everything else becomes easier.

```bash
pip install numpy
```

The convention is `import numpy as np`. Everyone does it. Don't be the person who types `import numpy` every time.

---

## 1. Creating Arrays

A Python list holds anything. A NumPy array holds one type, stores it in contiguous memory, and operates on it in C — which makes it 10-100x faster.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)        # [1 2 3 4 5 6]
print(type(arr))  # <class 'numpy.ndarray'>
```

Notice: no commas between printed elements. NumPy prints arrays differently from Python lists.

---

## 2. Array Attributes

Every array carries metadata — shape, dimensions, data type. Learn to read these:

```python
print(arr.shape)   # (6,) — a tuple with one element means 1D
print(arr.ndim)    # 1 — one dimension
print(arr.size)    # 6 — total number of elements
print(arr.dtype)   # int64 — the data type of every element
```

A 2D array (matrix) is just a list of lists:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix.shape)  # (2, 3) — 2 rows, 3 columns
print(matrix.ndim)   # 2
```

`shape` is always `(rows, columns)` for 2D. Read it left to right.

---

## 3. Creating Arrays Without Typing Data

You won't always have data ready. NumPy gives you factory functions:

```python
np.zeros((2, 3))          # 2x3 matrix of 0s
np.ones((3,))             # [1., 1., 1.]
np.eye(3)                 # 3x3 identity matrix (1s on diagonal)
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8] — like range() but returns array
np.linspace(0, 1, 5)      # [0., 0.25, 0.5, 0.75, 1.] — 5 evenly spaced from 0 to 1
np.random.rand(2, 3)      # 2x3 random numbers between 0 and 1
np.random.randint(1, 100, size=(2, 4))  # 2x4 random integers from 1 to 99
```

`arange` = "array range". `linspace` = "linear space" — useful when you need evenly spaced numbers for plotting.

---

## 4. Indexing and Slicing

Works like Python lists, but extends to multiple dimensions with a comma:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr[0, 1])     # 2 — row 0, column 1
print(arr[1])        # [4, 5, 6] — entire row 1
print(arr[:, 1])     # [2, 5, 8] — all rows, column 1
print(arr[0:2, :2])  # [[1, 2], [4, 5]] — first 2 rows, first 2 columns
```

The colon `:` means "everything". `arr[:, 1]` = "all rows, column 1".

**Boolean indexing** is where NumPy gets powerful. Give it a condition, it returns the elements that match:

```python
print(arr[arr > 5])   # [6, 7, 8, 9]
print(arr % 2 == 0)   # [[False  True False]
                       #  [ True False  True]
                       #  [False  True False]]
```

This replaces what would be a loop + if statement in plain Python.

---

## 5. Vectorized Operations

This is the whole point of NumPy. Operations apply to every element at once — no loops:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)     # [5, 7, 9]   — element-wise
print(a * b)     # [4, 10, 18] — element-wise
print(a ** 2)    # [1, 4, 9]   — square every element
print(np.sqrt(a))  # [1., 1.41, 1.73]
print(np.dot(a, b))  # 32 — dot product: 1*4 + 2*5 + 3*6
```

Statistical operations work the same way:

```python
print(a.sum())   # 6
print(a.mean())  # 2.0
print(a.max())   # 3
print(a.std())   # 0.816 — standard deviation
```

For 2D arrays, use `axis` to choose direction:
- `axis=0` = operate down the rows (result per column)
- `axis=1` = operate across the columns (result per row)

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

m.sum(axis=0)   # [5, 7, 9]   — sum of each column
m.sum(axis=1)   # [6, 15]     — sum of each row
m.mean(axis=0)  # [2.5, 3.5, 4.5]
```

---

## 6. Broadcasting

Broadcasting lets you operate on arrays of different shapes. NumPy figures out how to stretch the smaller one automatically:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Scalar → added to every element
arr + 10
# [[11, 12, 13],
#  [14, 15, 16]]

# 1D array → stretched across each row
row = np.array([10, 20, 30])
arr + row
# [[11, 22, 33],
#  [14, 25, 36]]
```

Without broadcasting you'd write nested loops. With it, one line.

---

## 7. Reshaping

Change an array's shape without changing its data:

```python
arr = np.arange(12)  # [0, 1, 2, ..., 11]

arr.reshape(3, 4)    # 3 rows, 4 columns
arr.reshape(4, -1)   # 4 rows, let NumPy figure out columns → (4, 3)
arr.reshape(-1, 3)   # let NumPy figure out rows → (4, 3)
```

The `-1` is a placeholder. You're telling NumPy: "you figure this dimension out."

```python
reshaped = arr.reshape(3, 4)
reshaped.flatten()   # back to 1D — returns a copy
reshaped.ravel()     # back to 1D — returns a view (faster, shares memory)
```

---

## 8. Stacking Arrays

Combine arrays side by side or on top of each other:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.hstack([a, b])   # [1, 2, 3, 4, 5, 6] — horizontal (side by side)
np.vstack([a, b])   # [[1,2,3], [4,5,6]] — vertical (stacked)
```

Think of `hstack` as "glue columns together" and `vstack` as "glue rows together".

---

## 9. Linear Algebra

NumPy has `@` for matrix multiplication and `np.linalg` for everything else:

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

A @ B                  # matrix multiplication — Python 3.5+
np.linalg.inv(A)       # inverse of A
np.linalg.det(A)       # determinant
np.linalg.eig(A)       # eigenvalues and eigenvectors
```

Solving a system of linear equations (`Ax = b`):

```python
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print(A @ x)  # verify: should print [5, 11]
```

---

## 10. Copying: Views vs Copies

This trips up everyone at least once:

```python
original = np.array([1, 2, 3, 4, 5])

# View — shares memory with original
view = original.view()
view[0] = 99
print(original)  # [99, 2, 3, 4, 5] — original changed!

# Copy — independent
copy = original.copy()
copy[0] = 0
print(original)  # [99, 2, 3, 4, 5] — unchanged
```

If you modify a view, you modify the original. Use `.copy()` when you need independence.

---

## 11. Random Numbers

`np.random` gives you everything from coin flips to normal distributions:

```python
np.random.seed(42)   # set seed for reproducibility

np.random.rand(3)              # 3 floats in [0, 1)
np.random.randn(3)             # 3 from standard normal (mean=0, std=1)
np.random.randint(0, 10, 5)    # 5 integers from 0 to 9
np.random.choice(["a", "b", "c"], size=3)  # random picks from a list
```

`seed` makes results reproducible. Same seed = same random numbers, every time.

---

## 12. Useful Tricks

```python
arr = np.array([10, 20, 30, 40, 50])

# np.where — element-wise if/else
np.where(arr > 25, arr, 0)  # [0, 0, 30, 40, 50]

# np.unique — distinct values and their counts
data = np.array([1, 3, 2, 3, 1, 3])
values, counts = np.unique(data, return_counts=True)
# values: [1, 2, 3]  counts: [2, 1, 3]

# np.sort — returns sorted copy
np.sort(arr)           # [10, 20, 30, 40, 50]
np.argsort(arr)        # [0, 1, 2, 3, 4] — indices that would sort it

# np.clip — clamp values to a range
np.clip(arr, 15, 45)  # [15, 20, 30, 40, 45]
```

---

## Saving and Loading

```python
np.save("array.npy", arr)        # save to binary file
arr = np.load("array.npy")       # load it back

np.savetxt("data.csv", arr, delimiter=",")  # save as CSV
arr = np.loadtxt("data.csv", delimiter=",") # load CSV
```

`.npy` is NumPy's native format — fast and preserves dtype. CSV is human-readable but slower.

---

## Common Gotchas

1. **Shape mismatch:** `arr.reshape(3, 4)` on an array with 13 elements → error. Total elements must stay the same.
2. **View vs copy:** Modifying a slice modifies the original. Use `.copy()` when in doubt.
3. **Integer division:** `np.array([1,2,3]) / 2` gives `[0.5, 1., 1.5]`, not `[0, 1, 1]`. Use `//` for floor division.
4. **Broadcasting shape rules:** Arrays must be compatible from the last dimension forward. `(3,4) + (4,)` works. `(3,4) + (3,)` doesn't.
5. **dtype matters:** `np.array([1, 2.5])` creates floats, not ints. Mixing types promotes to the more general type.

---

## What's Next?

- **Data analysis**: Pandas — built on NumPy arrays
- **Visualization**: Matplotlib, Seaborn
- **Machine learning**: scikit-learn — uses NumPy arrays everywhere

---

## Complete Code — Type This in Class

```python
import numpy as np

# 1. Creating arrays
arr = np.array([1, 2, 3, 4, 5, 6])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# 2. Attributes
print(arr.shape, arr.ndim, arr.size, arr.dtype)
print(matrix.shape, matrix.ndim)

# 3. Factory functions
print(np.zeros((2, 3)))
print(np.ones((3,)))
print(np.eye(3))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
print(np.random.randint(1, 100, size=(2, 4)))

# 4. Indexing and slicing
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(arr_2d[0, 1])
print(arr_2d[:, 1])
print(arr_2d[arr_2d > 5])

# 5. Vectorized operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b, a * b, a ** 2)
print(np.dot(a, b))
print(a.mean(), a.std())

# 6. Broadcasting
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr + 10)
print(arr + np.array([10, 20, 30]))

# 7. Reshaping
arr = np.arange(12)
print(arr.reshape(3, 4))
print(arr.reshape(4, -1))

# 8. Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack([a, b]))
print(np.vstack([a, b]))

# 9. Linear algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
print(np.linalg.inv(A))
print(np.linalg.det(A))

# 10. Views vs copies
original = np.array([1, 2, 3])
view = original.view()
view[0] = 99
print("original after view change:", original)  # [99, 2, 3]

copy = original.copy()
copy[0] = 0
print("original after copy change:", original)  # [99, 2, 3] — unchanged

# 11. Random
np.random.seed(42)
print(np.random.randint(0, 10, size=5))

# 12. Useful tricks
arr = np.array([10, 20, 30, 40, 50])
print(np.where(arr > 25, arr, 0))
print(np.clip(arr, 15, 45))
```

*Run `python numpy_examples.py` for the same code with full output printed step by step.*
