# =============================================================================
# NumPy Course — Runnable Examples
# =============================================================================
# To run this example:
#   1. Install numpy: pip install numpy
#   2. Run the script: python numpy_examples.py
#
# This script covers all the topics from the README.md with practical,
# runnable examples. Each section prints its output so you can follow along.
# =============================================================================

import numpy as np

def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

# =============================================================================
# 1. WHAT IS NUMPY — Creating Arrays from Lists
# =============================================================================
section("1. What is NumPy — Creating Arrays")

arr = np.array([1, 2, 3, 4, 5, 6])
print("1D array:", arr)
print("Type:", type(arr))

# 2D array from nested list
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("\n2D array:")
print(matrix)


# =============================================================================
# 2. UNDERSTANDING ARRAYS — Attributes
# =============================================================================
section("2. Array Attributes")

print("shape  :", arr.shape)    # (6,)
print("ndim   :", arr.ndim)     # 1
print("size   :", arr.size)     # 6
print("dtype  :", arr.dtype)    # int64

print("\n--- 2D array attributes ---")
print("shape  :", matrix.shape)  # (2, 3)
print("ndim   :", matrix.ndim)   # 2


# =============================================================================
# 3. CREATING ARRAYS — Factory Functions
# =============================================================================
section("3. Creating Arrays (Factory Functions)")

zeros = np.zeros((2, 3))
print("zeros((2,3)):\n", zeros)

ones = np.ones((2, 2))
print("\nones((2,2)):\n", ones)

identity = np.eye(3)
print("\neye(3):\n", identity)

sequence = np.arange(0, 10, 2)
print("\narange(0, 10, 2):", sequence)

evenly = np.linspace(0, 1, 5)
print("linspace(0, 1, 5):", evenly)

random_arr = np.random.rand(2, 3)
print("\nrand(2,3) uniform [0,1):\n", random_arr)

random_int = np.random.randint(1, 100, size=(2, 4))
print("\nrandint(1, 100, (2,4)):\n", random_int)

full = np.full((3, 3), 7)
print("\nfull((3,3), 7):\n", full)


# =============================================================================
# 4. INDEXING AND SLICING
# =============================================================================
section("4. Indexing and Slicing")

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Full array:\n", arr_2d)
print("\narr[0, 1]       :", arr_2d[0, 1])      # 2
print("arr[1]          :", arr_2d[1])             # [4 5 6]
print("arr[:, 1]       :", arr_2d[:, 1])          # [2 5 8]
print("arr[0:2, :2]    :\n", arr_2d[0:2, :2])   # [[1,2],[4,5]]

# Negative indexing
print("\narr[-1]         :", arr_2d[-1])           # [7 8 9]
print("arr[-1, -1]     :", arr_2d[-1, -1])        # 9

# Boolean indexing
mask = arr_2d > 5
print("\narr > 5 mask:\n", mask)
print("arr[arr > 5]    :", arr_2d[arr_2d > 5])   # [6 7 8 9]

# Fancy indexing
rows = np.array([0, 2])
cols = np.array([1, 2])
print("arr[[0,2], [1,2]]:", arr_2d[rows, cols])   # [2 9]


# =============================================================================
# 5. VECTORIZED OPERATIONS
# =============================================================================
section("5. Vectorized Operations")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b  =", a + b)       # [5, 7, 9]
print("a * b  =", a * b)       # [4, 10, 18]
print("a ** 2 =", a ** 2)      # [1, 4, 9]
print("a / b  =", a / b)       # [0.25, 0.4, 0.5]
print("a - b  =", a - b)       # [-3, -3, -3]

print("\nsqrt(a)  =", np.sqrt(a))
print("log(a)   =", np.log(a))
print("exp(a)   =", np.exp(a))
print("dot(a,b) =", np.dot(a, b))  # 32

# Comparison — Python loop vs NumPy
python_list = list(range(1_000_000))
np_arr = np.arange(1_000_000)

import time
start = time.time()
_ = [x ** 2 for x in python_list]
python_time = time.time() - start

start = time.time()
_ = np_arr ** 2
numpy_time = time.time() - start

print(f"\nSquared 1M elements — Python loop: {python_time:.4f}s | NumPy: {numpy_time:.6f}s")
print(f"NumPy is ~{python_time / numpy_time:.0f}x faster")


# =============================================================================
# 6. STATISTICAL OPERATIONS
# =============================================================================
section("6. Statistical Operations")

data = np.array([14, 18, 22, 15, 30, 25, 19, 17])

print("data   :", data)
print("sum    :", data.sum())
print("mean   :", data.mean())
print("std    :", round(data.std(), 4))
print("var    :", round(data.var(), 4))
print("min    :", data.min())
print("max    :", data.max())
print("argmin :", data.argmin())  # index of min
print("argmax :", data.argmax())  # index of max
print("median :", np.median(data))
print("percentile(25):", np.percentile(data, 25))
print("percentile(75):", np.percentile(data, 75))

# Axis-wise operations on 2D
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print("\nmatrix:\n", m)
print("sum(axis=0) [cols]  :", m.sum(axis=0))   # [5, 7, 9]
print("sum(axis=1) [rows]  :", m.sum(axis=1))   # [6, 15]
print("mean(axis=0) [cols] :", m.mean(axis=0))  # [2.5, 3.5, 4.5]


# =============================================================================
# 7. BROADCASTING
# =============================================================================
section("7. Broadcasting")

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original:\n", arr)

# Scalar broadcasting
print("\narr + 10:\n", arr + 10)

# 1D array broadcasting across rows
row = np.array([10, 20, 30])
print("\narr + [10,20,30]:\n", arr + row)

# 1D array broadcasting down columns
col = np.array([100, 200]).reshape(2, 1)
print("\narr + [[100],[200]]:\n", arr + col)

# Practical example: normalize columns
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
print("\nOriginal matrix:\n", matrix)
col_means = matrix.mean(axis=0)
col_stds = matrix.std(axis=0)
normalized = (matrix - col_means) / col_stds
print("Column-normalized:\n", np.round(normalized, 2))


# =============================================================================
# 8. RESHAPING
# =============================================================================
section("8. Reshaping")

arr = np.arange(12)
print("Original (arange(12)):", arr)

reshaped = arr.reshape(3, 4)
print("\nreshape(3,4):\n", reshaped)

# -1 inference
print("\nreshape(4,-1):\n", arr.reshape(4, -1))
print("reshape(-1,3):\n", arr.reshape(-1, 3))

# flatten vs ravel
print("\nflatten():", reshaped.flatten())  # returns copy
print("ravel()  :", reshaped.ravel())      # returns view

# Transpose
print("\nTranspose:\n", reshaped.T)
print("reshape(4,3).T shape:", arr.reshape(4, 3).T.shape)


# =============================================================================
# 9. STACKING ARRAYS
# =============================================================================
section("9. Stacking Arrays")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a, "  b:", b)
print("\nhstack:", np.hstack([a, b]))        # [1,2,3,4,5,6]
print("vstack:\n", np.vstack([a, b]))       # 2D vertical stack

# Column stack (makes 2D from 1D)
print("\ncolumn_stack:\n", np.column_stack([a, b]))

# concatenate along axis
c = np.array([[7, 8, 9, 10]])
print("\nconcatenate axis=0:\n", np.concatenate([reshaped, c], axis=0))
print("concatenate axis=1:\n", np.concatenate([np.zeros((3,1)), reshaped], axis=1))


# =============================================================================
# 10. LINEAR ALGEBRA
# =============================================================================
section("10. Linear Algebra")

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("A:\n", A)
print("B:\n", B)

print("\nA @ B (matmul):\n", A @ B)
print("np.dot(A,B):\n", np.dot(A, B))

print("\nnp.linalg.inv(A):\n", np.linalg.inv(A))
print("det(A):", np.linalg.det(A))

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues :", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Solve linear system: Ax = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print("\nSolve Ax=[5,11]: x =", x)
print("Verify A@x:", A @ x)

# SVD
U, S, Vt = np.linalg.svd(A)
print("\nSVD of A:")
print("  U:\n", U)
print("  S:", S)
print("  Vt:\n", Vt)


# =============================================================================
# 11. RANDOM NUMBERS
# =============================================================================
section("11. Random Numbers")

# Set seed for reproducibility
np.random.seed(42)

print("rand(3)        :", np.random.rand(3))
print("randn(3)       :", np.random.randn(3))
print("randint(0,10,5):", np.random.randint(0, 10, size=5))

# Random choices and shuffling
fruits = np.array(["apple", "banana", "cherry", "date"])
print("\nrandom choice   :", np.random.choice(fruits, size=3))
print("random choice p :", np.random.choice(fruits, size=5, p=[0.5, 0.2, 0.2, 0.1]))

shuffled = fruits.copy()
np.random.shuffle(shuffled)
print("shuffled        :", shuffled)

# Normal distribution
samples = np.random.normal(loc=100, scale=15, size=10000)
print(f"\nNormal(μ=100, σ=15) — mean: {samples.mean():.2f}, std: {samples.std():.2f}")


# =============================================================================
# 12. BOOLEAN AND LOGICAL OPERATIONS
# =============================================================================
section("12. Boolean & Logical Operations")

arr = np.array([1, 5, 10, 15, 20, 25, 30])

print("arr:", arr)
print("arr > 10        :", arr > 10)
print("np.all(arr > 0) :", np.all(arr > 0))
print("np.any(arr > 25):", np.any(arr > 25))
print("np.sum(arr > 10):", np.sum(arr > 10), "elements > 10")

# Logical operators
print("\n(arr > 5) & (arr < 20):", (arr > 5) & (arr < 20))
print("np.logical_and       :", np.logical_and(arr > 5, arr < 20))
print("np.where(arr>15, 'big', 'small'):", np.where(arr > 15, "big", "small"))

# Count elements meeting condition
print(f"\nElements between 10 and 25: {np.sum((arr >= 10) & (arr <= 25))}")


# =============================================================================
# 13. COPYING ARRAYS
# =============================================================================
section("13. Copying Arrays (Views vs Copies)")

original = np.array([1, 2, 3, 4, 5])

# View — shares memory with original
view = original.view()
view[0] = 99
print("After view[0] = 99:")
print("  original:", original)   # [99, 2, 3, 4, 5] — MODIFIED!
print("  view    :", view)
print("  Shares memory:", np.shares_memory(original, view))

# Copy — independent
original2 = np.array([1, 2, 3, 4, 5])
copy_arr = original2.copy()
copy_arr[0] = 99
print("\nAfter copy[0] = 99:")
print("  original:", original2)  # [1, 2, 3, 4, 5] — unchanged
print("  copy    :", copy_arr)
print("  Shares memory:", np.shares_memory(original2, copy_arr))


# =============================================================================
# 14. USEFUL NUMPY TRICKS
# =============================================================================
section("14. Useful NumPy Tricks")

# np.where — conditional selection
arr = np.array([10, 20, 30, 40, 50])
result = np.where(arr > 25, arr, 0)
print("np.where(arr>25, arr, 0):", result)

# np.unique
data = np.array([1, 3, 2, 3, 1, 3, 2, 4, 1])
print("\nnp.unique:", np.unique(data))
unique, counts = np.unique(data, return_counts=True)
print("unique + counts:", dict(zip(unique, counts)))

# np.bincount — count occurrences of each non-negative int
labels = np.array([0, 1, 1, 2, 2, 2, 3])
print("bincount:", np.bincount(labels))

# np.sort and np.argsort
unsorted = np.array([40, 10, 30, 20, 50])
print("\nnp.sort:", np.sort(unsorted))
print("argsort:", np.argsort(unsorted))   # indices that would sort it
print("sorted  :", unsorted[np.argsort(unsorted)])

# np.clip
print("\nclip(10,30):", np.clip(unsorted, 10, 30))

# np.linspace for evenly spaced
print("linspace(0, 100, 6):", np.linspace(0, 100, 6))

# Meshgrid — useful for plotting
x = np.array([0, 1, 2])
y = np.array([0, 1])
xx, yy = np.meshgrid(x, y)
print("\nmeshgrid x:\n", xx)
print("meshgrid y:\n", yy)


# =============================================================================
# 15. PRACTICAL EXAMPLES
# =============================================================================
section("15. Practical Examples")

# --- Student grades ---
np.random.seed(0)
n_students = 5
subjects = ["Math", "Science", "English"]
grades = np.random.randint(50, 100, size=(n_students, len(subjects)))
student_names = np.array(["Alice", "Bob", "Charlie", "Diana", "Eve"])

print("Student Grades:")
print("        ", "  ".join(subjects))
for i, name in enumerate(student_names):
    print(f"  {name:8s}", "  ".join(f"{g:3d}" for g in grades[i]))

print(f"\nClass average per subject : {grades.mean(axis=0)}")
print(f"Class average per student : {grades.mean(axis=1)}")
print(f"Best student: {student_names[grades.mean(axis=1).argmax()]}")

# --- Simulate dice rolls ---
rolls = np.random.randint(1, 7, size=(10000, 2))
sums = rolls.sum(axis=1)
print(f"\nDice: rolled 2 dice 10,000 times")
for s in range(2, 13):
    pct = np.sum(sums == s) / len(sums) * 100
    bar = "#" * int(pct)
    print(f"  Sum {s:2d}: {pct:5.1f}% {bar}")

# --- Moving average ---
signal = np.sin(np.linspace(0, 4 * np.pi, 100)) + np.random.normal(0, 0.2, 100)
window = 5
moving_avg = np.convolve(signal, np.ones(window) / window, mode="valid")
print(f"\nSignal length: {len(signal)}")
print(f"Moving average (window={window}) length: {len(moving_avg)}")
print(f"Original first 5: {np.round(signal[:5], 2)}")
print(f"Smoothed first 5: {np.round(moving_avg[:5], 2)}")


# =============================================================================
# Done
# =============================================================================
print(f"\n{'='*60}")
print("  All NumPy examples completed!")
print(f"{'='*60}")
