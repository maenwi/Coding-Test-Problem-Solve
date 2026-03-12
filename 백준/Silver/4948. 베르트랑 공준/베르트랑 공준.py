import sys

input = sys.stdin.readline

primes = [False] + [True] * 246912
for d in range(2, int(246912 ** 0.5) + 1):
    if primes[d]:
        for m in range(d * 2, 246913, d):
            primes[m] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    print(sum(primes[n+1:2*n+1]))
