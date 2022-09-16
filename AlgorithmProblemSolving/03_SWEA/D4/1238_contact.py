'''
1238. [S/W 문제해결 기본] 10일차 - Contact D4
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.
'''


import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
for tc in range(1, 11):
    N, s = map(int, input().split())
    ipt = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    visited = [False] * 101
    for i in range(0, N, 2):
        arr[ipt[i]].append(ipt[i+1])
    q = deque([(s, 0)])
    visited[s] = True
    ans, mx = 0, 0
    while q:
        p, t = q.popleft()
        if t > mx:
            mx = t
            ans = p
        elif t == mx:
            if p >= ans:
                ans = p
        for a in arr[p]:
            if not visited[a]:
                visited[a] = True
                q.append((a, t+1))
    print(f'#{tc}', ans)