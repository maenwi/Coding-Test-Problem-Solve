import copy

R, C = map(int, input().split())

maps = []
X_location = []

for r in range(R):
    a_row = list(input())
    for c, point in enumerate(a_row):
        if point == "X":
            X_location.append((r, c))
    maps.append(a_row)

maps_after_50 = copy.deepcopy(maps)

for r, c in X_location:
    ocean = 0
    if r - 1 == -1 or maps[r - 1][c] == ".":
        ocean += 1
    if r + 1 == R or maps[r + 1][c] == ".":
        ocean += 1
    if c - 1 == -1 or maps[r][c - 1] == ".":
        ocean += 1
    if c + 1 == C or maps[r][c + 1] == ".":
        ocean += 1

    if ocean >= 3:
        maps_after_50[r][c] = "."

top_boundary = next(i for i in range(R) if "X" in maps_after_50[i])
left_boundary = next(i for i in range(C) if any(row[i] == "X" for row in maps_after_50))
bot_boundary = next(i for i in range(R - 1, -1, -1) if "X" in maps_after_50[i])
right_boundary = next(i for i in range(C - 1, -1, -1) if any(row[i] == "X" for row in maps_after_50))

for r in range(top_boundary, bot_boundary + 1):
    for c in range(left_boundary, right_boundary + 1):
        print(maps_after_50[r][c],end = "")
    print("")