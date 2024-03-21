from collections import deque


def battle(si, sj):
    s = w = 0

    q = deque([(si, sj)])
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if arr[ci][cj] == 'v':
            w += 1
        elif arr[ci][cj] == 'o':
            s += 1

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == '#': continue
            if v[ni][nj]: continue
            v[ni][nj] = 1
            q.append((ni, nj))

    if s > w:
        w = 0
    else:
        s = 0

    return s, w


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
v = [[0] * M for _ in range(N)]
cnt_s = cnt_w = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == '#': continue
        if v[i][j]: continue
        s, w = battle(i, j)
        cnt_s += s
        cnt_w += w

print(cnt_s, cnt_w)
