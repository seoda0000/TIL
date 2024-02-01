"""
https://www.acmicpc.net/problem/14442

백준 골드3 14442 벽 부수고 이동하기

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
"""

from collections import deque


def bfs():
    v = [[INF] * M for _ in range(N)]
    v[0][0] = 0
    q = deque([(0, 0)])
    h = 0  # 지나온 칸 수

    while q:
        nq = len(q)
        h += 1

        for _ in range(nq):
            ci, cj = q.popleft()
            if ci == N - 1 and cj == M - 1:
                return h

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                # 영역 안이고, 벽을 부순 횟수를 감소하여 갱신할 수 있다면 기록
                if 0 > ni or ni >= N or 0 > nj or nj >= M: continue
                if v[ni][nj] <= v[ci][cj] + arr[ni][nj] or v[ci][cj] + arr[ni][nj] > K: continue
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
                q.append((ni, nj))

    return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
INF = N * M
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

print(bfs())
