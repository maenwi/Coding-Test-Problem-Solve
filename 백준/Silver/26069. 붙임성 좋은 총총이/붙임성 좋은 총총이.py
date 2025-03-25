N = int(input())

dancings = {"ChongChong" : True}

for _ in range(N):
    a, b = input().split(" ")

    # a 또는 b가 춤추는지 확인하고
    # 둘 중 하나가 춤추면 나머지 하나를 춤추게 만들자

    if dancings.get(a, False):
        # a가 춤을 추고 있다면
        dancings[b] = True
        continue
    
    if dancings.get(b, False):
        # b가 춤을 추고 있다면
        dancings[a] = True
        continue

print(len(dancings))