"""
https://www.acmicpc.net/problem/1613
역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.
"""


# 왜 틀린 건지 확인해야함

import sys
input = sys.stdin.readline

def f(p, t):
    global ans
    if p == 0:
        return True
    if pre[p] == t:
        ans = num
        return False
    else:
        f(pre[p], t)

N, K = map(int, input().split())
pre = [0]*(400+1)
num = 0

for _ in range(K):
    a, b = map(int, input().split())
    if pre[b] == 0:
        pre[b] = a
    else:
        if not f(pre[b], a):
            pre[b] = a

S = int(input())
for _ in range(S):
    ans = 0
    num = 1
    a, b = map(int, input().split())
    f(a, b)
    if ans == 0:
        num = -1
        f(b, a)
    print(ans)
