"""
https://www.acmicpc.net/problem/2638
백준 골드3 2638 치즈
"""

from collections import deque


def checkOuterAir():  # 바깥공기를 2로 체크한다
    arr[0][0] = 2

    while airQ:
        ci, cj = airQ.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == 0:
                arr[ni][nj] = 2
                airQ.append((ni, nj))

    return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
airQ = deque([(0, 0)])  # 바깥공기 큐
checkOuterAir()

q = deque()  # 치즈위치 큐
t = 0
for i in range(N):  # 치즈 위치를 큐에 넣어준다
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    nq = len(q)
    t += 1
    nxtAir = []  # 직후 공기가 될 치즈 리스트

    for _ in range(nq):
        ci, cj = q.popleft()
        cnt = 0  # 인접한 공기의 수
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == 2:
                airQ.append((ni, nj))  # 치즈와 인접한 공기만 바깥공기 큐에 넣는다
                cnt += 1
        if cnt >= 2:
            nxtAir.append((ci, cj))
        else:
            q.append((ci, cj))

    for i, j in nxtAir:  # 치즈가 녹으면 바깥공기가 된다
        arr[i][j] = 2
        airQ.append((i, j))

    checkOuterAir()  # 바깥공기 확장

print(t)
