from collections import defaultdict


def game(ci, cj, aduinos):
    for o in range(len(orders)):

        d = orders[o]
        board[ci][cj] = '.'
        ni, nj = ci + di[d], cj + dj[d]

        nxt_aduinos = defaultdict(int)

        for ai, aj in aduinos:
            board[ai][aj] = '.'
            if ni == ai and nj == aj:
                return o + 1

            nai, naj = 0, 0
            mnd = 100 * 100
            for e in idx:
                ei, ej = ai + di[e], aj + dj[e]
                if abs(ei - ni) + abs(ej - nj) < mnd:
                    nai, naj = ei, ej
                    mnd = abs(ei - ni) + abs(ej - nj)

            if mnd == 0:
                return o + 1

            nxt_aduinos[(nai, naj)] += 1

        aduinos = []
        for key, values in nxt_aduinos.items():
            if values > 1:
                continue
            ai, aj = key
            aduinos.append((ai, aj))
            board[ai][aj] = 'R'

        board[ni][nj] = 'I'
        ci, cj = ni, nj

    return 0


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
di = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dj = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
idx = [1, 2, 3, 4, 6, 7, 8, 9]
aduinos = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            aduinos.append((i, j))
        elif board[i][j] == 'I':
            ci, cj = i, j

orders = list(map(int, input()))
t = game(ci, cj, aduinos)
if t > 0:
    print('kraj', t)
else:
    for b in board:
        print(''.join(b))
