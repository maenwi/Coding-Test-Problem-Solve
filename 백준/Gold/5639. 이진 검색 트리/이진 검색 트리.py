# 전위 순회, 후위 순회
# 전위 순회 : D L R
# 후위 순회 : L R D

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.tree = None
  
    def insert(self, x):
        # 입력 받은 노드 선언
        new_node = Node(x)

        # 아직 트리가 만들어지지 않았다면,
        # 트리를 만듦.
        if self.tree is None:
            self.tree = new_node
            return

        # 이미 만들어진 트리가 있다면, 넣을 자리 탐색
        current_node = self.tree
        parent_node = None

        while current_node is not None:
            if current_node.data == x:
                return  # 중복이면 아무 것도 안 함
            parent_node = current_node
            if x < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if x < parent_node.data:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

    def postorder(self):
        result = []
        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.data)
        _postorder(self.tree)
        return result

import sys
sys.setrecursionlimit(10**6)

inputs = list(map(int, sys.stdin.read().split()))

bst = BinarySearchTree()

for i in inputs:
    bst.insert(i)

answer = bst.postorder()
for a in answer:
    print(a)
