import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(i, cnt):
    global dist, end, mnT

    if dist < cnt:
        dist = cnt
        end = i
        mnT = visited[i]
    elif dist == cnt and visited[i] < mnT:
        end = i
        mnT = visited[i]

    for g in range(N+1):
        if graph[i][g] != 0 and visited[g] == -1:
            visited[g] = visited[i] + graph[i][g]
            dfs(g, cnt + 1)


N, T = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    graph[A][B] = graph[B][A] = C


dist, end, mnT = 0, 1, 100000**50000 + 1
visited = [-1] * (N+1)
visited[0] = 0
dfs(1, 1)

visited = [-1] * (N+1)
dist, mnT = 0, 100000**50000 + 1
visited[end] = 0
dfs(end, 1)
print(mnT // T + int(mnT%T!=0))