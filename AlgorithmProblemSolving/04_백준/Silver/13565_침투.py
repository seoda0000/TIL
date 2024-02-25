from collections import deque

ans = "NO"
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
q = deque()
v = [[0] * M for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for j in range(M):
    if arr[0][j] == 0:
        q.append((0, j))
        v[0][j] = 1

while q:
    ci, cj = q.popleft()

    if ci == N - 1:
        ans = "YES"
        break

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < M): continue
        if arr[ni][nj]: continue
        if v[ni][nj]: continue
        v[ni][nj] = 1
        q.append((ni, nj))

print(ans)
