
# APPENDIX 1: EMERGENCY DISPATCH RECORD SEARCH

LAST_NAME = "Pacudan"
STUDENT_ID = "TUPM-26-1859"
FAVORITE_ARTIST = "The 1975"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(
    ord(c.upper()) - ord("A") + 1
    for c in FAVORITE_ARTIST if c.isalpha()
)

# Generate original and rotated datasets
original = [
    ID_SUM + ARTIST_SUM + i * (NAME_LENGTH + 1)
    for i in range(10)
]

rotation = SEED_DIGIT % len(original)
rotated = original[rotation:] + original[:rotation]
target = ID_SUM + ARTIST_SUM


def linear_search(data, target):
    comparisons = 0

    for index, value in enumerate(data):
        comparisons += 1
        if value == target:
            return index, comparisons

    return -1, comparisons


def rotated_binary_search(data, target):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2

        comparisons += 1
        if data[mid] == target:
            return mid, comparisons

        comparisons += 1
        if data[left] <= data[mid]:
            comparisons += 1
            if data[left] <= target < data[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            comparisons += 1
            if data[mid] < target <= data[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1, comparisons


# Perform both searches
linear_index, linear_comparisons = linear_search(
    rotated, target
)

binary_index, binary_comparisons = rotated_binary_search(
    rotated, target
)

# FINAL OUTPUT: ASSESSMENT DATA
print("=" * 55)
print("FINAL OUTPUT: EMERGENCY DISPATCH RECORD SEARCH")
print("=" * 55)

print("Original Dataset:", original)
print("Rotated Dataset:", rotated)
print("Rotation Point:", rotation)
print("Target Incident:", target)

print("\nLinear Search:")
print("Position (0-based):", linear_index)
print("Position (1-based):",
      linear_index + 1 if linear_index != -1 else "Not Found")
print("Comparison Count:", linear_comparisons)

print("\nRotated Binary Search:")
print("Position (0-based):", binary_index)
print("Position (1-based):",
      binary_index + 1 if binary_index != -1 else "Not Found")
print("Comparison Count:", binary_comparisons)

print("\nComparison Summary:")
print("Linear Search Comparisons:", linear_comparisons)
print("Binary Search Comparisons:", binary_comparisons)
print("Fewer Comparisons:",
      "Binary Search" if binary_comparisons < linear_comparisons
      else "Linear Search" if linear_comparisons < binary_comparisons
      else "Equal")

print("\nTime Complexity:")
print("Linear Search: O(n)")
print("Rotated Binary Search: O(log n) average, O(n) worst case")

print("\nAuxiliary Space Complexity:")
print("Linear Search: O(1)")
print("Rotated Binary Search: O(1)")
print("Dataset Storage: O(n)")

print("\nSearch Results Match:", linear_index == binary_index)
print("=" * 55)

