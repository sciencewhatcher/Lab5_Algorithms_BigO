# EXERCISE 3: E-COMMERCE ORDER PROCESSING (sorting under different input orders)
import random
import time
from config import *

print("=== STUDENT-SPECIFIC INPUTS ===")
show_inputs()

# ---- DATA GENERATION -----------------------------------------------------
N = 100 + ID_SUM * 10                                   # number of orders
rng = random.Random(SEED_DIGIT * 100 + ID_SUM)          # reproducible per student
orders = list(range(5000 + ID_SUM, 5000 + ID_SUM + N))  # unique order numbers
random_orders = orders.copy()
rng.shuffle(random_orders)

conditions = {
    "Sorted":  orders.copy(),
    "Reverse": orders[::-1],
    "Random":  random_orders,
}

# ---- ALGORITHMS (return sorted list, comparisons, movements) ------------
def bubble_sort(data):
    a, comps, moves = data.copy(), 0, 0
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                moves += 1
                swapped = True
        if not swapped:
            break
    return a, comps, moves

def selection_sort(data):
    a, comps, moves = data.copy(), 0, 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            comps += 1
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            moves += 1
    return a, comps, moves

def insertion_sort(data):
    a, comps, moves = data.copy(), 0, 0
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0:
            comps += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            moves += 1
            j -= 1
        a[j + 1] = key
    return a, comps, moves

def measure(func, data, trials=5):
    total = 0.0
    for _ in range(trials):
        start = time.perf_counter()
        result = func(data)
        total += time.perf_counter() - start
    return result, total / trials

algorithms = [("Bubble Sort", bubble_sort),
              ("Selection Sort", selection_sort),
              ("Insertion Sort", insertion_sort)]

# ---- RUN ----------------------------------------------------------------
print("\n=== GENERATED ORDER DATASET ===")
print("Number of orders:", N)
for name, data in conditions.items():
    print(f"{name:<8} first 8: {data[:8]} ...")

results = {}   # (condition, algorithm) -> (comps, moves, time)
print("\n=== SORTING RESULTS ===")
for cond, data in conditions.items():
    print(f"\n--- {cond} input (n={N}) ---")
    print(f"{'Algorithm':<16}{'Comparisons':>12}{'Movements':>12}{'Time (s)':>14}{'Verified':>10}")
    for name, func in algorithms:
        (out, comps, moves), elapsed = measure(func, data)
        ok = out == sorted(data)
        results[(cond, name)] = (comps, moves, elapsed)
        print(f"{name:<16}{comps:>12}{moves:>12}{elapsed:>14.8f}{'PASS' if ok else 'FAIL':>10}")
        assert ok

# ---- THEORY CHECK -------------------------------------------------------
pairs = N * (N - 1) // 2
print("\n=== BIG O AND CASE ANALYSIS ===")
print(f"n(n-1)/2 = {pairs}   (n-1 = {N - 1})")
print(f"{'Algorithm':<16}{'Best (Sorted)':<22}{'Average (Random)':<22}{'Worst (Reverse)':<22}")
for name, _ in algorithms:
    row = [f"{results[(c, name)][0]} cmp" for c in ("Sorted", "Random", "Reverse")]
    print(f"{name:<16}{row[0]:<22}{row[1]:<22}{row[2]:<22}")

print("""
Algorithm       Best        Average     Worst       Space
Bubble Sort     O(n)*       O(n^2)      O(n^2)      O(1)
Selection Sort  O(n^2)      O(n^2)      O(n^2)      O(1)
Insertion Sort  O(n)        O(n^2)      O(n^2)      O(1)
(* with the early-exit 'swapped' flag)""")

print("=== OBSERVATIONS ===")
b, s, i = ("Bubble Sort", "Selection Sort", "Insertion Sort")
print(f"- Sorted input: Bubble and Insertion need only {results[('Sorted', b)][0]} comparisons "
      f"(n-1) and 0 movements; Selection still needs {results[('Sorted', s)][0]} (n(n-1)/2).")
print(f"- Reverse input is the worst case: Bubble/Insertion reach {results[('Reverse', b)][0]} "
      f"comparisons and {results[('Reverse', b)][1]} movements (n(n-1)/2).")
print(f"- Selection Sort never exceeds {max(results[(c, s)][1] for c in conditions)} swaps "
      f"(at most n-1), making it best when writes are costly.")
print("- Wall-clock time follows comparisons + movements: on Sorted input Bubble/Insertion do almost no work,")
print("  but on Reverse input Selection Sort is fastest and on Random input it is competitive, because it makes far fewer movements (swaps).")
print("- Insertion Sort halves the comparisons of Bubble Sort on Random input and is adaptive (near-O(n) on nearly sorted data).")
print("- Timings at this size are microseconds, so tiny differences (e.g. on Sorted input) are measurement noise.")

print("\n=== FINAL OUTPUT ===")
for cond in conditions:
    best = min(algorithms, key=lambda a: results[(cond, a[0])][2])[0]
    print(f"{cond:<8} input: fastest = {best}; all three outputs verified sorted.")