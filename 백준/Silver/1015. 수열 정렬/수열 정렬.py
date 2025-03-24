N = int(input())

seq = list(map(int, input().split()))

seq = [[v, i] for i, v in enumerate(seq)]

seq.sort(key = lambda x : x[0])
# O(N logN)

for new_idx in range(len(seq)):
    seq[new_idx].append(new_idx)

seq.sort(key = lambda x:x[1])
# O(N logN)

answer = [str(seq[idx][2]) for idx in range(len(seq))]
print(" ".join(answer))

# 입력 : 2 3 1
# idx : 0 1 2

# seq.sort() : 1 2 3
# idx        : 0 1 2
