from collections import deque

di = [-2, -2, -1, -1, 1, 1, 2, 2]
dj = [-1, 1, -2, 2, -2, 2, -1, 1]

N, M = map(int, input().split())
si, sj = map(int, input().split())
si, sj = si - 1, sj - 1
v = [[0] * N for _ in range(N)]

targets = []

for _ in range(M):
    ti, tj = map(int, input().split())
    ti, tj = ti - 1, tj - 1
    targets.append((ti, tj))
    v[ti][tj] = -1

v[si][sj] = 1
q = deque([(si, sj)])
cnt = M

while q and cnt > 0:
    ci, cj = q.popleft()

    for d in range(8):
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < N): continue
        if v[ni][nj] == -1: cnt -= 1  # 적 잡기
        if v[ni][nj] > 0: continue

        v[ni][nj] = v[ci][cj] + 1
        q.append((ni, nj))

ans = [v[ti][tj] - 1 for ti, tj in targets]
print(*ans)
