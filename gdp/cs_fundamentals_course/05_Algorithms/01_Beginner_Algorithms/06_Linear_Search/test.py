# ============================================================
# Linear Search — All Variants
# ============================================================

# --- Variant 1: Basic Linear Search ---
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# --- Variant 2: Sentinel Linear Search ---
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


# --- Variant 3: Recursive Linear Search ---
def recursive_linear_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_linear_search(arr, target, index + 1)


# --- Variant 4: Find All Occurrences ---
def find_all_linear_search(arr, target):
    results = []
    for i in range(len(arr)):
        if arr[i] == target:
            results.append(i)
    return results


# --- Variant 5: Sorted Linear Search with Early Exit ---
def sorted_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            return -1
    return -1


# --- Variant 6: Find Min / Find Max ---
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


# ============================================================
# Tests
# ============================================================

def test_linear_search():
    assert linear_search([10, 5, 20, 15, 30], 20) == 2
    assert linear_search([10, 5, 20, 15, 30], 10) == 0
    assert linear_search([10, 5, 20, 15, 30], 30) == 4
    assert linear_search([10, 5, 20, 15, 30], 100) == -1
    assert linear_search([], 5) == -1
    assert linear_search([7], 7) == 0
    print("  [PASS] Basic Linear Search")


def test_sentinel_search():
    data = [10, 5, 20, 15, 30]
    assert sentinel_search(data, 20) == 2
    assert sentinel_search(data, 10) == 0
    assert sentinel_search(data, 30) == 4
    assert sentinel_search(data, 100) == -1
    # Verify original array is restored
    assert data == [10, 5, 20, 15, 30]

    single = [42]
    assert sentinel_search(single, 42) == 0
    assert sentinel_search(single, 99) == -1
    print("  [PASS] Sentinel Search")


def test_recursive_linear_search():
    assert recursive_linear_search([10, 5, 20, 15, 30], 20) == 2
    assert recursive_linear_search([10, 5, 20, 15, 30], 10) == 0
    assert recursive_linear_search([10, 5, 20, 15, 30], 30) == 4
    assert recursive_linear_search([10, 5, 20, 15, 30], 100) == -1
    assert recursive_linear_search([], 5) == -1
    print("  [PASS] Recursive Linear Search")


def test_find_all_linear_search():
    assert find_all_linear_search([3, 7, 3, 10, 3, 15], 3) == [0, 2, 4]
    assert find_all_linear_search([1, 2, 3, 4, 5], 6) == []
    assert find_all_linear_search([5, 5, 5, 5], 5) == [0, 1, 2, 3]
    assert find_all_linear_search([], 1) == []
    assert find_all_linear_search([1], 1) == [0]
    print("  [PASS] Find All Occurrences")


def test_sorted_linear_search():
    sorted_list = [2, 5, 8, 12, 16, 23, 38]
    assert sorted_linear_search(sorted_list, 12) == 3
    assert sorted_linear_search(sorted_list, 2) == 0
    assert sorted_linear_search(sorted_list, 38) == 6
    assert sorted_linear_search(sorted_list, 10) == -1  # exits early
    assert sorted_linear_search(sorted_list, 1) == -1   # exits at first element
    assert sorted_linear_search([], 5) == -1
    print("  [PASS] Sorted Linear Search (Early Exit)")


def test_find_min_max():
    data = [14, 3, 27, 8, 21]
    assert find_min(data) == 3
    assert find_max(data) == 27

    assert find_min([42]) == 42
    assert find_max([42]) == 42

    assert find_min([-5, -1, -10, 0]) == -10
    assert find_max([-5, -1, -10, 0]) == 0
    print("  [PASS] Find Min / Find Max")


def test_edge_cases():
    # All duplicates
    assert linear_search([9, 9, 9, 9], 9) == 0

    # Single element not found
    assert linear_search([5], 3) == -1

    # Negative numbers
    assert linear_search([-3, -7, -1, -42], -42) == 3

    # Mixed with zeros
    assert linear_search([0, 0, 0, 1], 1) == 3

    print("  [PASS] Edge Cases")


if __name__ == "__main__":
    print("Running Linear Search Tests...\n")
    test_linear_search()
    test_sentinel_search()
    test_recursive_linear_search()
    test_find_all_linear_search()
    test_sorted_linear_search()
    test_find_min_max()
    test_edge_cases()
    print("\nAll tests passed!")
