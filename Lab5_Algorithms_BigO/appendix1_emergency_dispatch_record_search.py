# APPENDIX 1: EMERGENCY DISPATCH RECORD SEARCH
LAST_NAME = "Pacudan"
STUDENT_ID = "TUPM-26-1859"
FAVORITE_ARTIST = "The 1975"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c.upper()) - ord("A") + 1
                 for c in FAVORITE_ARTIST if c.isalpha())

original = [ID_SUM + ARTIST_SUM + i * (NAME_LENGTH + 1)
            for i in range(10)]
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

index, comparisons = linear_search(rotated, target)
print("Original Dataset:", original)
print("Rotated Dataset:", rotated)
print("Rotation Point:", rotation)
print("Target Incident:", target)
print("Target Position (0-based index):", index)
print("Target Position (1-based):", index + 1 if index >= 0 else "Not Found")
print("Linear Search Comparisons:", comparisons)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
