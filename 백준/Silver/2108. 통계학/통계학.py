import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
values = [int(input()) for _ in range(N)]

values.sort()  # O(N log N)

# 평균 O(N)
mean = int(round(sum(values) / N))

# 중앙값
median = values[N // 2]

# 최빈값
freq = Counter(values)
max_freq = max(freq.values())

mode_candidates = [k for k, v in freq.items() if v == max_freq]
mode_candidates.sort()

mod = mode_candidates[1] if len(mode_candidates) > 1 else mode_candidates[0]

# 범위
range_val = values[-1] - values[0]

# 출력
print(mean)
print(median)
print(mod)
print(range_val)
