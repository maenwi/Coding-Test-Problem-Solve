w = [[[1] * 21 for _ in range(21)] for _ in range(21)]

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b and b < c:
                w[a][b][c] = w[a][b][c - 1] + w[a][b - 1][c - 1] - w[a][b - 1][c]
            else:
                w[a][b][c] = w[a - 1][b][c] + w[a - 1][b - 1][c] + w[a - 1][b][c - 1] - w[a - 1][b - 1][c - 1]

answers = []
while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    elif a <= 0 or b <= 0 or c <= 0:
        answers.append(((a, b, c), 1))
    
    elif a > 20 or b > 20 or c > 20:
        answers.append(((a, b, c), w[20][20][20]))

    else:
        answers.append(((a, b, c), w[a][b][c]))

for (a, b, c), val in answers:
    print(f"w({a}, {b}, {c}) = {val}")
