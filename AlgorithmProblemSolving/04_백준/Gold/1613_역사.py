"""
https://www.acmicpc.net/problem/1613
역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.
"""

import sys
input = sys.stdin.readline

def f(p, t):
    global ans
    if p == 0:
        return 1
    if pre[p] == t:
        ans = num
        return -1
    else:
        f(pre[p], t)

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]
pre = [0]*(N+1)
num = 0

for k in range(K):
    a, b = lst[k]
    if pre[b] == 0:
        pre[b] = a
    else:
        if not f(pre[b], a):
            pre[b] = a

S = int(input())
qlst  = [list(map(int, input().split())) for _ in range(S)]
for s in range(S):
    ans = 0
    num = 1
    f(qlst[s][0], qlst[s][1])
    if ans == 0:
        num = -1
        f(qlst[s][1], qlst[s][0])
    print(ans)
