def make_order(nth):
    if nth == K:
        order_lst.append(tuple(temp))

    for n in range(K):
        if n not in temp:
            temp.append(n)
            make_order(nth + 1)
            temp.pop()
    return


def do_order(order, arr):
    ti, tj, tk = order
    ti, tj = ti - 1, tj - 1

    for k in range(1, tk + 1):
        d = 0
        si, sj = ti - k, tj - k
        ei, ej = ti + k, tj + k

        ci, cj = si, sj
        bef = arr[ci][cj]

        while True:
            ni, nj = ci + di[d], cj + dj[d]
            if not (si <= ni <= ei and sj <= nj <= ej):
                d = (d + 1) % 4
                ni, nj = ci + di[d], cj + dj[d]
            bef, arr[ni][nj] = arr[ni][nj], bef

            ci, cj = ni, nj
            if ci == si and cj == sj:
                break

    return


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M, K = map(int, input().split())
start_arr = [tuple(map(int, input().split())) for _ in range(N)]
calcs = [list(map(int, input().split())) for _ in range(K)]

# 순열 만들기
order_lst = []
temp = []
make_order(0)

ans = 100 * 50 + 1
for orders in order_lst:
    arr = [list(a[:]) for a in start_arr]
    for order in orders:  # 회전 연산 순서대로 수행
        do_order(calcs[order], arr)

    mn_sm = 100 * 50 + 1  # 배열 값의 최소값 갱신

    for a in arr:
        mn_sm = min(mn_sm, sum(a))

    ans = min(ans, mn_sm)

print(ans)
