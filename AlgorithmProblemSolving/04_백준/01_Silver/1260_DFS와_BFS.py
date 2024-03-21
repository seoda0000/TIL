'''
DFS와 BFS
https://www.acmicpc.net/problem/1260
백준 실버2 1260

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
'''


def dfs(n):
    for i in sorted(arr[n]):
        if v[i] == 0:
            v[i] = 1
            d.append(i)
            dfs(i)


def bfs(s):
    q = [s]
    while q:
        n = q.pop(0)
        for i in sorted(arr[n]):
            if v[i] == 0:
                v[i] = 1
                b.append(i)
                q.append(i)





N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
d = [V]
b = [V]
v = [0] * (N+1)
v[V] = 1
dfs(V)
v = [0] * (N+1)
v[V] = 1
bfs(V)
print(*d)
print(*b)