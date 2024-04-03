
"""
20:46 시작
20:48 구상 완료
21:00 구현 완료
21:05 디버깅 완료
"""
from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_near_cus(ti, tj):
    v = [[0] * N for _ in range(N)]
    q = deque([(ti, tj)])
    v[ti][tj] = 1
    k = -1
    customers = []
    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            if cus_arr[ci][cj]:
                customers.append((ci, cj))

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if OOB(ni, nj): continue
                if v[ni][nj]: continue
                if board[ni][nj]: continue  # 벽

                v[ni][nj] = 1
                q.append((ni, nj))

        if customers:
            break

    if customers:
        customers.sort()
        ci, cj = customers[0]
        return ci, cj, k
    return -1, -1, -1


def go_to(ti, tj, ei, ej):
    v = [[0] * N for _ in range(N)]
    q = deque([(ti, tj)])
    v[ti][tj] = 1
    k = -1
    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            if ci == ei and cj == ej:
                return k

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if OOB(ni, nj): continue
                if v[ni][nj]: continue
                if board[ni][nj]: continue  # 벽

                v[ni][nj] = 1
                q.append((ni, nj))

    return -1


INF = 20 * 20 + 1
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, cus_cnt, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # 0 길 # 1 벽
cus_arr = [[0] * N for _ in range(N)]
cus_dic = dict()
ti, tj = map(int, input().split())
ti -= 1
tj -= 1

for id in range(1, cus_cnt + 1):
    si, sj, ei, ej = map(int, input().split())
    cus_arr[si - 1][sj - 1] = id
    cus_dic[id] = (ei - 1, ej - 1)

while True:
    ci, cj, need_fuel = find_near_cus(ti, tj)  # 가장 가까운 손님 위치, 그때의 필요 연료량 구하기

    if need_fuel < 0 or need_fuel > fuel:
        break

    fuel -= need_fuel  # 이동
    ti, tj = ci, cj

    ei, ej = cus_dic[cus_arr[ti][tj]]

    cus_arr[ci][cj] = 0
    need_fuel = go_to(ti, tj, ei, ej)  # 필요 연료량 구하기

    if need_fuel < 0 or need_fuel > fuel:
        break
    fuel += need_fuel
    cus_cnt -= 1
    ti, tj = ei, ej

if cus_cnt:
    print(-1)
else:
    print(fuel)
