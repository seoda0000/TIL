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

"""
1년 후 풀이
"""

import sys
input = sys.stdin.readline
from collections import  deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
zeroCnt = 0
for n in range(N):
    zeroCnt += arr[n].count(0)
    for m in range(M):
        if arr[n][m] == 1:  # 익은 토마토 위치 파악
            q.append((n, m))

if zeroCnt == 0:  # 모든 토마토가 익은 경우
    print(0)
elif len(q) == 0:  # 모든 토마토가 못 익는 경우
    print(-1)
else:
    day = 0
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    while q:
        isChanged = False
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if 0 > ni or ni >= N or 0 > nj or nj >= M: continue
                if arr[ni][nj] == 0:
                    zeroCnt -= 1
                    isChanged = True
                    arr[ni][nj] = 1
                    q.append((ni, nj))

        if isChanged:
            day += 1
        else:
            break

    if zeroCnt:
        print(-1)
    else:
        print(day)


