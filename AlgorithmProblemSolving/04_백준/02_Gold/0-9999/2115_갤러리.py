N, M = map(int, input().split())
arr = [input() for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
ans = 0
for d in range(4):  # 방향별 체크
    v = [[0] * M for _ in range(N)]  # 벽 표시
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'X': continue
            ni, nj = i + di[d], j + dj[d]
            if arr[ni][nj] != 'X': continue
            v[i][j] = 1  # 해당 방향에 벽이 있다
    pv = [[0] * M for _ in range(N)]  # 그림 표시
    if d // 2:  # 좌우
        nd = 1
    else:  # 상하
        nd = 3
    for i in range(N):
        for j in range(M):
            if not v[i][j]: continue
            if pv[i][j]: continue
            ni, nj = i + di[nd], j + dj[nd]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if not v[ni][nj] or pv[ni][nj]: continue
            pv[i][j] = 1
            pv[ni][nj] = 1
            ans += 1
