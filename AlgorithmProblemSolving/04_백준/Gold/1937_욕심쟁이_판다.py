from collections import deque
import sys

sys.setrecursionlimit(25_00_00)


def search(ci, cj):
    if v[ci][cj]:
        return v[ci][cj]

    mx = 0

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): continue
        if arr[ni][nj] <= arr[ci][cj]: continue
        cnt = search(ni, nj)
        mx = max(cnt, mx)

    v[ci][cj] = mx + 1

    return v[ci][cj]


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if v[i][j]: continue
        search(i, j)

ans = 0
for vv in v:
    ans = max(ans, max(vv))

print(ans)
