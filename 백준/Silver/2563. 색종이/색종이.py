paper = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())

for _ in range(N):
    row, col = map(int, input().split())

    for r in range(row - 1, row + 9):
        for c in range(col - 1, col + 9):
            paper[r][c] = 1

area = 0
for r in range(len(paper)):
    for c in range(len(paper)):
        area += paper[r][c]

print(area)