"""
부모 찾는 거 까먹었다...
"""

from collections import deque
import heapq


def check_land(si, sj, id):
    q = deque([(si, sj)])
    arr[i][j] = id

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] != 1: continue
            arr[ni][nj] = id
            q.append((ni, nj))
    return


def build_bridge(si, sj):
    start = arr[si][sj]

    for d in range(4):
        ci, cj = si, sj
        cnt = 0
        while True:
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): break
            if arr[ni][nj] == start:
                break
            elif arr[ni][nj] == 0:
                ci, cj = ni, nj
                cnt += 1
            else:
                if cnt > 1:
                    end = arr[ni][nj]
                    heapq.heappush(bridges, (cnt, start, end))
                break
    return


def find(a):
    if p[a] == a:
        return a
    else:
        p[a] = find(p[a])
        return p[a]


def union(a, b):
    p[find(b)] = p[a]


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
id = 1
INF = M * N + 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            id += 1
            check_land(i, j, id)
Nl = id - 1
bridges = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            build_bridge(i, j)

p = list(range(id + 1))
mn = 0
while bridges:
    cnt, start, end = heapq.heappop(bridges)
    if find(start) != find(end):
        mn += cnt
        union(start, end)
pcnt = 0
for i in range(2, id + 1):
    if p[i] == i:
        pcnt += 1
if pcnt == 1:
    print(mn)
else:
    print(-1)
