N, L = map(int, input().split())

a = None

min_sum = (L - 1) * (L - 2) / 2

for l in range(L, 101):
    min_sum += (l - 1)
    a = (2 * N / l + 1 - l) / 2

    if min_sum > N:
        a = None
        break

    if int(a) == a:
        break

    a = None

if a is None:
    print(-1)
else:
    a = int(a)
    print(" ".join([str(a + i) for i in range(l)]))