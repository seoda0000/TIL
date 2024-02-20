import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    orders = input()

    ci = cj = pi = pj = mi = mj = 0  # 처음 좌표, 오른쪽 위 좌표, 왼쪽 아래 좌표
    d = 0
    ilst = [0]
    jlst = [0]

    for order in orders:
        if order == 'F':
            ci, cj = ci + di[d], cj + dj[d]
            ilst.append(ci)
            jlst.append(cj)

        elif order == 'B':
            ci, cj = ci - di[d], cj - dj[d]
            ilst.append(ci)
            jlst.append(cj)

        elif order == 'L':
            d = (d + 3) % 4

        else:
            d = (d + 1) % 4
    ans = (max(ilst) - min(ilst)) * (max(jlst) - min(jlst))
    print(ans)
