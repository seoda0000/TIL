from collections import deque


def get_buildings(si, sj):
    buildings = [(si, sj)]
    v[si][sj] = 1
    q = deque(buildings)

    while q:
        ci, cj = q.popleft()
        for d in range(6):
            ni, nj = ci + di[ci % 2][d], cj + dj[ci % 2][d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] != 1: continue
            if v[ni][nj]: continue
            v[ni][nj] = 1
            buildings.append((ni, nj))
            q.append((ni, nj))

    return buildings


def check_outside():
    q = deque([(0, 0)])
    arr[0][0] = 2

    while q:
        ci, cj = q.popleft()
        for d in range(6):
            ni, nj = ci + di[ci % 2][d], cj + dj[ci % 2][d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] != 0: continue
            arr[ni][nj] = 2
            q.append((ni, nj))
    return


di = [[0, 0, 1, -1, -1, 1], [0, 0, 1, -1, 1, -1]]  # 0행: 짝수, 1행: 홀수
dj = [[1, -1, 0, 0, -1, -1], [1, -1, 0, 0, 1, 1]]
M, N = map(int, input().split())
arr = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]
M += 2
N += 2
check_outside()
v = [[0] * M for _ in range(N)]
ans = 0
for i in range(1, N):
    for j in range(1, M):
        if arr[i][j] != 1: continue
        if v[i][j]: continue

        buildings = get_buildings(i, j)

        walls = 0
        for bi, bj in buildings:
            for d in range(6):
                ni, nj = bi + di[bi % 2][d], bj + dj[bi % 2][d]
                if not (0 <= ni < N and 0 <= nj < M): continue
                if arr[ni][nj] != 2: continue
                walls += 1

        ans += walls

print(ans)
