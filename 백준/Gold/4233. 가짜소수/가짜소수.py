def a_to_the_p(a, p, mod):
    result = 1
    while p:
        if p % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        p //= 2
    return result

def is_prime(p):
    for d in range(2, int(p ** 0.5) + 1):
        if p % d == 0:
            return False
    return True

answer = []
while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        print("\n".join(answer))
        break
    
    if is_prime(p):
        answer.append("no")
        continue
    
    if a_to_the_p(a, p, p) == a:
        answer.append("yes")
    
    else:
        answer.append("no")