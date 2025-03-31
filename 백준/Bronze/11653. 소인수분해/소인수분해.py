def euler_totient_function(n):
    result = n
    # 소인수 분해는 sqrt 까지만 확인하면 됨.
    for p in range(2, int(n ** (1/2)) + 1):
        if n % p == 0: # 소인수인 p를 찾았다면, 
            while n % p == 0: # p가 더 안 남아 있을 때 까지 나눠줌
                print(p)
                n //= p
            result -= result // p
    
    # sqrt(n) 보다 큰 소인수가 남아있다면 확인이 안 됐을 거고,
    # 이 소인수는 유일함
    # 왜냐하면, sqrt(n)보다 큰 소인수 두 개가 있고, 각각을 p1, p2라고 한다면,
    # p1 * p2 > n 임. 따라서 sqrt(n)보다 큰 소인수는 하나 밖에 없음.
    if n > 1:
        print(n)
        result -= result // n
    return result

euler_totient_function(int(input()))