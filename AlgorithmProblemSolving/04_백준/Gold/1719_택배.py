import sys
input = sys.stdin.readline


def f(i, x, k, w):
    if routes[a][k] > w:
        routes[a][k] = w
        ans[a][k] = x

n, m = map(int, input().split())
# n <= 200, m <= 10000

routes = [[200*10000] * n for _ in range(n)]
ans = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    routes[a][b] = min(routes[a][b], t)
    routes[b][a] = min(routes[b][a], t)
    ans[a][b] = b+1
    ans[b][a] = a+1

# 플로이드 워셜 알고리즘 (점화식 이용 --> DP)
for k in range(n):
    for a in range(n):
        for b in range(n):
            if routes[a][b] > routes[a][k] + routes[k][b]:
                routes[a][b] = routes[a][k] + routes[k][b]
                ans[a][b] = ans[a][k]

for r in range(n):
    ans[r][r] = '-'

for r in range(n):
    print(*ans[r])