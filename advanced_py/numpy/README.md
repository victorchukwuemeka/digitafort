# NumPy — Numerical Computing in Python

## 1. What is NumPy?
NumPy is the fundamental library for numerical computing in Python. Its core feature is the **ndarray** — a fast, memory-efficient array that stores elements of the same type in contiguous memory. This makes NumPy 10-100x faster than Python lists because operations run in C, not Python loops.

```python
import numpy as np

# Create an array from a list
arr = np.array([1, 2, 3, 4, 5, 6])
```

## 2. Understanding Arrays
An array has attributes that describe its shape and contents. Let's inspect ours:

```python
print(arr.shape)   # (6,) — 1D with 6 elements
print(arr.ndim)    # 1 — one dimension
print(arr.size)    # 6 — total elements
print(arr.dtype)   # int64 — data type
```

We can also create 2D arrays (matrices) using nested lists:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix.shape)  # (2, 3) — 2 rows, 3 columns
print(matrix.ndim)   # 2
```

## 3. Creating Arrays
NumPy provides many ways to create arrays without typing data manually:

```python
zeros = np.zeros((2, 3))      # [[0., 0., 0.], [0., 0., 0.]]
ones = np.ones((2, 2))        # [[1., 1.], [1., 1.]]
identity = np.eye(3)          # 3x3 identity matrix
sequence = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
evenly = np.linspace(0, 1, 5)   # [0., 0.25, 0.5, 0.75, 1.]
random = np.random.rand(2, 3)   # 2x3 uniform random [0, 1)
```

`arange` is like Python's `range()` but returns an array. `linspace` creates evenly spaced numbers between a start and end — useful for plotting.

## 4. Indexing and Slicing
Indexing works like Python lists but extends to multiple dimensions:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr[0, 1])     # 2 — row 0, column 1
print(arr[1])        # [4, 5, 6] — entire row 1
print(arr[:, 1])     # [2, 5, 8] — all rows, column 1
print(arr[0:2, :2])  # [[1, 2], [4, 5]] — submatrix
```

Boolean indexing is especially powerful — it selects elements based on a condition:

```python
mask = arr > 5
print(mask)
# [[False False False]
#  [False False  True]
#  [ True  True  True]]

print(arr[mask])  # [6, 7, 8, 9]
print(arr[arr > 5])  # same — one line
```

## 5. Vectorized Operations
The biggest advantage of NumPy: operations apply to every element at once. No loops needed.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)     # [5, 7, 9] — element-wise addition
print(a * b)     # [4, 10, 18] — element-wise multiplication
print(a ** 2)    # [1, 4, 9]
print(np.sqrt(a))  # [1., 1.41, 1.73]
print(np.dot(a, b))  # 32 — dot product (1*4 + 2*5 + 3*6)
```

Statistical operations are also vectorized:

```python
print(a.sum())   # 6
print(a.mean())  # 2.0
print(a.max())   # 3
print(a.std())   # 0.816
```

## 6. Broadcasting
Broadcasting allows operations between arrays of different shapes. NumPy automatically expands the smaller array to match.

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Scalar broadcasting — adds 10 to every element
print(arr + 10)
# [[11, 12, 13],
#  [14, 15, 16]]

# 1D array broadcasting — adds across rows
row = np.array([10, 20, 30])
print(arr + row)
# [[11, 22, 33],
#  [14, 25, 36]]
```

Without broadcasting, you'd need nested loops. With broadcasting, it's one line and fast.

## 7. Reshaping
You can change an array's shape without changing its data:

```python
arr = np.arange(12)  # [0, 1, 2, ..., 11]

reshaped = arr.reshape(3, 4)
print(reshaped)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]

# -1 tells NumPy to infer the dimension
print(arr.reshape(4, -1))  # (4, 3)

# flatten() creates a 1D copy; ravel() creates a 1D view (faster)
```

## 8. Stacking Arrays
Combine multiple arrays into one:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack([a, b]))  # [1, 2, 3, 4, 5, 6] — side by side
print(np.vstack([a, b]))  # [[1,2,3],[4,5,6]] — stacked vertically
```

## 9. Linear Algebra
NumPy has a full linear algebra module:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)             # matrix multiplication (Python 3.5+)
print(np.linalg.inv(A))  # [[-2., 1.], [1.5, -0.5]] — inverse
print(np.linalg.det(A))  # -2.0 — determinant
```

## 10. Saving and Loading Arrays
```python
np.save("array.npy", arr)
loaded = np.load("array.npy")

np.savetxt("data.csv", reshaped, delimiter=",")
loaded_csv = np.loadtxt("data.csv", delimiter=",")
```

NumPy is the foundation for Pandas, SciPy, and scikit-learn. Everything you learn here applies directly to those libraries.
