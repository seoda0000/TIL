from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
si, sj = map(int, input().split())
ei, ej = map(int, input().split())
si, sj, ei, ej = si - 1, sj - 1, ei - 1, ej - 1
arr = [list(map(int, input().split())) for _ in range(N)]
INF = N * M + 1
v0 = [[INF] * M for _ in range(N)]  # 벽 안 부수고 도착한 시간
v1 = [[INF] * M for _ in range(N)]  # 벽 하나 부수고 도착한 시간
q = deque([(si, sj, 0)])  # 좌표, 벽 부순 횟수
v0[si][sj] = 0

while q:
    ci, cj, ck = q.popleft()

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < M): continue

        if arr[ni][nj]:  # 벽
            if ck: continue

            if v1[ni][nj] <= v0[ci][cj] + 1: continue
            v1[ni][nj] = v0[ci][cj] + 1
            q.append((ni, nj, 1))

        else:  # 빈 칸
            if ck:
                if v1[ni][nj] <= v1[ci][cj] + 1: continue
                v1[ni][nj] = v1[ci][cj] + 1
            else:
                if v0[ni][nj] <= v0[ci][cj] + 1: continue
                v0[ni][nj] = v0[ci][cj] + 1
            q.append((ni, nj, ck))

ans = min(v0[ei][ej], v1[ei][ej])
if ans == INF:
    ans = -1

print(ans)
