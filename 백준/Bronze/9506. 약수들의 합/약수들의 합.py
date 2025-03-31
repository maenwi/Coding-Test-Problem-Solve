def is_perfect(n):
    divisor_from_small = [1]
    divisor_from_big = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisor_from_small.append(d)
            divisor_from_big.append(n // d)
    
    return divisor_from_small + [d for d in divisor_from_big[::-1]]

answers = []
while True:
    n = int(input())
    if n == -1:
        break
    divisors = is_perfect(n)
    summation = sum(divisors)

    if summation == n:
        answers.append(f"{n} = {" + ".join([str(d) for d in divisors])}")
    else:
        answers.append(f"{n} is NOT perfect.")

print("\n".join(answers))
