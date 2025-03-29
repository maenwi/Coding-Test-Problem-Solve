T = int(input())

factorials = [1 for _ in range(31)]

for idx in range(1, 31):
    factorials[idx] = factorials[idx - 1] * idx

answer = []
for _ in range(T):
    N, M = map(int, input().split())
    answer.append(int(factorials[M]/(factorials[N]*factorials[M - N])))

for a in answer:
    print(a)