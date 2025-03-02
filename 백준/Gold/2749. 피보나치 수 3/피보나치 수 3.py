# 행렬 곱 피보나치
# 2 by 2 행렬 곱이 필요

def matrix_multiplication(A, B, mod):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, 
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, 
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def matrix_exponential(matrix_to_exp, n, mod):
    # base는 2의 거듭제곱
    # answer는 답이 될 것
    answer = [[1, 0], [0, 1]]
    base = matrix_to_exp

    while n: # n이 0이 아닐 동안
        if n % 2: # n이 홀수라면
            answer = matrix_multiplication(answer, base, mod)
        
        base = matrix_multiplication(base, base, mod)
        n //= 2
    
    return answer

def fibonacci(n, mod):
    if n == 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    answer = matrix_exponential(matrix, n - 1, mod)
    return answer[0][0]

n = int(input())
print(fibonacci(n, 1000000))