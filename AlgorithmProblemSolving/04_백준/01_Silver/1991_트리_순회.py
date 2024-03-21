"""
트리 순회
https://www.acmicpc.net/problem/1991
백준 실버1

이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

전위 순회한 결과 : // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.
"""


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def forward(Node):
    global ans
    ans += Node.data
    if Node.left:
        idx = ord(Node.left) - ord('A')
        forward(tree[idx])
    if Node.right:
        idx = ord(Node.right) - ord('A')
        forward(tree[idx])


def center(Node):
    global ans
    if Node.left:
        idx = ord(Node.left) - ord('A')
        center(tree[idx])
    ans += Node.data
    if Node.right:
        idx = ord(Node.right) - ord('A')
        center(tree[idx])

def backward(Node):
    global ans
    if Node.left:
        idx = ord(Node.left) - ord('A')
        backward(tree[idx])
    if Node.right:
        idx = ord(Node.right) - ord('A')
        backward(tree[idx])
    ans += Node.data

import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
tree = [Node(0, 0, 0)] * N

for _ in range(N):
    d, r, l = input().split()
    if r == '.':
        r = None
    if l == '.':
        l = None
    idx = ord(d) - ord('A')
    tree[idx] = Node(d, r, l)
ans = ""
forward(tree[0])
print(ans)
ans = ""
center(tree[0])
print(ans)
ans = ""
backward(tree[0])
print(ans)