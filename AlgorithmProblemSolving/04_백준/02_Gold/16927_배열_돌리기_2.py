import sys

input = sys.stdin.readline


def mark(arr, lst, p):
    ci, cj = p, p
    k = d = 0
    while True:
        v[ci][cj] = 2
        arr[ci][cj] = lst[k]
        if ci == p + 1 and cj == p: break
        k += 1
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M) or v[ni][nj] == 2:
            d = (d + 1) % 4
            ni, nj = ci + di[d], cj + dj[d]
        ci, cj = ni, nj
    return


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

v = [[0] * M for _ in range(N)]
p = 0
while True:
    if v[p][p]: break

    ci, cj = p, p
    d = 0
    lst = []
    while True:
        v[ci][cj] = 1
        lst.append(arr[ci][cj])
        if ci == p + 1 and cj == p: break
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M) or v[ni][nj]:
            d = (d + 1) % 4
            ni, nj = ci + di[d], cj + dj[d]
        ci, cj = ni, nj
    r = R % len(lst)
    lst = lst[r:] + lst[:r]
    mark(arr, lst, p)
    p += 1
for a in arr:
    print(*a)
