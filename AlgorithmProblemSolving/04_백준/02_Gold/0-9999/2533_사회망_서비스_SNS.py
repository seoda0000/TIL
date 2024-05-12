import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def check(cur):
    dp = [1, 0]  # [얼리어답터, 일반인]
    for c in routes[cur]:
        if v[c]: continue
        v[c] = 1
        dp_c = check(c)
        dp[0] += min(dp_c)
        dp[1] += dp_c[0]
    return dp


N = int(input())
routes = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    routes[a].append(b)
    routes[b].append(a)

v = [0] * (N + 1)
v[1] = 1

print(min(check(1)))
