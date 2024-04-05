"""
1:03 시작
1:09 구현 완료
1:43 red_bombs 디버깅 완료
"""

from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_group(si, sj):
    q = deque([(si, sj)])
    v[si][sj] = 1
    num = arr[si][sj]
    bombs = [(si, sj)]
    red_bombs = []

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj) or v[ni][nj]: continue
            if arr[ni][nj] == 0 and (ni, nj) not in red_bombs:  # 빨폭
                q.append((ni, nj))
                red_bombs.append((ni, nj))
            elif arr[ni][nj] == num:  # 같은 색 폭탄
                q.append((ni, nj))
                bombs.append((ni, nj))
                v[ni][nj] = 1

    # bombs.sort() # 백준
    bombs.sort(key=lambda x: (-x[0], x[1])) # 코드트리
    gi, gj = bombs[0]
    bomb_dic[(gi, gj)] = bombs + red_bombs
    return len(bombs) + len(red_bombs), len(red_bombs), gi, gj


def gravity(arr):
    for j in range(N):
        floor = N - 1
        for i in range(N)[::-1]:
            if arr[i][j] == -1:  # 검은 돌
                floor = i - 1
            elif 0 <= arr[i][j]:  # 폭탄
                arr[floor][j], arr[i][j] = arr[i][j], arr[floor][j]
                floor -= 1
    return


BLANK = -2
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    # 폭탄 묶음 찾기
    v = [[0] * N for _ in range(N)]
    bomb_dic = dict()  # 기준점 좌표 : 폭탐 좌표 목록
    bomb_lst = []  # 크기, 빨간 폭탄 수, 행, 열
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue  # 검은 돌이나 빨간 폭탄
            if v[i][j]: continue
            gcnt, rcnt, gi, gj = find_group(i, j)
            if gcnt < 2: continue
            bomb_lst.append((gcnt, rcnt, gi, gj))
    if not bomb_lst: break
    # bomb_lst.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))  # 백준
    bomb_lst.sort(key=lambda x: (-x[0], x[1], -x[2], x[3])) # 코드트리

    gcnt, _, gi, gj = bomb_lst[0]
    ans += gcnt * gcnt

    for i, j in bomb_dic[(gi, gj)]:
        arr[i][j] = BLANK

    gravity(arr)

    arr = list(map(list, zip(*arr)))[::-1]  # 반시계 회전

    gravity(arr)

print(ans)
