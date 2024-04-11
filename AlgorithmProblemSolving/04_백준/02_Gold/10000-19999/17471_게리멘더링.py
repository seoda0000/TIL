'''
게리맨더링
https://www.acmicpc.net/problem/17471
백준 골드4 17471

백준시는 N개의 구역으로 나누어져 있고, 구역은 1번부터 N번까지 번호가 매겨져 있다.
구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다.
선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다.
중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.

각 선거구는 적어도 하나의 구역을 포함해야 한다.

공평하게 선거구를 나누기 위해 두 선거구에 포함된 인구의 차이를 최소로 하려고 한다. 백준시의 정보가 주어졌을 때, 인구 차이의 최솟값을 구해보자.
'''

import sys


def input():
    return sys.stdin.readline().rstrip()


from itertools import combinations
from collections import deque

N = int(input())
popul = [0] + list(map(int, input().split()))
adjL = [[] for _ in range(N + 1)]  # 1. 인접 리스트 만들기
for n in range(N):
    _, *arg = map(int, input().split())
    for a in arg:
        adjL[n + 1].append(a)
city = list(range(1, N + 1))
combi = []
ans = []
for n in range(1, N):  # 2. 가능한 모든 조합 구하기
    combi += list(combinations(city, n))
for comb1 in combi:
    f = True  # 3. 집합 1의 도시가 모두 연결되어 있는지 확인
    cn = len(comb1)
    q = deque([comb1[0]])
    route = [comb1[0]]
    while q:
        c = q.popleft()
        for a in adjL[c]:
            if a not in route and a in comb1:
                q.append(a)
                route.append(a)
    if cn != 1 and set(comb1) & set(route) != set(comb1):
        f = False

    if f:  # 4. 집합 2의 도시가 모두 연결되어 있는지 확인
        comb2 = list(set(city) - set(comb1))
        q = deque([comb2[0]])
        route = [comb2[0]]
        while q:
            c = q.popleft()
            for a in adjL[c]:
                if a not in route and a in comb2:
                    q.append(a)
                    route.append(a)
        if N - cn != 1 and set(comb2) & set(route) != set(comb2):
            f = False
    if f:  # 5. 인구 차 구하기
        tmp = 0
        tmp2 = 0
        for a in comb1:
            tmp += popul[a]
        for a in comb2:
            tmp2 += popul[a]
        if tmp * tmp2 > 0:
            ans.append(abs(tmp - tmp2))

if ans or N == 1:
    answer = min(ans)
else:
    answer = -1
print(answer)

"""
1년 후 풀이
"""

from collections import deque, defaultdict
import sys

input = sys.stdin.readline


def make_union_one(n, union_one):  # 1과 같은 선거구 뽑기
    global ans
    if n == N + 1:
        # 1 선거구 연결되어 있는지 확인
        if not check_nearby(union_one): return
        p = sum([population[o] for o in union_one])
        if abs(P - p - p) < ans:
            # 2 선거구 연결되어 있는지 확인
            union_two = list(ALL - set(union_one))
            if check_nearby(union_two):
                ans = abs(P - p - p)
        return

    make_union_one(n + 1, union_one)
    make_union_one(n + 1, union_one + [n])


def check_nearby(union):  # 선거구끼리 다 이어져 있는지 확인
    v = [-1] * (N + 1)
    for city in union:
        v[city] = 0

    q = deque([union[0]])
    v[union[0]] = 1

    while q:
        c = q.popleft()

        for city in dic[c]:
            if v[city]: continue
            v[city] = 1
            q.append(city)

    return v.count(1) == len(union)


N = int(input())
ALL = set(range(1, N + 1))
population = [0] + list(map(int, input().split()))
P = sum(population)
dic = defaultdict(list)
for n in range(1, N + 1):
    ipt = list(map(int, input().split()))
    if ipt[0] > 0:
        dic[n] = ipt[1:]
INF = 100 * 10 + 1
ans = INF

make_union_one(2, [1])

if ans == INF:
    print(-1)
else:
    print(ans)
