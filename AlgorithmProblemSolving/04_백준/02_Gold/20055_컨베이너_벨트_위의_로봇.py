import sys

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
points = list(map(int, input().split()))

s = 0 # 올리는 곳
e = N - 1 # 내리는 곳

t = 0
robots = deque() # 로봇 리스트
v = [0] * 2 * N # 로봇의 현 위치 표기

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

        nr = r + 1 # 로봇의 다음 위치
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
