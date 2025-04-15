import sys
input = sys.stdin.readline

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

while True:
    line = input()
    if not line:
        break
    n = int(line.strip())
    if n == 0:
        break

    A = [int(input()) for _ in range(n)]

    result_set = set()
    prev_gcds = set()

    for a in A:
        curr_gcds = {a}
        for g in prev_gcds:
            curr_gcds.add(find_gcd(g, a))
        prev_gcds = curr_gcds
        result_set.update(curr_gcds)

    print(len(result_set))
