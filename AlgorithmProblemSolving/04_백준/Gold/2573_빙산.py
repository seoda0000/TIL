"""
https://www.acmicpc.net/problem/2573
백준 골드4 2573 빙산

"""


def meltIce():  # 녹은 후 빙산 return
    newArr = [[0] * M for _ in range(N)]

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if arr[i][j] > 0:
                zeroCnt = 0
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if arr[ni][nj] == 0:
                        zeroCnt += 1
                newArr[i][j] = max(0, arr[i][j] - zeroCnt)

    return newArr


def searchIce(si, sj, v):  # (si, sj)와 같은 빙산 v 표시

    q = [(si, sj)]

    while q:
        ci, cj = q.pop()
        v[ci][cj] = 1

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if arr[ni][nj] > 0 and v[ni][nj] == 0:
                q.append((ni, nj))

    return


def countIce():  # 빙산 개수 return
    cnt = 0
    v = [[0] * M for _ in range(N)]

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if arr[i][j] > 0 and v[i][j] == 0:
                searchIce(i, j, v)
                cnt += 1

    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0
t = 1
while True:
    # 녹이기
    arr = meltIce()

    # 빙산 개수 세기
    cnt = countIce()
    if cnt >= 2:
        print(t)
        break
    elif cnt == 0:
        print(0)
        break
    t += 1
