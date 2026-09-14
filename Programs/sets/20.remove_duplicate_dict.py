data = [
    {"name": "Rohit", "age": 21},
    {"name": "Aman", "age": 20},
    {"name": "Rohit", "age": 21},
    {"age": 20, "name": "Aman"}
]

unique = []
seen = set()

for item in data:
    key = frozenset(sorted(item.items()))

    if key not in seen:
        seen.add(key)
        unique.append(item)

print(unique)    

print(type(unique))


# [(1,2),(3,4),(2,1),(5,6),(7,8),(6,5)]   home work questions



# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16


# 5 1 2 3
# 9 6 7 4
# 13 10 11 8
# 14 15 16 12

# 13 9  5  1 
# 14 6  7  2
# 15 10 11 3
# 16 12 8  4



# 1 → 2 → 3 → 4
# ↓           ↓
# 5           8
# ↓           ↓
# 9           12
# ↓           ↓
# 13 ←14 ←15 ←16


# Airline Seat Reservation

# Represent seats as a matrix.

# Support:-

# Book Seat
# Cancel Seat
# Show Available Seats
# Show Occupied Seats
# Find Adjacent Seats


# hello world

#  missing letters
# duplicate
# unique

# a to z