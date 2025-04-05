# 0 0 3 4
    # 3 1 0 0 -> Temp
# 5 0 0 7
# _ _ _ 28
# _ _ 21 28
# 20 _ 21 28
def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def find_lcm(a, b, gcd = None):
    if b > a:
        a, b = b, a
    
    if gcd is None:
        gcd = find_gcd(a, b)

    return int(a * b / gcd)

from collections import deque

N = int(input())
prev = [0] * N
temps = deque()

for i in range(N - 1):
    a, b, p, q = map(int, input().split())

    gcd = find_gcd(p, q)
    p //= gcd
    q //= gcd

    # 첫 입력
    if i == 0:
        prev[a] = p
        prev[b] = q
        continue
    
    # 이번에 입력 받은거가, 전에 입력받은 것과 일치하는 위치가 없음
    if prev[a] == 0 and prev[b] == 0:
        temps.append([a, b, p, q])
        continue

    if prev[a] != 0:
        lcm = find_lcm(prev[a], p)
        prev = [num * (lcm // prev[a]) for num in prev]
        prev[b] = q * (lcm // p)
    
    elif prev[b] != 0:
        lcm = find_lcm(prev[b], q)
        prev = [num * (lcm // prev[b]) for num in prev]
        prev[a] = p * (lcm // q)

while temps:
    a, b, p, q = temps.popleft()
    # 이번에 입력 받은거가, 전에 입력받은 것과 일치하는 위치가 없음
    if prev[a] == 0 and prev[b] == 0:
        temps.append([a, b, p, q])
        continue

    if prev[a] != 0:
        lcm = find_lcm(prev[a], p)
        prev = [num * (lcm // prev[a]) for num in prev]
        prev[b] = q * (lcm // p)
    
    elif prev[b] != 0:
        lcm = find_lcm(prev[b], q)
        prev = [num * (lcm // prev[b]) for num in prev]
        prev[a] = p * (lcm // q)

last_gcd = prev[0]
for v in prev[1:]:
    last_gcd = find_gcd(last_gcd, v)
prev = [str(val // last_gcd) for val in prev]

print(" ".join(prev))