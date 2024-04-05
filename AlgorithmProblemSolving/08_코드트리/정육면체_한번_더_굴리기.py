"""
1:54 시작
2:12 구상 완료
2:25 구현 완료
"""

from collections import deque


def roll(d, up, down, front, back, right, left):
    if d == 0:
        return left, right, front, back, up, down
    elif d == 1:
        return back, front, up, down, right, left
    elif d == 2:
        return right, left, front, back, down, up
    else:
        return front, back, down, up, right, left


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < M)


def get_score(si, sj):
    q = deque([(si, sj)])
    v[si][sj] = 1
    ij_lst = [(si, sj)]
    num = board[si][sj]

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj): continue
            if v[ni][nj]: continue
            if board[ni][nj] != num: continue

            ij_lst.append((ni, nj))
            q.append((ni, nj))
            v[ni][nj] = 1

    score = len(ij_lst) * num

    for i, j in ij_lst:
        score_arr[i][j] = score

    return


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, roll_cnt = map(int, input().split()) # 코드트리
M = N
# N, M, roll_cnt = map(int, input().split()) # 백준
board = [list(map(int, input().split())) for _ in range(N)]
score_arr = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if v[i][j]: continue
        get_score(i, j)

ci, cj, cd = 0, 0, 0
up, front, right, down, back, left = 1, 2, 3, 6, 5, 4 # 코드트리
# up, front, right, down, back, left = 1, 5, 3, 6, 2, 4 # 백준
ans = 0
for _ in range(roll_cnt):
    ni, nj = ci + di[cd], cj + dj[cd]
    if OOB(ni, nj):
        cd = (cd + 2) % 4
        ni, nj = ci + di[cd], cj + dj[cd]
    ans += score_arr[ni][nj]
    up, down, front, back, right, left = roll(cd, up, down, front, back, right, left)
    if down > board[ni][nj]:
        cd = (cd + 1) % 4
    elif down < board[ni][nj]:
        cd = (cd - 1) % 4
    ci, cj = ni, nj

print(ans)
