# STUDENT CONFIGURATION  (edit these three lines only)
LAST_NAME = "Gualberto"
STUDENT_ID = "TUPM-26-1130"
FAVORITE_ARTIST = "Amiel Sol"          # <-- CHANGE THIS to your actual favorite artist

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

_letters = [c for c in FAVORITE_ARTIST.upper() if c.isalpha()]
ARTIST_LENGTH = len(_letters)                         # letters only (spaces ignored)
ARTIST_SUM = sum(ord(c) - ord("A") + 1 for c in _letters)   # A=1 ... Z=26

def show_inputs():
    print(f"LAST_NAME       = {LAST_NAME}")
    print(f"STUDENT_ID      = {STUDENT_ID}")
    print(f"FAVORITE_ARTIST = {FAVORITE_ARTIST}")
    print(f"SEED_DIGIT      = {SEED_DIGIT}")
    print(f"ID_SUM          = {ID_SUM}")
    print(f"NAME_LENGTH     = {NAME_LENGTH}")
    print(f"ARTIST_LENGTH   = {ARTIST_LENGTH}")
    print(f"ARTIST_SUM      = {ARTIST_SUM}")