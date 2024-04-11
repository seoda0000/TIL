'''
벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
백준 골드3 2206

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
'''


from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
q = deque([(0, 0, 0, 1)])
ans = 1000 * 1000 + 1  # 초기 최대값
v = set()  # visited 집합
while q:
    i, j, f, s = q.popleft()
    if s > ans:  # ans보다 이미 큰 경우 가지치기
        continue
    if i == N-1 and j == M-1:
        if s < ans:  # ans 업데이트
            ans = s
        continue
    for a, b in dr:
        ni, nj = i+a, j+b
        if 0 <= ni < N and 0 <= nj < M and (ni, nj, f) not in v:  # 범위 내이고 아직 방문하지 않았다면
            if arr[ni][nj] == 0:          # 이동 가능
                v.add((ni, nj, f))            # 벽 부순 여부와 함께 v에 저장
                q.append((ni, nj, f, s+1))    # enqueue
            elif f == 0:                  # 벽 부수고 이동 가능
                v.add((ni, nj, 1))            # 벽 부순 여부와 함께 v에 저장
                q.append((ni, nj, 1, s + 1))  # enqueue
if ans == 1000 * 1000 + 1:
    ans = -1
print(ans)

"""
1년 후 풀이
훨씬 빨라졌다
"""
from collections import deque


def bfs():
    q = deque([(0, 0, False)])
    h = 0  # 지나온 칸 수

    while q:
        nq = len(q)
        h += 1

        for _ in range(nq):
            ci, cj, isBroken = q.popleft()
            if ci == N - 1 and cj == M - 1:
                return h

            if not isBroken:  # 아직 벽을 안 부쉈다면
                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]
                    # 어디든 갈 수 있다. 또한 이전에 벽 부수고 도착한 곳은 1로 갱신해준다. (벽을 부수지 않는 경우가 최단거리에 더 유리하기 때문)
                    if 0 > ni or ni >= N or 0 > nj or nj >= M or v1[ni][nj] == 1: continue
                    if not arr[ni][nj]:  # 통로
                        v1[ni][nj] = 1  # 아직 벽을 부수지 않고 도착시 1 표기
                        q.append((ni, nj, False))

                    else:  # 벽 (부순다)
                        v1[ni][nj] = 2  # 벽 부수고 도착시 2 표기
                        q.append((ni, nj, True))

            else:  # 이미 벽을 부쉈다면

                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]
                    # 통로만 갈 수 있다. 또한 벽을 부수지 않고 도착할 수 있는 곳에는 굳이 가지 않는다.
                    if 0 > ni or ni >= N or 0 > nj or nj >= M or arr[ni][nj] or v1[ni][nj]: continue
                    v1[ni][nj] = 2  # 벽 부수고 도착시 2 표기
                    q.append((ni, nj, isBroken))

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v1 = [[0] * M for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

print(bfs())
