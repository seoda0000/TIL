"""
https://www.acmicpc.net/problem/1967
백준 골드4 1967 트리의 지름

트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다.
트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다.
이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오.
아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

트리의 노드는 1부터 n까지 번호가 매겨져 있다.

"""

"""
언제나 이진 트리가 아닐 가능성을 고려하자
"""

import sys

sys.setrecursionlimit(10 ** 5)


def dfs(now, length):
    global ans, far

    flag = 0
    for i in range(len(tree[now])):
        node, h = tree[now][i]
        if v[node] == 0 and node > 0:
            flag = 1
            v[node] = 1
            dfs(node, length + h)
            v[node] = 0
    if flag == 0:
        if ans <= length:
            far = now
            ans = length


N = int(input())
lines = [list(map(int, input().split())) for _ in range(N - 1)]
tree = [list() for _ in range(N + 1)]

for line in lines:
    p, c, h = line
    tree[c].append((p, h))
    tree[p].append((c, h))

v = [0] * (N + 1)

v[1] = 1
ans = far = 0
dfs(1, 0)
start = far

v[1], v[start] = 0, 1
ans = far = 0
dfs(start, 0)

print(ans)
