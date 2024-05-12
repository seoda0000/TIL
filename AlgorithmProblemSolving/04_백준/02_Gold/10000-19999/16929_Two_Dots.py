def solve():
    for i in range(N):
        for j in range(M):
            v[i][j] = 1
            if check([(i, j)]):
                return True
    return False


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < M)


def check(lst):
    ci, cj = lst[-1]
    if len(lst) >= 4:
        si, sj = lst[0]
        if abs(si - ci) + abs(sj - cj) == 1:  # 인접
            return True

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if OOB(ni, nj): continue
        if arr[ni][nj] != arr[ci][cj]: continue
        if v[ni][nj]: continue

        v[ni][nj] = 1
        if check(lst + [(ni, nj)]):
            return True
        v[ni][nj] = 0

    return False


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
v = [[0] * M for _ in range(N)]
if solve():
    print("Yes")
else:
    print("No")
