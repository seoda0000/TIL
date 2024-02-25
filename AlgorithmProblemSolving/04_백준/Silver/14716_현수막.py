from collections import deque


def check_word(si, sj):
    q = deque([(si, sj)])
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for d in range(8):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == 0: continue
            if v[ni][nj]: continue

            v[ni][nj] = 1
            q.append((ni, nj))
    return


di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: continue
        if v[i][j]: continue
        ans += 1
        check_word(i, j)

print(ans)
