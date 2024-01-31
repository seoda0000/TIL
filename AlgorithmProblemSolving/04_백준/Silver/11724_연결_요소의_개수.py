"""
https://www.acmicpc.net/problem/11724
백준 실버2 11724 연결 요소의 개수

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
"""


def search(start):  # start와 연결된 정점의 visited 표시
    q = [start]
    while q:
        now = q.pop()
        for r in routes[now]:
            if v[r] == 0:
                v[r] = 1
                q.append(r)

    return


N, M = map(int, input().split())
routes = [list() for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    routes[s].append(e)
    routes[e].append(s)

v = [0] * (N + 1)
ans = 0
for i in range(1, N + 1):
    if v[i] == 0:  # 방문하지 않았다면 새로운 연결 요소 발견
        v[i] = 1
        search(i)
        ans += 1
print(ans)
