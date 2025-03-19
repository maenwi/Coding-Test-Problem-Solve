T = int(input())

fib0 = [0] * 41
fib1 = [0] * 41

fib0[0], fib1[0] = 1, 0
fib0[1], fib1[1] = 0, 1
for idx in range(2, 41):
    fib0[idx] = fib0[idx - 1] + fib0[idx - 2]
    fib1[idx] = fib1[idx - 1] + fib1[idx - 2]

ans = []
for _ in range(T):
    n = int(input())
    ans.append(f"{fib0[n]} {fib1[n]}")

print("\n".join(ans))
