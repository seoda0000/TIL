"""
https://www.acmicpc.net/problem/1753

백준 골드4 1753 최단경로

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(20001)


def dij(now, d):
    v[now] = 1
    relations = list(roads[now].items())
    relations.sort(key=lambda x: x[1])

    for k, itms in relations:
        if mnroads[k] > itms + d:
            mnroads[k] = itms + d

    mnd = INF
    nxtIdx = 0

    for i in range(V + 1):
        if mnroads[i] < mnd and v[i] == 0:
            nxtIdx = i
            mnd = mnroads[i]

    if nxtIdx:
        dij(nxtIdx, mnroads[nxtIdx])
    else:
        return


V, E = map(int, input().split())
K = int(input())
INF = 11 * E
roads = [dict() for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    if roads[u].get(v):
        roads[u][v] = min(roads[u][v], w)
    else:
        roads[u][v] = w

mnroads = [INF] * (V + 1)
v = [0] * (V + 1)
mnroads[K] = 0
dij(K, 0)
for a in mnroads[1:]:
    if a == INF:
        print('INF')
    else:
        print(a)
