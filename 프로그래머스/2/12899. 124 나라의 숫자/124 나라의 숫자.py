def solution(n):
    answer = []
    while n:
        if n % 3:
            answer.append(str(n % 3))
            n //= 3
        else:
            answer.append(str(4))
            n = n//3 - 1

    return "".join(answer[::-1])

