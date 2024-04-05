"""
실행시간: 232 -> 144
풀이시간: 37분 -> 31분

얻을 수 있는 점수 판을 먼저 구한 후 주사위를 굴려주었다.
주사위 문제에서는 앞으로 될 면과 이전 면만 헷갈리지 말자.
"""

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
# N, roll_cnt = map(int, input().split()) # 코드트리
# M = N
N, M, roll_cnt = map(int, input().split())  # 백준
board = [list(map(int, input().split())) for _ in range(N)]
score_arr = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if v[i][j]: continue
        get_score(i, j)

ci, cj, cd = 0, 0, 0
# up, front, right, down, back, left = 1, 2, 3, 6, 5, 4 # 코드트리
up, front, right, down, back, left = 1, 5, 3, 6, 2, 4  # 백준
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

"""
9:00 시작
9:12 구상 완료
9:25 구현 완료
9:37 코드 점검 및 제출

이전에 주사위 문제를 풀어서 손쉽게 접근했다.
다만 변화 기준을 잘못 잡아서 거꾸로 한번 뒤집었다. 변화 기준은 무조건 '변화주체=변화대상'으로 할당해야 한다

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
