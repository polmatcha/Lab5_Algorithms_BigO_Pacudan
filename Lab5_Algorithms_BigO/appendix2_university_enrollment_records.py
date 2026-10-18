# APPENDIX 2: UNIVERSITY ENROLLMENT RECORDS
LAST_NAME = "Pacudan"
STUDENT_ID = "TUPM-26-1859"
FAVORITE_ARTIST = "The 1975"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

dataset_a = [SEED_DIGIT + ID_SUM + i * 2 for i in range(5)]
dataset_b = [ARTIST_LENGTH + NAME_LENGTH + i * 3 for i in range(5)]

def merge_sorted(a, b):
    i = j = comparisons = 0
    merged = []
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, comparisons

merged, comparisons = merge_sorted(dataset_a, dataset_b)
print("Department A Dataset:", dataset_a)
print("Department B Dataset:", dataset_b)
print("Consolidated Dataset:", merged)
print("Records Before Consolidation:", len(dataset_a) + len(dataset_b))
print("Records After Consolidation:", len(merged))
print("Comparison Count:", comparisons)
print("Sorted Correctly:", merged == sorted(merged))
print("Time Complexity: O(n + m)")
print("Auxiliary Space Complexity: O(n + m)")
