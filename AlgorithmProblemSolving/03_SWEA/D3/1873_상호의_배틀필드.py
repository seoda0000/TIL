"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc

SWEA D3 1873 상호의 배틀필드
"""


def moveTank(i, j, d):
    ni, nj = i + di[d], j + dj[d]

    if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == flat:  # 이동 가능
        arr[ni][nj] = tank[d]
        arr[i][j] = flat
        return ni, nj
    else:  # 이동 불가능
        arr[i][j] = tank[d]
        return i, j


def shootBomb(i, j, d):
    ci, cj = i, j
    while True:
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < H and 0 <= nj < W): break  # 범위 밖: 아무 일도 일어나지 않는다.
        if arr[ni][nj] == flat or arr[ni][nj] == water:  # 평지 or 물: 다음 땅으로
            ci, cj = ni, nj
            continue
        if arr[ni][nj] == brick:  # 벽돌: 파괴 후 중지
            arr[ni][nj] = flat
            break
        if arr[ni][nj] == iron:  # 강철: 중지
            break

    return


T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
tank = '^v<>'
flat, brick, iron, water = '.', '*', '#', '-'
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    orders = input()

    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank:
                ci, cj = i, j
                break

    for order in orders:

        if order == 'U':
            ci, cj = moveTank(ci, cj, 0)

        elif order == 'D':
            ci, cj = moveTank(ci, cj, 1)

        elif order == 'L':
            ci, cj = moveTank(ci, cj, 2)

        elif order == 'R':
            ci, cj = moveTank(ci, cj, 3)

        elif order == 'S':
            toShoot = tank.index(arr[ci][cj])
            shootBomb(ci, cj, toShoot)

    print(f'#{test_case}', end=' ')
    for a in arr:
        print(''.join(a))
