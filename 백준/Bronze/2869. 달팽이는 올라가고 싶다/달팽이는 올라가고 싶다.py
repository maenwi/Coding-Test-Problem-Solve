A, B, V = map(int, input().split())

q, r = divmod(V - A, A - B)

if r:
    print(q + 2)
else:
    print(q + 1)
