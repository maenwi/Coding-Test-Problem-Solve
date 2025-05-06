import sys

input = sys.stdin.readline

N = int(input())
d = {k : 1 for k in input().split()}

M = int(input())
for t in input().split():
    print(d.get(t, 0))