"""
9:05 시작
9:12 구상 완료
9:24 구현 완료

q에 넣는 코드를 깜빡해서 디버깅해서 잡았다
진짜 뭐지... 테케 돌리기 전에 설계 보면서 검토 한번 하자
"""
from collections import deque


def bfs(si, sj, arr):  # 계란 이동이 있을 경우 이동 후 True return
    v[si][sj] = 1
    q = deque([(si, sj)])
    egg_box = [(si, sj)]  # 현재 상자에 포함된 칸들
    box_cnt = arr[si][sj]  # 현재 상자에 포함된 총 계란 수
    while q:
        ci, cj = q.popleft()
        ccnt = arr[ci][cj]

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if v[ni][nj]: continue

            ncnt = arr[ni][nj]
            if not (L <= abs(ccnt - ncnt) <= R): continue

            v[ni][nj] = 1
            q.append((ni, nj))
            egg_box.append((ni, nj))
            box_cnt += ncnt

    if len(egg_box) > 1:  # 이동
        egg_cnt = box_cnt // len(egg_box)

        for ei, ej in egg_box:
            arr[ei][ej] = egg_cnt
        return True
    else:  # 이동 안함
        return False


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

t = 0
while True:
    v = [[0] * N for _ in range(N)]

    move = False

    for i in range(N):
        for j in range(N):
            if v[i][j]: continue
            if bfs(i, j, arr):
                move = True

    if not move:
        break
    else:
        t += 1

print(t)
