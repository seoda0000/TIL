"""
https://www.acmicpc.net/problem/2589
백준 2589 골드5 보물섬

1. 섬을 먼저 구하고 섬 내부의 모든 경로를 구한 풀이
왜 그랬을까...?
브루트포스부터 하고 생각하자...
"""


def findRoute(i, j, check):
    v[i][j] = check

    q = [(i, j)]
    cnt = 0

    while True:
        lenq = len(q)
        nxtq = []
        for l in range(lenq):
            a, b = q[l]
            for n in range(4):
                na, nb = a + dx[n], b + dy[n]

                if 0 <= na < N and 0 <= nb < M and 0 < v[na][nb] < check:
                    v[na][nb] = check
                    nxtq.append((na, nb))

        if nxtq:
            cnt += 1
            q = nxtq
        else:
            break

    return cnt


def findLand(i, j):
    dist = 0
    v[i][j] = 1
    q = [(i, j)]
    land = [(i, j)]

    while True:
        lenq = len(q)
        nxtq = []
        for l in range(lenq):
            a, b = q[l]
            for n in range(4):
                na, nb = a + dx[n], b + dy[n]

                if 0 <= na < N and 0 <= nb < M and v[na][nb] == 0:
                    if arr[na][nb] == 'W':
                        v[na][nb] = -1
                    elif arr[na][nb] == 'L':
                        v[na][nb] = 1
                        nxtq.append((na, nb))
                        land.append((na, nb))
        if nxtq:
            q = nxtq
        else:
            break

    for s in range(len(land)):
        nxi, nxj = land[s]
        dist = max(dist, findRoute(nxi, nxj, s + 2))

    return dist


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if v[i][j] != 0:
            continue
        if arr[i][j] == 'L':
            ans = max(ans, findLand(i, j))
        else:
            v[i][j] = -1

print(ans)

"""
섬과 바다 상관 없이 모든 곳에서 경로를 구한 풀이
"""


def findLand(i, j):
    v = [[0] * M for _ in range(N)]
    v[i][j] = 1
    q = [(i, j)]
    cnt = 0

    while True:
        nxtq = []
        for l in range(len(q)):
            a, b = q[l]
            for n in range(4):
                na, nb = a + dx[n], b + dy[n]
                if 0 <= na < N and 0 <= nb < M and v[na][nb] == 0:
                    if arr[na][nb] == 'W':
                        v[na][nb] = -1
                    elif arr[na][nb] == 'L':
                        v[na][nb] = 1
                        nxtq.append((na, nb))
        if nxtq:
            q = nxtq
            cnt += 1
        else:
            break

    return cnt


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = max(ans, findLand(i, j))

print(ans)
