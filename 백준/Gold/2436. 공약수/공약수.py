def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def solution(gcd, lcm):
    if gcd == lcm:
        print(f"{lcm} {lcm}")
        return

    # a / gcd * b / gcd * gcd = lcm
    # 따라서 lcm을 gcd로 나누면, 그 수는 (a/gcd)*(b/gcd)임
    target = lcm // gcd

    # 약수가 1, target
    min_pair = (1, target)
    min_sum = 1 + target 

    for small_divisor in range(1, int(target ** 0.5) + 1):
        if target % small_divisor == 0:
            large_divisor = target // small_divisor

            # 찾은 두 숫자가 서로소여야
            # input에서의 gcd, lcm이 만족됨
            if find_gcd(small_divisor, large_divisor) != 1:
                continue
            
            if small_divisor + large_divisor < min_sum:
                min_sum = small_divisor + large_divisor
                min_pair = (small_divisor, large_divisor)
    
    a, b = min_pair[0] * gcd, min_pair[1] * gcd
    print(f"{min(a, b)} {max(a, b)}")

    return

gcd, lcm = map(int, input().split())

solution(gcd, lcm)