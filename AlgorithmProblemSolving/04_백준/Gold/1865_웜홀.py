"""
55%에서 시간초과
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
