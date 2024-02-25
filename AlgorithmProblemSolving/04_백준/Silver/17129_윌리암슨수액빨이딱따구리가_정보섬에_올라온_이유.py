from collections import deque


def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                return i, j


def find_route(si, sj):
    q = deque([(si, sj)])
    v[si][sj] = 1
    k = -1
    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            if arr[ci][cj] > 2:
                return k

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]

                if not (0 <= ni < N and 0 <= nj < M): continue
                if v[ni][nj]: continue
                if arr[ni][nj] == 1: continue

                v[ni][nj] = 1
                q.append((ni, nj))
    return -1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
si, sj = find_start()

ans = find_route(si, sj)

if ans >= 0:
    print("TAK")
    print(ans)
else:
    print("NIE")
