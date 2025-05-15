import math

N = int(input())

def find_diviors(n):
    divisors_from_s = []
    divisors_from_l = []
    for s_div in range(2, int(math.sqrt(n)) + 1):
        l_div, remainder = divmod(n, s_div)
        if remainder == 0:
            if l_div != s_div:
                divisors_from_s.append(s_div)
            divisors_from_l.append(l_div)
    
    return [1] + divisors_from_s + divisors_from_l[::-1] + [n]

divisors = find_diviors(N)

answer = 0

for d in divisors:
    summation = N // d + 1 
    for x in range(1, summation // 2  + 1):
        y = summation - x
        if math.gcd(x, y) == 1:
            answer += 1

print(answer)
