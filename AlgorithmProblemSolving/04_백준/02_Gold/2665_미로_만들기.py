from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
INF = N * N + 1
v = [[INF] * N for _ in range(N)]

# 0 검은 방, 1 흰 방
q = deque([(0, 0)])
v[0][0] = 0

while q:
    ci, cj = q.popleft()

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < N): continue

        if arr[ni][nj]:  # 흰방
            if v[ni][nj] <= v[ci][cj]: continue
            v[ni][nj] = v[ci][cj]
        else:  # 검은방
            if v[ni][nj] <= v[ci][cj] + 1: continue
            v[ni][nj] = v[ci][cj] + 1

        q.append((ni, nj))

print(v[N - 1][N - 1])
