import sys

input = sys.stdin.readline

T = int(input().rstrip())

answer = []
for _ in range(T):
    answer.append(str(sum(map(int, input().rstrip().split()))))

print("\n".join(answer))