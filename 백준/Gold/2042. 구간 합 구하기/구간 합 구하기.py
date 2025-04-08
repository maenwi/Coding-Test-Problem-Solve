class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, left, right):
        if left == right:
            self.tree[node] = data[left]
        else:
            mid = (left + right) // 2
            self.build(data, node*2, left, mid)
            self.build(data, node*2+1, mid+1, right)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def sum_range(self, node, left, right, ql, qr):
        # tree의 node가,
        # 원래 배열에서의 [left, right] 구간을 커버하고 있음.
        if qr < left or ql > right:
            # 우리의 관심사 밖이라면,
            # 즉, node가 커버하는 구간 [left, right] 가 [ql, qr]을 벗어났다면
            return 0 # 무시
        if ql <= left and right <= qr:
            # 우리의 관심사 안이라면,
            # 즉, node가 커버하는 구간 [left, right] 가 [ql, qr]에 속해있다면, 
            # 그 값 리턴
            return self.tree[node] # 이 값은 [left, right]를 커버하고 있음.
        mid = (left + right) // 2
        return self.sum_range(node*2, left, mid, ql, qr) + self.sum_range(node*2+1, mid+1, right, ql, qr)

    def update_a_value(self, node, left, right, idx, value):
        # 원래 data의 idx번째 값을 val로 바꿔주세요.
        # 이 idx 번째 값이 영향을 미치는 모든 구간의 합을 다 바꿔줌
        if left == right:
            self.tree[node] = value
        else:
            mid = (left + right) // 2
            if idx <= mid:
                self.update_a_value(node*2, left, mid, idx, value)
            else:
                self.update_a_value(node*2+1, mid+1, right, idx, value)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]


import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
seq = [int(input()) for _ in range(N)]
operations = [tuple(map(int, input().split())) for _ in range(M + K)]

segment_tree = SegmentTree(seq)

for a, b, c in operations:
    if a == 1:
        segment_tree.update_a_value(1, 0, N - 1, b - 1, c)
    else:
        print(segment_tree.sum_range(1, 0, N - 1, b - 1, c - 1))
