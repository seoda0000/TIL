from collections import defaultdict
import sys
sys.setrecursionlimit(10**4)

def calUsado(cur):
    for r, nxt in usadoDic[cur]:
        if v[nxt]: continue
        if r < K:
            continue
        else:
            v[nxt] = 1
            calUsado(nxt)
    return


N, Q = map(int, input().split())
usadoDic = defaultdict(list)
for _ in range(N - 1):
    p, q, r = list(map(int, input().split()))
    usadoDic[p].append((r, q))
    usadoDic[q].append((r, p))

for _ in range(Q):
    K, V = map(int, input().split())
    v = [0] * (N + 1)
    v[V] = 1
    calUsado(V)
    print(sum(v) - 1)
