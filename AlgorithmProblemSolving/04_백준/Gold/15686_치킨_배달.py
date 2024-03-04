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


"""
조합 구하기 수제작 코드
"""
def choose_hospital(nth, temp):
    if nth == m + 1:
        check_shortcut(temp[1:])
        return

    for h in range(temp[nth - 1] + 1, Nh):
        temp[nth] = h
        choose_hospital(nth + 1, temp)
        temp[nth] = -1


def check_shortcut(temp):
    global ans

    res = 0
    for c in range(Nc):
        mn = INF

        for idx in temp:
            mn = min(mn, v[c][idx])
        res += mn

    ans = min(ans, res)
    return


N, m = map(int, input().split())
customers = []
hospitals = []
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(N):
        if ipt[j] == 1:
            customers.append((i, j))
        elif ipt[j] == 2:
            hospitals.append((i, j))

Nc = len(customers)
Nh = len(hospitals)
v = [[0] * Nh for _ in range(Nc)]

for c in range(Nc):
    ci, cj = customers[c]
    for h in range(Nh):
        hi, hj = hospitals[h]
        v[c][h] = abs(ci - hi) + abs(cj - hj)

temp = [-1] * (m + 1)
INF = N * N * Nc
ans = INF
choose_hospital(1, temp)
print(ans)
