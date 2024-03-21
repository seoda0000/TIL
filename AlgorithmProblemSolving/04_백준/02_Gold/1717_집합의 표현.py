"""
https://www.acmicpc.net/problem/1717
백준 골드5 1717 집합의 표현
"""


import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def union(a, b):
    p[find(a)] = find(b)
    return


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


N, M = map(int, input().split())
p = list(range(N + 1))
for _ in range(M):
    w, a, b = map(int, input().split())
    if w:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
