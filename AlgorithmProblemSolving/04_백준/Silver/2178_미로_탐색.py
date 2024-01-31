'''
미로 탐색
https://www.acmicpc.net/problem/2178
백준 실버1 2178

N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

'''
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
q = deque([(0, 0, 1)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = 1
ans = N * M
while q:
    pi, pj, s = q.popleft()
    if pi == N - 1 and pj == M - 1:
        if s < ans:
            ans = s
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= pi + a < N and 0 <= pj + b < M and arr[pi + a][pj + b] and not visited[pi + a][pj + b]:
            visited[pi + a][pj + b] = True
            q.append((pi + a, pj + b, s + 1))
print(ans)

"""
칸 수 단위로 나눈 풀이
"""

N, M = map(int, input().split())
N, M = N + 2, M + 2
arr = ['0' * M] + ['0' + input() + '0' for _ in range(N - 2)] + ['0' * M]
v = [[0] * M for _ in range(N)]
v[1][1] = 1
t = 0
flag = False
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
q = [(1, 1)]
ans = -1
while q:
    n = len(q)
    t += 1
    for _ in range(n):
        ci, cj = q.pop(0)
        if ci == N - 2 and cj == M - 2:
            ans = t
            flag = True
            break
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if arr[ni][nj] == '1' and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))

    if flag:
        break
print(ans)
