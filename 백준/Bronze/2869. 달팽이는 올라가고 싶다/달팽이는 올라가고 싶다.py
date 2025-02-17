A, B, V = map(int, input().split())

# (A - B) * k + A >= V
# k >= (V - A)/(A - B)

t = (V - A)/(A - B)
if int(t) == t:
    print(int(t) + 1)
else:
    print(int(t) + 2)
