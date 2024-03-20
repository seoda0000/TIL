"""
9:00 시작
9:12 구상 완료
9:25 구현 완료
"""
from collections import deque


def move(t, b, n, s, e, w, d):
    if d == 0:  # 동
        return w, e, n, s, t, b
    elif d == 1:  # 남
        return n, s, b, t, e, w
    elif d == 2:  # 서
        return e, w, n, s, b, t
    else:  # 북
        return s, n, t, b, e, w


def count_same_number(si, sj):
    cnt = 1
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    q = deque([(si, sj)])
    num = board[si][sj]
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if board[ni][nj] != num: continue

            v[ni][nj] = 1
            cnt += 1
            q.append((ni, nj))

    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

top, bottom, north, south, east, west = 1, 6, 2, 5, 3, 4
cd = 0
ci, cj = 0, 0
ans = 0
for _ in range(K):
    ni, nj = ci + di[cd], cj + dj[cd]

    if not (0 <= ni < N and 0 <= nj < M):
        cd = (cd + 2) % 4
        ni, nj = ci + di[cd], cj + dj[cd]

    top, bottom, north, south, east, west = move(top, bottom, north, south, east, west, cd)
    num_a = bottom
    num_b = board[ni][nj]
    num_c = count_same_number(ni, nj)
    ans += num_b * num_c

    if num_a > num_b:
        cd = (cd + 1) % 4
    elif num_a < num_b:
        cd = (cd - 1) % 4

    ci, cj = ni, nj

print(ans)
