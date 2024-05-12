import sys
from collections import deque

input = sys.stdin.readline


def move(ci, cj, d):
    t = 0
    while True:
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < M):  # 절벽으로 빠짐
            return -1, -1, -1
        if arr[ni][nj] == R:  # 직전 위치 반환
            return ci, cj, t
        elif arr[ni][nj] == H:  # 구멍에 빠짐
            return -1, -1, -1
        elif arr[ni][nj] == E:  # 출구
            return ni, nj, t
        else:
            t += arr[ni][nj]
            ci, cj = ni, nj


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

M, N = map(int, input().split())
R, H, E = -2, -3, -4
arr = []
for i in range(N):
    ipt = list(input())
    row = []

    for j in range(M):
        x = ipt[j]
        if x == 'T':
            row.append(0)
            si, sj = i, j
        elif x == 'R':
            row.append(R)
        elif x == 'H':
            row.append(H)
        elif x == 'E':
            row.append(E)
            ei, ej = i, j
        else:
            row.append(int(x))
    arr.append(row)

INF = 500 * 500 * 500
v = [[INF] * M for _ in range(N)]
q = deque([(si, sj)])
v[si][sj] = 0

while q:
    ci, cj = q.popleft()

    for d in range(4):
        ni, nj, nt = move(ci, cj, d)
        if nt < 0:
            continue
        if v[ni][nj] > v[ci][cj] + nt:
            v[ni][nj] = v[ci][cj] + nt
            q.append((ni, nj))

if v[ei][ej] == INF:
    print(-1)
else:
    print(v[ei][ej])
