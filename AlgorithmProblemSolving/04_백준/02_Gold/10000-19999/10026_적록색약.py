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

"""
비트마스킹을 이용한 풀이
"""

def viewColor(si: int, sj: int, isBlue: bool):  # 적록색약의 영역 구분
    stk = [(si, sj)]
    v[si][sj] |= 1  # 1 표시
    while stk:
        ci, cj = stk.pop(0)
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if arr[ni][nj] == '.': continue  # 가장자리 제거
            if (arr[ni][nj] == 'B') == isBlue and (not v[ni][nj] & 1):
                v[ni][nj] |= 1  # 1 표시
                stk.append((ni, nj))
    return


def viewOther(si: int, sj: int, c: str):  # 일반인의 영역 구분
    stk = [(si, sj)]
    v[si][sj] |= 2  # 2 표시
    while stk:
        ci, cj = stk.pop(0)
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if arr[ni][nj] == c and (not v[ni][nj] & 2):
                v[ni][nj] |= 2  # 2 표시
                stk.append((ni, nj))
    return


N = int(input()) + 2
arr = ['.' * N] + ['.' + input() + '.' for _ in range(N - 2)] + ['.' * N]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
v = [[0] * N for _ in range(N)]
ansColor = ansOther = 0

for i in range(1, N - 1):
    for j in range(1, N - 1):
        if v[i][j] == 3: continue  # 검토 완료
        if not v[i][j] & 1:  # 적록색약 검토 필요
            viewColor(i, j, arr[i][j] == 'B')
            ansColor += 1
        if not v[i][j] & 2:  # 일반인 검토 필요
            viewOther(i, j, arr[i][j])
            ansOther += 1

print(ansOther, ansColor)
