import sys
sys.setrecursionlimit(20001)
def dfs(now, d):

    nxts = list(roads[now].keys())

    for nxt in nxts:
        nd = d + roads[now][nxt]
        if v[nxt] == 0 and mnroads[nxt] > nd:
            v[nxt] = 1
            mnroads[nxt] = nd
            dfs(nxt, d + roads[now][nxt])
            v[nxt] = 0


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
v[K] = 1
mnroads[K] = 0
dfs(K, 0)
for a in mnroads[1:]:
    if a == INF:
        print('INF')
    else:
        print(a)
