import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = [0] + list(map(int, input().split()))

cumulative_sum = [0] * (N + 1)
for idx in range(1, N + 1):
    cumulative_sum[idx] = cumulative_sum[idx - 1] + sequence[idx]

output = []
for _ in range(M):
    s, e = map(int, input().split())
    output.append(str(cumulative_sum[e] - cumulative_sum[s - 1]))

print('\n'.join(output))
