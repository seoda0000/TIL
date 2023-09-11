"""
백준 골드5 7576
https://www.acmicpc.net/problem/7576
"""

import sys
input = sys.stdin.readline
from collections import  deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
stk = deque()

for m in range(M):
    for n in range(N):
        if box[n][m] == 1:
            stk.append((n, m))

aLst = [-1, 1, 0, 0]
bLst =  [0, 0, 1, -1]
t = 0

while True:
    tlst = deque()
    while stk:
        i, j = stk.popleft()
        for x in range(4):
            ni = i+aLst[x]
            nj = j+bLst[x]
            if (0 <= ni < N) and ( 0 <= nj < M) and box[ni][nj] == 0:
                box[ni][nj] = t+1
                tlst.append((ni, nj))
    if tlst:
        t += 1
        stk = tlst
    else:
        break
ans = 0
for m in range(M):
    for n in range(N):
        if box[n][m] == 0:
            ans = -1
            break
    if ans == -1:
        break
if ans == 0:
    print(t)
else:
    print(-1)



