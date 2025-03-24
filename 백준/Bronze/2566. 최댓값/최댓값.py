maximum = -1
max_loc = []
for r in range(9):
    a_row = list(map(int, input().split()))
    for c in range(9):
        if a_row[c] >= maximum:
            maximum = a_row[c]
            max_loc = [str(r + 1), str(c + 1)]

print(maximum)
print(" ".join(max_loc))