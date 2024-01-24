"""
https://www.acmicpc.net/problem/10026
백준 10026 골드5 적록색약
"""


def findGeneral(color, i, j):
    global ansG

    vG[i][j] = 1

    q = [(i, j)]
    while q:
        a, b = q.pop(0)
        for n in range(4):
            na, nb = a + di[n], b + dj[n]
            if na < 0 or na >= N or nb < 0 or nb >= N or vG[na][nb] == 1:
                continue
            if arr[na][nb] == color:
                vG[na][nb] = 1
                q.append((na, nb))
    ansG += 1
    return


def findColor(color, i, j):
    global ansC

    vC[i][j] = 1

    color = (color == 'B')

    q = [(i, j)]
    while q:
        a, b = q.pop(0)
        for n in range(4):
            na, nb = a + di[n], b + dj[n]
            if na < 0 or na >= N or nb < 0 or nb >= N or vC[na][nb] == 1:
                continue
            if (arr[na][nb] == 'B') == color:
                vC[na][nb] = 1
                q.append((na, nb))
    ansC += 1


N = int(input())
arr = [input() for _ in range(N)]
vG = [[0] * N for _ in range(N)]
vC = [[0] * N for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ansG = ansC = 0
for i in range(N):
    for j in range(N):
        color = arr[i][j]
        if vG[i][j] == 0:
            findGeneral(color, i, j)
        if vC[i][j] == 0:
            findColor(color, i, j)

print(ansG, ansC)
