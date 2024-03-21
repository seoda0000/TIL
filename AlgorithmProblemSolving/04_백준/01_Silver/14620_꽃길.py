def flower(nth, money, bi, bj):
    global ans
    if nth == 3:
        ans = min(ans, money)
        return

    for j in range(bj + 3, N - 1):
        here = calc_money(bi, j)
        if here < 0:
            continue
        else:
            check_v(bi, j, 1)
            flower(nth + 1, money + here, bi, j)
            check_v(bi, j, 0)

    for i in range(bi + 1, N - 1):
        for j in range(1, N - 1):
            here = calc_money(i, j)
            if here < 0:
                continue
            else:
                check_v(i, j, 1)
                flower(nth + 1, money + here, i, j)
                check_v(i, j, 0)
    return


def calc_money(si, sj):  # si, sj에 심지 못하면 -1, 심을 수 있으면 비용 반환
    if v[si][sj]: return -1

    sm = arr[si][sj]

    for d in range(4):
        ni, nj = si + di[d], sj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): return -1
        if v[ni][nj]: return -1
        sm += arr[ni][nj]

    return sm


def check_v(si, sj, num):
    v[si][sj] = num
    for d in range(4):
        ni, nj = si + di[d], sj + dj[d]
        v[ni][nj] = num


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
ans = 200 * 10 * 10
flower(0, 0, 0, 0)

print(ans)
