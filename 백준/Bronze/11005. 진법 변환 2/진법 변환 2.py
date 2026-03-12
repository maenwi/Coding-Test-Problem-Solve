alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mapping = {i+10 : alphabets[i] for i in range(26)}
mapping.update({i:str(i) for i in range(10)})

n, b = map(int, input().split())

base_b = ""

while n > 0:
    n, r = divmod(n, b)
    base_b = mapping[r] + base_b

print(base_b)
