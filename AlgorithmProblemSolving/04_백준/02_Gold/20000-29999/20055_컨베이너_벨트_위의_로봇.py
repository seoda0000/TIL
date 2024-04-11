"""
실행시간: 1828(408) -> 1756(272)

이전에는 이차원 배열을 회전하여 풀었다. 이후에는 인덱스를 이동시키며 풀었다.
이번에는 deque를 이용해 배열 자체를 회전시켰다. 훨씬 오래 걸리지만 직관적이다.
-> list를 이용했더니 훨씬 빨라졌다. 값의 수정이 있기 때문에 연결 리스트는 오래 걸리는 것 같다.
"""

"""
9:06 시작
9:10 구상 완료
9:19 1차 구현 완료
"""

from collections import deque

N, K = map(int, input().split())
safety_lst = list(map(int, input().split()))
ppl_lst = [0] * N

turn = 0
while True:
    turn += 1
    # 한칸 회전한다
    ppl_lst.insert(0, ppl_lst.pop())
    safety_lst.insert(0, safety_lst.pop())

    # n-1번칸 확인
    ppl_lst[N - 1] = 0

    # 사람이 이동한다
    for i in range(N - 1)[::-1]:
        if ppl_lst[i]:  # 사람 있음
            if not (ppl_lst[i + 1] or safety_lst[i + 1] == 0):  # 이동 가능
                ppl_lst[i] = 0
                ppl_lst[i + 1] = 1
                safety_lst[i + 1] -= 1

    # n-1번칸 확인
    ppl_lst[N - 1] = 0

    # 0번칸에 사람 올린다
    if not (ppl_lst[0] or safety_lst[0] == 0):
        ppl_lst[0] = 1
        safety_lst[0] -= 1

    if safety_lst.count(0) >= K:
        break

print(turn)

"""
한달 전 풀이
"""
import sys

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
points = list(map(int, input().split()))

s = 0  # 올리는 곳
e = N - 1  # 내리는 곳

t = 0
robots = deque()  # 로봇 리스트
v = [0] * 2 * N  # 로봇의 현 위치 표기

while True:
    t += 1

    s, e = s - 1, e - 1
    if s < 0:
        s = 2 * N - 1
    if e < 0:
        e = 2 * N - 1

    nq = len(robots)

    for _ in range(nq):
        r = robots.popleft()
        if r == e:
            v[r] = 0
            continue

        nr = r + 1  # 로봇의 다음 위치
        if nr >= 2 * N:
            nr = 0

        if v[nr]:
            robots.append(r)
            continue

        if points[nr] == 0:
            robots.append(r)
            continue

        points[nr] -= 1
        v[r] = 0

        if nr == e:
            continue
        else:
            v[nr] = 1
            robots.append(nr)

    if points[s]:
        robots.append(s)
        v[s] = 1
        points[s] -= 1

    zero_cnt = points.count(0)

    if zero_cnt >= K:
        break

print(t)
