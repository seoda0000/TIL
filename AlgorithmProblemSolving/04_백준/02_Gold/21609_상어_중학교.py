"""
실행시간: 340 -> 248
풀이시간: 59분 -> 40분

이 문제 역시 이전엔 일일이 조건 비교를 해서 값을 갱신해주었다면, 이번엔 정렬을 이용하여 간단히 풀었다.
또한 중력 로직에서 파이썬의 튜플 전환을 활용하여 간단히 풀 수 있었다. 이게 좋은듯
코드트리와 백준의 세부조건이 다른 문제다.
"""

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

    bombs.sort()
    # bombs.sort(key=lambda x: (-x[0], x[1])) # 코드트리
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
    bomb_lst.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))  # 백준
    # bomb_lst.sort(key=lambda x: (-x[0], x[1], -x[2], x[3])) # 코드트리

    gcnt, _, gi, gj = bomb_lst[0]
    ans += gcnt * gcnt

    for i, j in bomb_dic[(gi, gj)]:
        arr[i][j] = BLANK

    gravity(arr)

    arr = list(map(list, zip(*arr)))[::-1]  # 반시계 회전

    gravity(arr)

print(ans)

"""
9:48 문제 시작
9:54 문제 읽기 완료
9:54 구상 시작
9:58 구상 완료
10:20 구현 완료
10:26 테케 1 디버깅 완료 (떨어질 자리에 블록이 있었던 경우 구현)
10:27 테케 2 오류 발견
10:30 코드&문제 검토 및 무지개 블록 수 고려 디버깅
10:35 테케 2 오류 확인 및 테케 검토
10:42 코드 검토
10:47 무지개 블록 갱신 누락 오류 발견 및 테케 2 디버깅 완료

무지개 블록이 제일 많은 그룹을 선택하는 로직을 빼먹어서 디버깅을 했다.
이후 바로 로직을 추가했는데, 정작 최대 무지개 그룹 수를 갱신하는 로직을 추가하지 않았다. 이로서 디버깅 시간이 길어졌다.
로직을 추가했을 때는 완벽하게 추가가 반영이 되었는지부터 확인하자. 보통 그 부분에 오류가 있다.

구현에서 테스트케이스를 모두 일일이 확인하는 것은 매우 어려운 일이다.
그것은 최후의 수단으로 미뤄두고, 코드에서 로직 체크부터 하자.
"""

from collections import deque


def find_group(si, sj):  # si, sj가 속한 그룹을 찾고, 그룹에 속한 블록 좌표 리스트, 무지개 블록의 수, 기준 블록의 좌표를 return
    group = [(si, sj)]
    gi, gj = -1, -1
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    color = arr[si][sj]
    q = deque([(si, sj)])
    r_cnt = 0

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if arr[ni][nj] == BLACK or arr[ni][nj] == AIR: continue  # 검은색과 공기 무시
            if 0 < arr[ni][nj] and arr[ni][nj] != color: continue  # 다른 색 무시
            if v[ni][nj]: continue

            v[ni][nj] = 1
            q.append((ni, nj))
            group.append((ni, nj))
            if arr[ni][nj] == RAINBOW:  # 무지개 블록 개수 세기
                r_cnt += 1

    group.sort()

    for bi, bj in group:
        if arr[bi][bj] != RAINBOW:
            gi, gj = bi, bj  # 기준 블럭 좌표
            break

    return group, r_cnt, gi, gj


def gravity(arr):
    for j in range(N):
        down_idx = N - 1
        for i in range(N)[::-1]:
            if arr[i][j] == AIR:  # 공기일 경우
                pass
            elif arr[i][j] == BLACK:  # 검은 블록
                down_idx = i - 1  # 다음 블록은 위에 쌓인다
            else:  # 일반, 무지개 블록
                if down_idx != i:  # 떨어져야 하는 경우
                    arr[down_idx][j] = arr[i][j]
                    arr[i][j] = AIR
                down_idx -= 1  # 다음 블록은 위에 쌓인다
    return


RAINBOW, BLACK, AIR = 0, -1, -2
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:

    # 1. 그룹을 고른다
    target_group = []  # 타겟 그룹에 속한 블록 리스트
    tr_cnt = -1  # 타겟 그룹의 무지개 블록 갯수
    ti, tj = -1, -1  # 타겟 그룹의 기준 블럭 좌표
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:  # 일반 블록을 만났을 때 그룹 찾기
                group, gr_cnt, gi, gj = find_group(i, j)

                if len(group) > len(target_group):  # 1) 크기가 가장 큰 그룹
                    target_group = group
                    ti, tj, tr_cnt = gi, gj, gr_cnt
                elif len(group) == len(target_group):
                    if gr_cnt > tr_cnt:  # 2) 무지개 블록이 제일 많은 그룹
                        target_group = group
                        ti, tj, tr_cnt = gi, gj, gr_cnt
                    elif gr_cnt == tr_cnt:
                        if gi > ti:  # 3) 기준 블록의 행 번호가 가장 큰 그룹
                            target_group = group
                            ti, tj, tr_cnt = gi, gj, gr_cnt
                        elif gi == ti and gj > tj:  # 4) 기준 블록의 열 번호가 가장 큰 그룹
                            target_group = group
                            ti, tj, tr_cnt = gi, gj, gr_cnt

    # 그룹이 존재하지 않으면 종료
    if len(target_group) < 2:
        break

    # 2. 점수 계산 + 고른 그룹의 블록 제거
    ans += len(target_group) ** 2
    for bi, bj in target_group:
        arr[bi][bj] = AIR  # 공백

    # 3. 중력 작용
    gravity(arr)

    # 4. 격자가 반시계 90도 회전
    arr = list(map(list, zip(*arr)))[::-1]

    # 5. 중력 작용
    gravity(arr)

print(ans)
