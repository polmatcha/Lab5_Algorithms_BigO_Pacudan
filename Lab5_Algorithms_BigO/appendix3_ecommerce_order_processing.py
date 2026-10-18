
# APPENDIX 3: E-COMMERCE ORDER PROCESSING

import random
import time

LAST_NAME = "Pacudan"
STUDENT_ID = "TUPM-26-1859"
FAVORITE_ARTIST = "The 1975"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

orders = [
    (ID_SUM * 3 + i * 7 + SEED_DIGIT) % 1000
    for i in range(12)
]

sorted_orders = sorted(orders)
reverse_orders = sorted(orders, reverse=True)

rng = random.Random(ID_SUM + SEED_DIGIT)
random_orders = orders.copy()
rng.shuffle(random_orders)


def bubble_sort(data):
    a = data.copy()
    comparisons = movements = 0

    for i in range(len(a)):
        swapped = False

        for j in range(len(a) - i - 1):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 1
                swapped = True

        if not swapped:
            break

    return a, comparisons, movements


def selection_sort(data):
    a = data.copy()
    comparisons = movements = 0

    for i in range(len(a) - 1):
        minimum = i

        for j in range(i + 1, len(a)):
            comparisons += 1

            if a[j] < a[minimum]:
                minimum = j

        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            movements += 1

    return a, comparisons, movements


def insertion_sort(data):
    a = data.copy()
    comparisons = movements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] <= key:
                break

            a[j + 1] = a[j]
            movements += 1
            j -= 1

        a[j + 1] = key

    return a, comparisons, movements


algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
]

conditions = [
    ("Sorted", sorted_orders),
    ("Reverse", reverse_orders),
    ("Random", random_orders),
]

# STORE RESULTS FOR THE FINAL SUMMARY
results = []

# ASSESSMENT DATA
print("Original Order Dataset:", orders)

for condition_name, dataset in conditions:
    print("\nInput Condition:", condition_name)
    print("Input:", dataset)

    for name, algorithm in algorithms:
        times = []
        result = None

        for _ in range(5):
            start = time.perf_counter()
            result = algorithm(dataset)
            times.append(time.perf_counter() - start)

        sorted_result, comparisons, movements = result
        average_time = sum(times) / len(times)
        verified = sorted_result == sorted(dataset)

        print("\nAlgorithm:", name)
        print("Sorted Output:", sorted_result)
        print("Comparisons:", comparisons)
        print("Movements:", movements)
        print(f"Average Execution Time: {average_time:.8f} s")
        print("Sorting Verified:", verified)

        results.append({
            "condition": condition_name,
            "algorithm": name,
            "comparisons": comparisons,
            "movements": movements,
            "time": average_time,
            "verified": verified,
        })

print("\nTime Complexity:")
print("Bubble Sort: Best O(n), Average/Worst O(n^2)")
print("Selection Sort: Best/Average/Worst O(n^2)")
print("Insertion Sort: Best O(n), Average/Worst O(n^2)")

# FINAL OUTPUT
print("\n" + "=" * 55)
print("FINAL OUTPUT: E-COMMERCE ORDER PROCESSING")
print("=" * 55)

print("Original Order Dataset:", orders)
print("Total Orders:", len(orders))

print("\nSorting Assessment Summary:")
print("Input Conditions: Sorted, Reverse, Random")
print("Algorithms: Bubble Sort, Selection Sort, Insertion Sort")
print("Total Sorting Tests:", len(results))
print("All Sorting Results Verified:",
      all(result["verified"] for result in results))

for condition_name, _ in conditions:
    condition_results = [
        result for result in results
        if result["condition"] == condition_name
    ]

    fastest = min(condition_results, key=lambda r: r["time"])
    fewest = min(condition_results, key=lambda r: r["comparisons"])

    print(f"\n{condition_name} Input:")
    print("Fastest Measured Algorithm:", fastest["algorithm"])
    print("Fewest Comparisons:", fewest["algorithm"])
    print("Comparison Count:", fewest["comparisons"])

print("\nTime Complexity:")
print("Bubble Sort: Best O(n), Average/Worst O(n^2)")
print("Selection Sort: O(n^2) in all cases")
print("Insertion Sort: Best O(n), Average/Worst O(n^2)")

print("\nConclusion:")
print("Sorting performance varies depending on the algorithm")
print("and the initial order of the data.")

print("=" * 55)
