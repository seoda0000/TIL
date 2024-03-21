"""
https://www.acmicpc.net/problem/16933

백준 골드1 16933 벽 부수고 이동하기 3

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다. 이동하지 않고 같은 칸에 머물러있는 경우도 가능하다. 이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다.

이번 문제에서는 낮과 밤이 번갈아가면서 등장한다. 가장 처음에 이동할 때는 낮이고, 한 번 이동할 때마다 낮과 밤이 바뀌게 된다. 이동하지 않고 같은 칸에 머무르는 경우에도 낮과 밤이 바뀌게 된다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다. 단, 벽은 낮에만 부술 수 있다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
"""

from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    v1 = [[INF] * M for _ in range(N)]  # 낮
    v1[0][0] = 0
    v2 = [[INF] * M for _ in range(N)]  # 밤
    v2[0][0] = 0
    q = deque([(0, 0)])
    h = 0  # 지나온 칸 수

    while q:
        nq = len(q)
        h += 1

        letsWait = False
        for _ in range(nq):
            ci, cj = q.popleft()
            if ci == N - 1 and cj == M - 1:
                return h

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if 0 > ni or ni >= N or 0 > nj or nj >= M: continue  # 범위 밖이면 continue

                if h % 2:  # 홀수: 현재 낮
                    # 벽을 부순 횟수를 감소하여 갱신할 수 있다면 기록
                    if v2[ni][nj] <= v1[ci][cj] + arr[ni][nj] or v1[ci][cj] + arr[ni][nj] > K: continue
                    v2[ni][nj] = v1[ci][cj] + arr[ni][nj]
                    q.append((ni, nj))

                else:  # 짝수: 현재 밤

                    if arr[ni][nj]:  # 다음 목적지에 벽이 있을 경우
                        letsWait = True  # 기다린다

                    else:  # 다음 목적지가 통로일 경우
                        if v1[ni][nj] > v2[ci][cj]:  # 벽을 부순 횟수를 감소하여 갱신할 수 있다면 기록
                            v1[ni][nj] = v2[ci][cj]
                            q.append((ni, nj))

            if letsWait:
                q.append((ci, cj))  # 기다려야 하는 경우 현 위치 push
                v1[ci][cj] = min(v1[ci][cj], v2[ci][cj])

    return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
INF = N * M * 2
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

print(bfs())
