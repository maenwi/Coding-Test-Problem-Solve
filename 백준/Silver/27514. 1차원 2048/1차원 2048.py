from collections import Counter

N = int(input())
count = Counter(list(map(int, input().split())))

max_num = max(count.keys())

for power in range(1, 63):
    small = 2 ** (power - 1)
    large = 2 ** power
    small_count = count.get(small, None)
    large_count = count.get(large, None)

    if small_count is None or small_count <= 1:
        continue

    elif large_count is None:
        count[large] = small_count // 2
    
    else:
        count[large] += small_count // 2
    
    count[small] -= (small_count // 2) * 2

    if count[large] >= 1 and max_num <= large:
        max_num = large

print(max_num)
