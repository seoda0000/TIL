"""
4퍼에서 시간초과
"""
from queue import PriorityQueue


def dij(now, h, lst, routes):
    while not routes[now].empty():
        e, t = routes[now].get()
        if lst[e] > h + t:
            lst[e] = h + t
            dij(e, h + t, lst, routes)


N, M, X = map(int, input().split())
routes1 = [PriorityQueue() for _ in range(N + 1)]
routes2 = [PriorityQueue() for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    routes1[s].put((t, e))
    routes2[s].put((t, e))

INF = M * 101
shortcut = [INF] * (N + 1)
shortcut[X] = 0
dij(X, 0, shortcut, routes1)

for i in range(1, N + 1):
    if i == X: continue
    v = [INF] * (N + 1)
    v[i] = 0
    dij(i, 0, v, routes2)
    shortcut[i] += v[X]
print(max(shortcut[1:]))
