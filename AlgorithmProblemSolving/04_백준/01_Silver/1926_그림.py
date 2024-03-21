from collections import deque


def checkPaint(si, sj):
    global mx

    b = 0

    v[si][sj] = 1
    q = deque([(si, sj)])

    while q:
        ci, cj = q.popleft()
        b += 1

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
    mx = max(mx, b)
    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
cnt = mx = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] and v[i][j] == 0:
            checkPaint(i, j)
            cnt += 1

print(cnt)
print(mx)
