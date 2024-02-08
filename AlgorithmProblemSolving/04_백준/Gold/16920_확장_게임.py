"""
1퍼에서 시간초과
"""

from collections import deque
import sys

input = sys.stdin.readline


def game():
    while True:
        move = False
        for i in range(1, P + 1):  # 플레이어 i의 턴
            q = qs[i]

            for s in range(skills[i]):
                moveIth = False
                nq = len(q)

                for _ in range(nq):
                    ci, cj = q.popleft()

                    for d in range(4):
                        ni, nj = ci + di[d], cj + dj[d]
                        if not (0 <= ni < N and 0 <= nj < M): continue
                        if v[ni][nj]: continue
                        v[ni][nj] = 1
                        q.append((ni, nj))
                        cnt[i] += 1
                        move = True
                        moveIth = True
                if not moveIth:
                    break

        if not move:
            break
    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M, P = map(int, input().split())
skills = [0] + list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(N)]
v = [[0] * M for _ in range(N)]
qs = [deque() for _ in range(P + 1)]
cnt = [0] * (P + 1)

for i in range(N):
    for j in range(M):
        if arr[i][j] != '.':
            v[i][j] = 1
        if arr[i][j] not in '.#':
            ith = int(arr[i][j])
            qs[ith].append((i, j))
            cnt[ith] += 1

game()

print(*cnt[1:])
