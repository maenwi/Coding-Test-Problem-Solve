import sys
from itertools import combinations

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

input = sys.stdin.readline

N = int(input())
numberss = [list(map(int, input().split())) for _ in range(N)]

for numbers in numberss:
    max_gcd = -1
    
    for a, b in combinations(numbers, 2):
        gcd = find_gcd(a, b)
        if gcd >= max_gcd:
            max_gcd = gcd
    
    print(max_gcd)
