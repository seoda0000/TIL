"""
백준 실버1 14940
쉬운 최단거리

지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.
"""

import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
v = [[0]*W for _ in range(H)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
ab = [(0, 1), (1, 0), (-1, 0), (0, -1)]

i = 0
while i < H:

    for j in range(W):
        if arr[i][j] == 2:
            ti, tj = i, j
            i = H
            break
    i += 1

q = deque()
q.append((ti, tj))
k = 0

while q:
    k += 1
    n = len(q)
    for _ in range(n):
        i, j = q.popleft()
        for a, b in ab:
            ni, nj = a+i, b+j
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = k

for i in range(H):
    for j in range(W):
        if v[i][j] == 0 and 0<arr[i][j]<2:
            v[i][j] = -1
for vv in v:
    print(" ".join(map(str,vv)))