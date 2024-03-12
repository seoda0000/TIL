import sys

T = int(input())
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    bc_lst = [list(map(int, input().split())) for _ in range(A)]

    ai, aj = 1, 1
    bi, bj = 10, 10
    ans = 0

    for m in range(M + 1):

        # 영향권인 bc 구하기
        bc_a = []
        bc_b = []
        for tj, ti, tc, tp in bc_lst:

            if abs(ai - ti) + abs(aj - tj) <= tc:
                bc_a.append((tp, ti, tj))

            if abs(bi - ti) + abs(bj - tj) <= tc:
                bc_b.append((tp, ti, tj))

        bc_a.sort(reverse=True)
        bc_b.sort(reverse=True)

        if bc_a and not bc_b:
            ans += bc_a[0][0]
        elif not bc_a and bc_b:
            ans += bc_b[0][0]
        elif bc_a and bc_b:
            mx_bc_a = bc_a[0]
            mx_bc_b = bc_b[0]

            if mx_bc_a != mx_bc_b:
                ans += mx_bc_a[0] + mx_bc_b[0]
            else:
                mxp = mx_bc_a[0]
                cases = [mxp]  # 가능한 충전량

                if len(bc_a) > 1:
                    cases.append(mxp + bc_a[1][0])
                if len(bc_b) > 1:
                    cases.append(mxp + bc_b[1][0])

                ans += max(cases)

        # 이동
        if m == M:
            break
        ai += di[move_a[m]]
        aj += dj[move_a[m]]
        bi += di[move_b[m]]
        bj += dj[move_b[m]]

    print(f'#{test_case} {ans}')
