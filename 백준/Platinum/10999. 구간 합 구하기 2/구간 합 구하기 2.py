class LazySegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            m = (l + r) // 2
            self.build(data, node*2, l, m)
            self.build(data, node*2+1, m+1, r)
            self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def push(self, node, l, r):
        if self.lazy[node] != 0:
            self.tree[node] += (r - l + 1) * self.lazy[node]  # 누적합 반영
            if l != r:  # 리프 노드가 아니라면 자식에게도 미뤄줌
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2+1] += self.lazy[node]
            self.lazy[node] = 0

    def range_update(self, node, l, r, ul, ur, val):
        self.push(node, l, r)
        if ur < l or r < ul:
            # [l, r] [ul, ur] or [ul, ur] [l, r]
            return
        if ul <= l and r <= ur:
            # 이 노드가 커버하는 구간이,
            # 우리가 업데이트 해야할 구간 내에 있다면,
            # [ul, [l, r], ur]
            self.lazy[node] += val
            self.push(node, l, r)
            return
        m = (l + r) // 2
        self.range_update(node*2, l, m, ul, ur, val)
        self.range_update(node*2+1, m+1, r, ul, ur, val)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def range_query(self, node, l, r, ql, qr):
        self.push(node, l, r)
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r) // 2
        left = self.range_query(node*2, l, m, ql, qr)
        right = self.range_query(node*2+1, m+1, r, ql, qr)
        return left + right

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
seq = [int(input()) for _ in range(N)]
operations = [tuple(map(int, input().split())) for _ in range(M + K)]

lazy_segment_tree = LazySegmentTree(seq)

for operation in operations:
    if operation[0] == 1:
        lazy_segment_tree.range_update(1, 0, N - 1, operation[1] - 1, operation[2] - 1, operation[3])
    else:
        print(lazy_segment_tree.range_query(1, 0, N - 1, operation[1] - 1, operation[2] - 1))