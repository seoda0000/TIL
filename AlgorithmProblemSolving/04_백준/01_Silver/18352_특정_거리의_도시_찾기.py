"""
https://www.acmicpc.net/problem/18352
백준 실버2 18352 특정 거리의 도시 찾기
"""

import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
routes = [list() for _ in range(N + 1)]
INF = 1000_001
for _ in range(M):
    s, e = map(int, input().split())
    routes[s].append(e)
v = [0] * (N + 1)
costs = [INF] * (N + 1)
costs[X] = 0
cur = X
ans = []
while True:
    v[cur] = 1
    for r in routes[cur]:
        if v[r]: continue
        if costs[r] > costs[cur] + 1:
            costs[r] = costs[cur] + 1

    mnc = INF
    nxt = 0
    for n in range(1, N + 1):
        if v[n]: continue
        if costs[n] < mnc:
            nxt = n
            mnc = costs[n]  # 최소값 갱신 잊지마

    if nxt:
        if costs[nxt] > K:  # 가능성 없음
            break
        elif costs[nxt] == K:
            ans.append(nxt)
        cur = nxt

    else:
        break

if ans:
    ans.sort()
    print(*ans, sep="\n")
else:
    print(-1)

"""
heapq 이용
"""
import heapq


def find_route_K(cur):
    q = []
    while True:
        v[cur] = 1
        for r in routes[cur]:
            if v[r]: continue
            heapq.heappush(q, (costs[cur] + 1, r))
        cur = 0
        while q:
            cost, nxt = heapq.heappop(q)
            if v[nxt]: continue
            if cost > K: return  # 가능성 없음
            if cost == K:
                ans.append(nxt)
            costs[nxt] = cost
            cur = nxt
            break
        if not cur:
            return
    return


N, M, K, X = map(int, input().split())
routes = [list() for _ in range(N + 1)]
INF = -1
for _ in range(M):
    s, e = map(int, input().split())
    routes[s].append(e)
v = [0] * (N + 1)
costs = [INF] * (N + 1)
costs[X] = 0

ans = []

find_route_K(X)
ans.sort()
if ans:
    print(*ans, sep="\n")
else:
    print(-1)

"""
bfs 이용
쉽게 풀자...
"""
from collections import deque

N, M, K, X = map(int, input().split())
routes = [list() for _ in range(N + 1)]
INF = 1000_001
for _ in range(M):
    s, e = map(int, input().split())
    routes[s].append(e)

v = [0] * (N + 1)
v[X] = 1
ans = []
q = deque([(0, X)])

while q:
    cost, cur = q.popleft()
    if cost == K:
        ans.append(cur)
    elif cost > K:
        break

    for nxt in routes[cur]:
        if v[nxt]: continue
        v[nxt] = 1
        q.append((cost + 1, nxt))

if ans:
    ans.sort()
    print(*ans, sep="\n")
else:
    print(-1)
