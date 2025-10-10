def isPrime(p):
    if p < 2:
        return False
    for i in range(2, int(p ** (0.5)) + 1):
        if p % i == 0:
            return False
    return True

def convert_base(n, k):
    base_k = []
    while n != 0:
        n, r = divmod(n, k)
        base_k.append(str(r))
    return "".join(base_k[::-1])
            
def solution(n, k):
    num = convert_base(n, k)
    num = num.split("0")
    
    answer = 0
    for n in num:
        if n == "":
            continue
        if isPrime(int(n)):
            answer += 1
        
    return answer