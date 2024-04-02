"""
실행시간: 152 -> 152
풀이시간: 31분 -> 14분

로봇 표시(9)를 지우지 않아서 몬스터처럼 처리하는 실수가 있었다.
긴장감 없이 풀어서 사소한 실수가 많이 생기는 것 같다... 집중하자 집중
이외 풀이는 완전히 동일하다

"""

"""
3:43 시작
3:46 구상 완료
3:55 구현 완료
3:57 디버깅: 로봇 표시 제거
"""

from collections import deque


def find_monster(ri, rj):
    v = [[0] * N for _ in range(N)]
    v[ri][rj] = 1
    q = deque([(ri, rj)])

    monsters = []

    k = -1
    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            if 0 < arr[ci][cj] < level:  # 없앨 수 있는 몬스터 발견
                monsters.append((ci, cj))

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]

                if not (0 <= ni < N and 0 <= nj < N): continue
                if arr[ni][nj] > level: continue
                if v[ni][nj]: continue

                v[ni][nj] = 1
                q.append((ni, nj))

        if monsters:
            break

    if monsters:
        monsters.sort()
        ni, nj = monsters[0]
        return ni, nj, k
    else:
        return -1, -1, -1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if 9 not in arr[i]: continue
    ri, rj = i, arr[i].index(9)
    arr[ri][rj] = 0
    break

t = 0
level = 2
exp = 0
while True:
    ni, nj, nt = find_monster(ri, rj)
    if ni < 0: break  # 몬스터 없다

    ri, rj = ni, nj
    arr[ri][rj] = 0
    t += nt
    exp += 1

    if exp == level:
        level += 1
        exp = 0

print(t)

"""
09:40~09:51 구상
09:51~10:00 1차 구현
10:00~10:11 디버깅 및 제출

<실수한 부분>
구상할 때 두가지 방법을 생각했는데, 귀찮은 방법과 게으른 방법이다...
게으른 방법을 선택했다가 틀렸다!
구상은 일단 최대로 보수적으로 하고, 이후에 최적화를 하자!
"""
from collections import deque


def find_monster(si, sj, arr):
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    q = deque([(si, sj, 0)])

    monsters = []
    mnk = -1
    while q:
        ci, cj, ck = q.popleft()

        if 0 < arr[ci][cj] < lv:  # 몬스터 찾음
            if mnk < 0:  # 첫번째로 조건 충족한 몬스터
                monsters.append((ci, cj, ck))
                mnk = ck  # 최단거리
            else:
                if ck == mnk:  # 기존과 같은 거리면 리스트에 추가
                    monsters.append((ci, cj, ck))
                else:  # 기존보다 먼 거리면 탐색 종료
                    break

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < N): continue
            if v[ni][nj]: continue
            if arr[ni][nj] > lv: continue

            v[ni][nj] = 1
            q.append((ni, nj, ck + 1))

    if monsters:  # 몬스터 찾음 -> 조건에 맞는 몬스터 찾아서 없애기
        monsters.sort()
        mi, mj, mk = monsters[0]
        arr[mi][mj] = 0
        return mi, mj, mk
    return -1, -1, -1  # 몬스터 못 찾음


di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            ri, rj = i, j
            arr[i][j] = 0
            break
lv = 2
exp = 0
t = 0
while True:
    ri, rj, c_time = find_monster(ri, rj, arr)
    if c_time < 0:  # 몬스터 못 찾음
        break
    else:
        t += c_time
        exp += 1
        if exp == lv:
            lv += 1
            exp = 0
print(t)
