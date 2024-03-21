"""
백준 실버1 1325
https://www.acmicpc.net/problem/1325

해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다.
이 회사는 N개의 컴퓨터로 이루어져 있다.
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때,
한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
trust = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    trust[b].append(a)

ans = [0] * (N+1)
mx = 0
mx_lst = []
for i in range(1, N+1):
    if len(trust[i]) == 0:
        continue
    v = [0] * (N+1)
    v[i] = 1
    q = deque([i])
    while q:
        ti = q.popleft()
        ans[i] += 1
        for a in trust[ti]:
            if v[a] == 0:
                q.append(a)
                v[a] = 1


    if ans[i] > mx:
        mx_lst.clear()
        mx = ans[i]
        mx_lst.append(i)
    elif ans[i] == mx:
        mx_lst.append(i)

for m in mx_lst:
    sys.stdout.write(str(m) + " ")