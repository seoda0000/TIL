'''
바이러스
https://www.acmicpc.net/problem/2606
백준 실버3 2606

신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''
from collections import deque


C = int(input())
lst = [[] for _ in range(C+1)]
N = int(input())
visited = [0] * (C+1)

for _ in range(N):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

q = deque([1])
while q:
    n = q.popleft()
    visited[n] = True
    for a in lst[n]:
        if not visited[a]:
            q.append(a)
ans = sum(visited)-1
print(ans)