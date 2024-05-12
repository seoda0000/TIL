"""
https://www.acmicpc.net/problem/16946
백준 골드2 벽 부수고 이동하기 4

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.

각각의 벽에 대해서 다음을 구해보려고 한다.

벽을 부수고 이동할 수 있는 곳으로 변경한다.
그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
"""

from collections import deque


def checkBlank(si, sj, id, v):  # 0인 칸에 id와 cnt 체크
    lst = [(si, sj)]
    v[si][sj][0] = id
    p = 0
    while p < len(lst):
        ci, cj = lst[p]
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue  # 범위 밖
            if arr[ni][nj]: continue  # 0이 아니다
            if v[ni][nj][0]: continue  # 이미 id 체크한 빈칸

            v[ni][nj][0] = id
            lst.append((ni, nj))
        p += 1
    cnt = len(lst)
    for blank in lst:
        bi, bj = blank
        v[bi][bj][1] = cnt

    return


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[[0, 0] for _ in range(M)] for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
id = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and v[i][j][0] == 0:
            checkBlank(i, j, id, v)
            id += 1

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cnt = 0
            idLst = []
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if not (0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0): continue
                bId, bCnt = v[ni][nj]
                if bId not in idLst:
                    idLst.append(bId)
                    cnt += bCnt
            arr[i][j] = (cnt + 1) % 10

for row in arr:
    for r in row:
        print(r, end='')
    print()
