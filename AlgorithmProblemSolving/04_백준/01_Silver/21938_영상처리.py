from collections import deque


def check_object(si, sj):
    q = deque([(si, sj)])
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if arr[ni][nj] == 0: continue

            v[ni][nj] = 1
            q.append((ni, nj))

    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
ipts = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
v = [[0] * M for _ in range(N)]
arr = []

for n in range(N):
    row = []
    for m in range(M):
        mean = sum(ipts[n][m * 3:m * 3 + 3]) // 3
        if mean >= T:
            row.append(255)
        else:
            row.append(0)
    arr.append(row)

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 255 and v[i][j] == 0:
            ans += 1
            check_object(i, j)
print(ans)

