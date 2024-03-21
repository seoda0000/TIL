from collections import deque


def checkPower(si, sj):
    global cnt_b, cnt_w

    power = 1
    v[si][sj] = 1
    q = deque([(si, sj)])
    color = arr[si][sj]

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if arr[ni][nj] != color: continue
            v[ni][nj] = 1
            q.append((ni, nj))
            power += 1

    if color == 'W':
        cnt_w += power ** 2
    else:
        cnt_b += power ** 2
    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
M, N = map(int, input().split())
arr = [input() for _ in range(N)]
cnt_w, cnt_b = 0, 0
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if v[i][j]: continue
        checkPower(i, j)

print(cnt_w, cnt_b)
