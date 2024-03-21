"""
https://www.acmicpc.net/problem/22856
백준 골드4 트리 순회

N이 100000이므로 리스트 연산을 추가하는 건 바람직하지 않다.
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def inorder(now):
    if now == -1:
        return
    inorder(left[now])
    inorderLst.append(now)
    inorder(right[now])


def f(now):
    global ans, flag

    v[now] = 1
    if left[now] > 0 and v[left[now]] == 0:
        ans += 1
        f(left[now])
    if right[now] > 0 and v[right[now]] == 0:
        ans += 1
        f(right[now])

    # 기존 풀이
    # if sum(v) / N == 1:
    #     print(ans)
    #     exit()

    if now == inorderLst[-1] or flag:
        flag = 1
        return

    else:
        ans += 1
        return


N = int(input())
v = [0] * (N + 1)
parent = [0] * (N + 2)
left = [0] * (N + 1)
right = [0] * (N + 1)
for _ in range(N):
    n, lChild, rChild = map(int, input().split())
    left[n] = lChild
    right[n] = rChild
    parent[lChild] = n
    parent[rChild] = n

ans = 0
flag = 0
inorderLst = []
inorder(1)
f(1)
print(ans)
