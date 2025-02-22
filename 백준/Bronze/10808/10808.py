s = input()

d = {a : 0 for a in "abcdefghijklmnopqrstuvwxyz"}

for x in s:
    d[x] += 1

for i, v in enumerate(d.values()):
    if i == 25:
        print(v)
    else:
        print(v, end = " ")