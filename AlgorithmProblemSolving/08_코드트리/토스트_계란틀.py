"""
실행시간: 1592 -> 1564
풀이시간: 19분 -> 20분

확실히 하려고 check_v 배열을 따로 팠는데 백준에서 시간초과가 났다...
v 배열의 원리를 찬찬히 파악했다면 굳이 두개를 쓸 필요가 없다.
게으르게 구상하지 말고 v 배열의 원리를 하나하나 파악한 후에 구현하자
"""

"""
14:27 시작
14:30 구상 완료
14:40 구현 완료 및 코드 점검
14:41 제출
14:47 백준 제출
"""

from collections import deque


def move_eggs(si, sj):
    v[si][sj] = 1
    q = deque([(si, sj)])
    egg_lst = [(si, sj)]
    sm = arr[si][sj]

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if v[ni][nj]: continue
            if not (L <= abs(arr[ci][cj] - arr[ni][nj]) <= R): continue

            v[ni][nj] = 1
            q.append((ni, nj))
            egg_lst.append((ni, nj))
            sm += arr[ni][nj]

    if len(egg_lst) > 1:
        new_egg = sm // len(egg_lst)
        for ei, ej in egg_lst:
            arr[ei][ej] = new_egg
        return True

    return False


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

k = 0
while True:
    v = [[0] * N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if v[i][j]: continue
            if move_eggs(i, j):
                move = True
    if not move: break
    k += 1
print(k)

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
