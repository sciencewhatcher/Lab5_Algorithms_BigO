# EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH (search in a rotated sorted list)
from config import *

print("=== STUDENT-SPECIFIC INPUTS ===")
show_inputs()

# ---- DATA GENERATION ----------------------------------------------------
N = 15 + NAME_LENGTH                         # number of incident records
START = 1000 + ID_SUM                        # first incident number
STEP = SEED_DIGIT % 5 + 2                    # gap between incident numbers
original = [START + i * STEP for i in range(N)]          # unique, ascending

# Rotation point from SEED_DIGIT (+3 so it is never 0, even when SEED_DIGIT = 0)
ROTATION = (SEED_DIGIT * 2 + 3) % N
rotated = original[ROTATION:] + original[:ROTATION]      # front block moved to end

# Target from ID_SUM and ARTIST_SUM
TARGET = START + (ID_SUM + ARTIST_SUM) % (N * STEP)
MISSING = original[-1] + 1                   # guaranteed-absent target for testing

# ---- ALGORITHMS ---------------------------------------------------------
def linear_search(data, target):
    comparisons = 0
    for i, value in enumerate(data):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons

def rotated_binary_search(data, target):
    """O(log n): at each step one half is sorted; decide which half to keep."""
    low, high, comparisons = 0, len(data) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if data[mid] == target:
            return mid, comparisons
        comparisons += 1
        if data[low] <= data[mid]:                  # left half is sorted
            comparisons += 1
            if data[low] <= target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                                       # right half is sorted
            comparisons += 1
            if data[mid] < target <= data[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1, comparisons

# ---- RUN ----------------------------------------------------------------
print("\n=== GENERATED DATA ===")
print("Number of records :", N)
print("Original dataset  :", original)
print("Rotation point    :", ROTATION, "(first", ROTATION, "records moved to the end)")
print("Rotated dataset   :", rotated)
print("Target incident   :", TARGET)

print("\n=== SEARCH RESULTS ===")
for label, t in [("Target (from rule)", TARGET), ("Missing record test", MISSING)]:
    bi, bc = rotated_binary_search(rotated, t)
    li, lc = linear_search(rotated, t)
    status = f"found at index {bi}" if bi != -1 else "NOT FOUND"
    print(f"{label}: {t} -> {status}")
    print(f"  Rotated Binary Search comparisons: {bc}")
    print(f"  Linear Search comparisons        : {lc}")
    print(f"  Comparisons saved                : {lc - bc}")
    assert bi == li, "search results disagree"

# Verify every record can be found
assert all(rotated[rotated_binary_search(rotated, v)[0]] == v for v in original)
print("\nVerification: all", N, "records located correctly.")

print("\n=== COMPLEXITY ===")
print("Rotated Binary Search : Time O(log n), Space O(1)")
print("Linear Search         : Time O(n),     Space O(1)")
print("Best case  : O(1) (target at first midpoint)")
print("Worst case : O(log n) binary vs O(n) linear")

print("\n=== FINAL OUTPUT ===")
bi, bc = rotated_binary_search(rotated, TARGET)
li, lc = linear_search(rotated, TARGET)
print(f"Incident {TARGET}: index {bi if bi != -1 else 'not found'} | "
      f"binary={bc} comparisons | linear={lc} comparisons")