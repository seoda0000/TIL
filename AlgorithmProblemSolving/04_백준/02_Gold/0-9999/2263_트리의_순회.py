"""
백준 골드2 2263
트리의 순회
https://www.acmicpc.net/problem/2263

n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def f(si, ei, sp, ep): # 노드의 inorder 시작 idx, 끝 idx, postorder 시작 idx, 끝 idx
    if si > ei or sp > ep:
        return
    num = postorder[ep]           # 노드의 부모
    print(num, end=" ")
    n = inorderIndex[num] - si    # 노드의 부모 위치 idx
    f(si, si+n-1, sp, sp+n-1)         # 왼쪽 노드
    f(si+n+1, ei, sp+n, ep-1)         # 오른쪽 노드

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorderIndex = [0] * (n+1)
for i in range(n):
    inorderIndex[inorder[i]] = i
f(0, n-1, 0, n-1)