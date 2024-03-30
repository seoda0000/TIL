di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
ci, cj, cd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]
v[ci][cj] = 1

while True:
    can_go = False
    nd = cd
    for _ in range(4):
        nd = (nd - 1) % 4

        ni, nj = ci + di[nd], cj + dj[nd]
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] or v[ni][nj]:

            continue

        v[ni][nj] = 1
        ci, cj = ni, nj
        can_go = True
        break

    if not can_go:
        ni, nj = ci - di[nd], cj - dj[nd]
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj]: break
        ci, cj = ni, nj
    else:
        cd = nd

print(sum([sum(vv) for vv in v]))
