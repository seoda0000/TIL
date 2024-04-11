from collections import deque


def solve(si, sj):
    v = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(4)]

    q = deque([(si, sj, sd, 0)])

    v[sd][si][sj] = 0

    while q:
        ci, cj, cd, ck = q.popleft()

        if (ci, cj, cd) == (ei, ej, ed):
            return ck

        for nd in [(cd + 1) % 4, (cd - 1) % 4]:
            if v[nd][ci][cj] <= ck + 1:
                continue
            v[nd][ci][cj] = ck + 1
            q.append((ci, cj, nd, ck + 1))

        for x in range(1, 4):
            ni, nj = ci + di[cd] * x, cj + dj[cd] * x

            if not (0 <= ni < N and 0 <= nj < M): break
            if arr[ni][nj]: break
            if v[cd][ni][nj] <= ck + 1: continue
            v[cd][ni][nj] = ck + 1
            q.append((ni, nj, cd, ck + 1))

    return -1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dic = {1: 0, 2: 2, 3: 1, 4: 3}
N, M = map(int, input().split())
INF = N * M * 100 * 4
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())
si, sj, ei, ej = si - 1, sj - 1, ei - 1, ej - 1
sd, ed = dic[sd], dic[ed]
print(solve(si, sj))
