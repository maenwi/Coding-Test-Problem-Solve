import sys

input = sys.stdin.readline

a, d = map(int, input().split())
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def range_sum(a, d, l, r):
    if l == r:
        return a + (l - 1) * d
    
    first = a + (l - 1) * d
    last = a + (r - 1) * d
    return (first + last) * (r - l + 1) // 2

def range_gcd(a, d, l, r):
    if l == r:
        return a + (l - 1) * d
    return find_gcd(a, d)
    
for query, l, r in queries:
    if query == 1:
        print(range_sum(a, d, l, r))

    else:
        print(range_gcd(a, d, l, r))
