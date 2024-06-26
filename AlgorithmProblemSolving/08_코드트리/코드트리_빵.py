"""
실행시간: 201- > 209
풀이시간: 61분 -> 37분

기존엔 시작 방향을 들고 q에 들어갔는데, 이번에는 끝에서부터 시작점으로 향하고, 도착 시에 마지막 방향의 반대 방향을 리스트에 넣어줬다. (택민 프로님 코드 참고)
응용하기 좋은 아이디어 같다!
이동할 수 없는 조건을 명확히(==) 쓰는 게 좋은 것 같다.
"""

"""
4:19 시작
4:23 구상 완료
4:41 1차 구현 완료
4:56 디버깅 완료 - id, k 혼동
"""

from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_close_camp(si, sj):
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    q = deque([(si, sj)])
    camps = []

    while True:
        nq = len(q)
        for _ in range(nq):
            ci, cj = q.popleft()
            if arr[ci][cj] == 1:  # 캠프
                camps.append((ci, cj))
            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if OOB(ni, nj): continue
                if arr[ni][nj] == -1: continue  # 벽
                if v[ni][nj]: continue

                v[ni][nj] = 1
                q.append((ni, nj))

        if camps: break

    camps.sort()

    return camps[0]


def find_first_dir(si, sj, ei, ej):
    v = [[0] * N for _ in range(N)]
    v[ei][ej] = 1
    q = deque([(ei, ej)])

    d_lst = []

    while True:
        nq = len(q)
        flag = False
        for _ in range(nq):
            ci, cj = q.popleft()
            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if OOB(ni, nj): continue
                if ni == si and nj == sj:
                    d_lst.append(oppo[d])
                    flag = True
                    continue
                if arr[ni][nj] == -1: continue  # 벽
                if v[ni][nj]:
                    continue

                else:
                    v[ni][nj] = 1
                    q.append((ni, nj))
        if flag:
            break
    d_lst.sort()
    return d_lst[0]


di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
oppo = {0: 3, 3: 0, 1: 2, 2: 1}
N, ppl_cnt = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 0 빈 공간 1 베이스 캠프 -1 벽
store_dic = dict()  # 사람 id: 가고 싶은 편의점 좌표
ppl_dic = dict()  # 사람 id: 현재 위치
for id in range(1, ppl_cnt + 1):
    x, y = map(int, input().split())
    store_dic[id] = (x - 1, y - 1)

k = 0
while True:

    k += 1
    # 사람들 이동
    stores_to_walls = []
    item_lst = list(ppl_dic.items())
    for id, value in item_lst:
        ei, ej = store_dic[id]  # 편의점 좌표
        si, sj = ppl_dic[id]  # 편의점 좌표
        d = find_first_dir(si, sj, ei, ej)
        ni, nj = si + di[d], sj + dj[d]
        if ni == ei and nj == ej:  # 도착
            stores_to_walls.append((ei, ej))
            ppl_dic.pop(id)
        else:
            ppl_dic[id] = (ni, nj)

    # 도착한 편의점이 벽이 된다
    for i, j in stores_to_walls:
        arr[i][j] = -1

    # 베이스 캠프에 등장
    if k <= ppl_cnt:
        ei, ej = store_dic[k]  # 편의점 좌표
        ci, cj = find_close_camp(ei, ej)
        ppl_dic[k] = (ci, cj)
        arr[ci][cj] = -1  # 도착한 베이스 캠프가 벽이 된다

    if len(ppl_dic) == 0:
        break

print(k)

"""
3:00 시작
3:11 구상 완료
3:39 1차 구현 완료
3:58 98퍼 메모리 초과
4:01 방문 체크 로직 누락 해결 -> 제출

<실수한 부분>
bfs에서 방문체크 로직을 빼먹어서 메모리 초과가 났다.
98퍼까지 돌아간 게 기적이다... 이전에 한 실수인데 방심하자마자 바로 했다.
bfs 방문체크는 누락해도 코드가 돌아가서 깨닫기 어렵다. 잊지 말자ㅠㅠ!!

"""
from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def choose_camp(arr, t):  # t번째 사람의 목표지점에서 가장 가까운 베이스 캠프 위치 return
    si, sj = store_dic[t]  # 목표지점에서 시작

    v = [[0] * N for _ in range(N)]
    q = deque([(si, sj)])
    v[si][sj] = 1

    k = -1  # 거리
    camps = []  # 최단거리 캠프 좌표 리스트
    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            if arr[ci][cj] == CAMP:  # 캠프
                camps.append((ci, cj))

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if OOB(ni, nj): continue
                if arr[ni][nj] == WALL: continue
                if v[ni][nj]: continue

                v[ni][nj] = 1
                q.append((ni, nj))

        if camps: break

    camps.sort()
    ci, cj = camps[0]  # 우선순위 고려하여 캠프 선정
    arr[ci][cj] = WALL  # 접근금지

    return ci, cj


def go_to_store(t):  # t번째 사람이 편의점을 향해 이동 후 편의점 도착 여부 return
    si, sj = person_dic[t]
    ei, ej = store_dic[t]

    v = [[0] * N for _ in range(N)]
    q = deque([(si, sj, -1)])  # 좌표, 시작 방향
    v[si][sj] = 1

    direction = -1  # 최초 이동방향
    while q:
        ci, cj, cd = q.popleft()

        if ci == ei and cj == ej:  # 도착
            direction = cd
            break

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if OOB(ni, nj): continue
            if arr[ni][nj] == WALL: continue
            if v[ni][nj]: continue

            v[ni][nj] = 1
            if cd < 0:  # 최초 이동
                q.append((ni, nj, d))
            else:
                q.append((ni, nj, cd))

    ni, nj = si + di[direction], sj + dj[direction]
    person_dic[t] = (ni, nj)  # 이동

    return (ni == ei and nj == ej)  # 편의점 도착 여부


CAMP, WALL = 1, -1
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
N, person_cnt = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
store_dic = dict()
person_dic = dict()
for t in range(1, person_cnt + 1):
    x, y = map(int, input().split())
    store_dic[t] = (x - 1, y - 1)

cur = 0  # 현재 시간
while True:

    # 1번 행동: 이동
    is_done = True  # 모든 사람이 도착했는지
    arrived_lst = []  # 이번에 도착한 편의점 목록
    remain_lst = list(person_dic.keys())  # 이동해야 할 사람 목록

    for t in remain_lst:
        if go_to_store(t):  # 만약 이동 후 도착했다면 -> 표기 및 목록 제거

            arrived_lst.append(t)
            person_dic.pop(t)
        is_done = False

    # 2번 행동: 도달한 편의점이 벽이 된다
    for t in arrived_lst:
        si, sj = store_dic[t]
        arr[si][sj] = WALL

    if cur > person_cnt and is_done:  # 완료 시 종료
        break

    cur += 1
    # 3번 행동: cur번째 사람이 등장
    if cur <= person_cnt:
        ci, cj = choose_camp(arr, cur)
        person_dic[cur] = (ci, cj)

print(cur)
