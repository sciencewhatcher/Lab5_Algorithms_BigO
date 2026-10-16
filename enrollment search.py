# EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS (merge two sorted lists)
from config import *

print("=== STUDENT-SPECIFIC INPUTS ===")
show_inputs()

# ---- DATA GENERATION ----------------------------------------------------
SIZE_A = 8 + SEED_DIGIT % 5                  # Department A record count
SIZE_B = 6 + ARTIST_LENGTH % 5               # Department B record count

# Dataset A: ascending, from SEED_DIGIT and ID_SUM
dept_a = [2000 + ID_SUM + i * (SEED_DIGIT + 3) for i in range(SIZE_A)]
# Dataset B: ascending, from ARTIST_LENGTH and NAME_LENGTH
dept_b = [2000 + NAME_LENGTH + i * ARTIST_LENGTH for i in range(SIZE_B)]

# ---- ALGORITHM ----------------------------------------------------------
def merge_sorted(a, b):
    merged, i, j, comparisons = [], 0, 0, 0
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])        # leftovers need no comparisons
    merged.extend(b[j:])
    return merged, comparisons

# ---- RUN ----------------------------------------------------------------
print("\n=== GENERATED DATA ===")
print("Department A dataset:", dept_a)
print("Department B dataset:", dept_b)

merged, comps = merge_sorted(dept_a, dept_b)

print("\n=== MERGE RESULT ===")
print("Consolidated dataset:", merged)
print("Records before consolidation:", len(dept_a), "+", len(dept_b), "=", len(dept_a) + len(dept_b))
print("Records after consolidation :", len(merged))
print("Comparison count            :", comps,
      f"(best case min(m,n)={min(len(dept_a), len(dept_b))}, worst case m+n-1={len(merged) - 1})")

print("\n=== VERIFICATION ===")
is_ordered = all(merged[k] <= merged[k + 1] for k in range(len(merged) - 1))
same_records = sorted(dept_a + dept_b) == merged
count_ok = len(merged) == len(dept_a) + len(dept_b)
print("Ascending order       :", "PASS" if is_ordered else "FAIL")
print("No records lost/added :", "PASS" if same_records and count_ok else "FAIL")
dups = len(merged) - len(set(merged))
print("Duplicate IDs found   :", dups, "(kept; a student enrolled in both departments)" if dups else "")

print("\n=== COMPLEXITY ===")
print("Time : O(m + n)  - each element is placed once")
print("Space: O(m + n)  - new list holds all records")

print("\n=== FINAL OUTPUT ===")
print(f"{len(dept_a)} + {len(dept_b)} records merged into {len(merged)} "
      f"ordered records using {comps} comparisons.")