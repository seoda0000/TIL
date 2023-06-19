"""
https://www.acmicpc.net/problem/15686
백준 골드5 치킨 배달
"""


import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))
        elif arr[i][j] == 1:
            houses.append((i, j))

answer = N**4

# 치킨집 중 M개 골라서 각 집마다 최단거리 구하기
for comb in combinations(range(len(chickens)), M):
    ans = 0
    for h in houses:
        routes = N*N
        for c in comb:
            r = abs(h[0] - chickens[c][0]) + abs(h[1] - chickens[c][1])
            if routes > r:
                routes = r
        ans += routes
    answer = min(ans, answer)
print(answer)