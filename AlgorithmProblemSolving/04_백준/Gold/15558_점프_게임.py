"""
https://www.acmicpc.net/problem/15558
백준 골드5 15558 점프 게임
"""

from collections import deque


def jump():
    si, sj = 0, 1
    t = 0
    q = deque([(si, sj)])
    v[si][sj] = 1

    while q:
        t += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            for di, dj in [(0, 1), (0, -1), (1, K)]:
                ni, nj = (ci + di) % 2, cj + dj
                if nj > N:  # 목적 달성
                    return 1
                if nj <= t:  # 이동 불가 : 무너진 곳
                    continue
                if arr[ni][nj] == 0:  # 이동 불가 : 위험한 곳
                    continue
                if v[ni][nj]:  # 이미 방문한 곳
                    continue
                v[ni][nj] = 1
                q.append((ni, nj))
    return 0


N, K = map(int, input().split())
arr = [[0] + list(map(int, input())) for _ in range(2)]
v = [[0] * (N + 1) for _ in range(2)]
print(jump())
