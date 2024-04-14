import sys

input = sys.stdin.readline


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def check(i, j):
    num = int(arr[i][j])
    if num == 0 or num == 3:
        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if OOB(ni, nj): continue
            if arr[ni][nj] != '#': continue
            ground[ni][nj] = num // 2
        return True
    else:
        cnt = 0
        zcnt = 0
        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if OOB(ni, nj): continue
            if arr[ni][nj] != '#': continue
            if ground[ni][nj] == 1:
                cnt += 1
            elif ground[ni][nj] == -1:
                zcnt += 1
        if cnt == num:
            f = 0
        elif cnt + zcnt == num:
            f = 1
        else:
            return False

        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if OOB(ni, nj): continue
            if arr[ni][nj] != '#': continue
            if ground[ni][nj] != -1: continue
            ground[ni][nj] = f
    return True


N = int(input())
arr = [input() for _ in range(N)]
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
if N <= 3:
    print(int(arr[0][0]))
else:
    ground = [[0] * N] \
             + [[0] + [-1] * (N - 2) + [0] for _ in range(N - 2)] \
             + [[0] * N]
    for i in range(2, N - 2):
        for j in range(2, N - 2):
            ground[i][j] = 1
    check_lst = []
    for _ in range(100):
        for j in range(N):
            check_lst.append((0, j))
            check_lst.append((N - 1, j))
        for i in range(1, N - 1):
            check_lst.append((i, 0))
            check_lst.append((i, N - 1))
    while check_lst:
        nc = len(check_lst)
        for c in range(nc)[::-1]:
            i, j = check_lst[c]
            if check(i, j):
                check_lst.pop(c)

    print(sum([sum(g) for g in ground]))
