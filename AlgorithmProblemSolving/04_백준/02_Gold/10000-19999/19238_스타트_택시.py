"""
실행시간: 188 -> 240
풀이시간: 40분 -> 19분

INF를 칸의 개수 + 1로 주었는데, fuel이 무한정으로 늘어날 수도 있다는 것을 놓쳤다.
최대값을 줄 때는 꼭 기존보다 더 증가할 수 있는지, 축적할 수 있는지 확인하고 극단적으로 줘야 제대로 갱신이 된다.
이건 한번 더 풀어보면 좋을지도....
"""

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

"""
2:01 시작
2:15 구상 완료
2:25 1차 구현 완료 + 테케 확인 (거리 실수)
2:41 2차 구현 완료

처음엔 si, sj, ei, ej를 한 배열로 관리하려고 했는데, 구현의 편의를 위해 각각 2차원 배열과 딕셔너리로 분리했다.

<실수한 부분>
처음엔 벽을 고려하지 않고 맨하튼 거리로 구했다. bfs 실컷 하고 왜 그랬을까... 방심한 것 같다.
바로 다른 점을 알고 디버깅했다.
문제를 똑바로!! 읽자 방심하지 말자
"""

from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def find_next_customer(ti, tj, fuel):  # ti, tj에서 fuel의 연료로 갈 수 있는 거리 중 최단거리 손님 찾기
    v = [[0] * (N + 2) for _ in range(N + 2)]
    v[ti][tj] = 1
    q = deque([(ti, tj)])
    customers = []
    k = -1  # 거리
    while q:
        k += 1
        nq = len(q)

        if k > fuel:  # 연료가 없다
            return -1, -1, -1

        for _ in range(nq):
            ci, cj = q.popleft()

            if C_MAP[ci][cj]:  # 손님 발견
                customers.append((ci, cj))

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]

                if v[ni][nj]: continue
                if arr[ni][nj]: continue

                v[ni][nj] = 1
                q.append((ni, nj))

        if customers:  # 최단거리 손님 확인 완료
            break

    if customers:
        customers.sort()  # 손님 선정
        si, sj = customers[0]
        return k, si, sj

    return -1, -1, -1


def drive(ti, tj, ei, ej, fuel):  # ti, tj에서 ei, ej까지 fuel의 연료로 갈 수 있다면, 거리 return
    v = [[0] * (N + 2) for _ in range(N + 2)]
    v[ti][tj] = 1
    q = deque([(ti, tj)])
    k = -1
    while q:
        k += 1
        nq = len(q)

        if k > fuel:  # 연료가 없다
            return -1

        for _ in range(nq):
            ci, cj = q.popleft()

            if ci == ei and cj == ej:  # 도착
                return k

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]

                if v[ni][nj]: continue
                if arr[ni][nj]: continue

                v[ni][nj] = 1
                q.append((ni, nj))

    return -1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, customer_cnt, fuel = map(int, input().split())
arr = [[1] * (N + 2)] \
      + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] \
      + [[1] * (N + 2)]
C_MAP = [[0] * (N + 2) for _ in range(N + 2)]  # 손님 분포 지도
ti, tj = map(int, input().split())
customers = dict()  # 손님 목적지 딕셔너리
id = 0
for _ in range(customer_cnt):
    id += 1
    si, sj, ei, ej = map(int, input().split())
    C_MAP[si][sj] = id  # 출발점은 지도에
    customers[id] = (ei, ej)  # 도착점은 dict에

for _ in range(customer_cnt):
    need_fuel, si, sj = find_next_customer(ti, tj, fuel)  # 가장 가까운 승객 구하기
    if need_fuel < 0:  # 불가능 시 종료
        fuel = -1
        break
    next_customer_idx = C_MAP[si][sj]  # 이번 손님
    C_MAP[si][sj] = 0  # 완료 -> 지도에서 지우기
    ti, tj = si, sj  # 이동
    fuel -= need_fuel  # 연료 소모

    ei, ej = customers[next_customer_idx]  # 이번 손님의 목적지
    need_fuel = drive(ti, tj, ei, ej, fuel)  # 목적지까지의 거리

    if need_fuel < 0:  # 불가능 시 종료
        fuel = -1
        break

    ti, tj = ei, ej  # 가능하면 이동
    fuel += need_fuel  # 이동 성공시 충전

print(fuel)
