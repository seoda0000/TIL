"""
https://www.acmicpc.net/problem/1865

백준 골드3 1865 웜홀

때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
(단 도로는 방향이 없으며 웜홀은 방향이 있다.)
웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.
웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다.
한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.
여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.
"""
"""
시간 초과 코드
"""

import sys

input = sys.stdin.readline


def comeBack(sn, st):
    startCheck[sn] = 1
    for r in routes[sn]:
        nxt, t = r
        if v[nxt] > st + t:
            if v[nxt] != INF: return True
            v[nxt] = st + t
            if comeBack(nxt, st + t): return True
            v[nxt] = INF
    return False


TC = int(input())
for tc in range(TC):
    N, M, W = map(int, input().split())
    routes = [list() for _ in range(N + 1)]
    startCheck = [0] * (N + 1)
    INF = 10001 * (M + W)
    for _ in range(M):
        s, e, t = map(int, input().split())
        routes[s].append((e, t))
        routes[e].append((s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        routes[s].append((e, -t))

    for n in range(1, N + 1):
        if startCheck[n]: continue
        v = [INF] * (N + 1)
        v[n] = 0
        if comeBack(n, 0):
            print('YES')
            break
        v[n] = INF
    else:
        print('NO')

"""
벨만 포드 알고리즘을 이용해야 한다
"""
import sys

input = sys.stdin.readline


def comeBack(sn):
    shortcut[sn] = 0
    for i in range(N):
        for r in routes:
            s, e, t = r
            if shortcut[e] > shortcut[s] + t:
                shortcut[e] = shortcut[s] + t
                if i == N - 1:
                    return True

    return False


TC = int(input())
for tc in range(TC):
    N, M, W = map(int, input().split())
    routes = []
    INF = 10001 * (M + W)
    for _ in range(M):
        s, e, t = map(int, input().split())
        routes.append((s, e, t))
        routes.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        routes.append((s, e, -t))

    shortcut = [INF] * (N + 1)
    if comeBack(1):
        print('YES')
    else:
        print('NO')
