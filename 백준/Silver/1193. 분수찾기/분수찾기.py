n = int(input())

i = 0
while n > 0:
    i += 1
    n -= i

u = i + n
d = 1 - n

if i % 2 == 0:
    print(f"{u}/{d}")
else:
    print(f"{d}/{u}")

