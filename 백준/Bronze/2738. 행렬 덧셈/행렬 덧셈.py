N, M = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

for r in range(N):
    a_row = list(map(int, input().split()))

    for c in range(M):
        mat[r][c] += a_row[c]

for a_row in mat:
    for v in a_row:
        print(v, end = " ")
    print("")
