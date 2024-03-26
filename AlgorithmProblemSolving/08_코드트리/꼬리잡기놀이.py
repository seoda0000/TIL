"""
9:00 시작
9:09 구상 완료
9:33 1차 구현 완료
9:36 tc 확인 완료
9:42 자체tc 확인 완료 -> 틀렸습니다
9:57 사람이 꽉 차 있는 엣지 케이스 적용 후 제출

사람이 꽉 차 있는 경우를 충분히 생각할 수 있었는데!! 성실하게 엣지 케이스를 떠올려보자
처음엔 모든 팀원을 2로 통일할까 했는데, 문제를 있는 그대로 구현하기로 했다. 이후에 엣지케이스에서 1, 2, 3 정보가 필요하다는 걸 깨달았다.
어떤 엣지가 있을지 모르니 문제를 일단 그대로 구현하는 습관을 유지하자
"""

from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_team(si, sj):
    q = deque([(si, sj)])  # 머리에서 시작

    ci, cj = si, sj

    while True:
        stop = True
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if OOB(ni, nj): continue
            if (ni, nj) in q: continue
            if arr[ni][nj] in {0, 4}: continue
            if abs(arr[ni][nj] - arr[ci][cj]) <= 1:  # 1 이하로 차이나는 칸이 다음 칸이다
                q.append((ni, nj))
                ci, cj = ni, nj
                stop = False

        if stop:
            break

    return q


def move_team(idx, arr):  # idx번째 팀을 이동
    hi, hj = teams[idx][0]

    for d in range(4):  # 4를 우선하여 머리 고르기
        ni, nj = hi + di[d], hj + dj[d]
        if OOB(ni, nj): continue

        if arr[ni][nj] == 4:  # 빈칸이 있는 경우: 확정
            nhi, nhj = ni, nj
            break
        elif arr[ni][nj] == 3:  # 사람이 꽉 차 있는 경우
            nhi, nhj = ni, nj

    # 기존 머리, 꼬리 지우기
    ti, tj = teams[idx].pop()
    arr[hi][hj] = 2
    arr[ti][tj] = 4

    # 새로운 머리, 꼬리 표시
    teams[idx].appendleft((nhi, nhj))
    nti, ntj = teams[idx][-1]
    arr[nhi][nhj] = 1
    arr[nti][ntj] = 3

    return


def check_score(i, j):  # i, j의 사람이 받았을 때 점수 체크
    global ans

    for t in range(team_cnt):
        if (i, j) in teams[t]:
            ans += (1 + teams[t].index((i, j))) ** 2
            teams[t].reverse()  # 방향 전환
            hi, hj = teams[t][0]  # 머리 꼬리 교체
            ti, tj = teams[t][-1]
            arr[hi][hj] = 1
            arr[ti][tj] = 3
    return


di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

N, team_cnt, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

teams = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            teams.append(find_team(i, j))

for k in range(K):
    # 팀이 이동한다
    for t in range(team_cnt):
        move_team(t, arr)

    # 공이 던져진다
    num = k % (4 * N)  # 공의 종류 (총 4N개)
    d, nth = divmod(num, N)  # 방향, 순번

    if d == 0:
        for j in range(N):
            if arr[nth][j] in {1, 2, 3}:
                check_score(nth, j)
                break
    elif d == 1:
        for i in range(N)[::-1]:
            if arr[i][nth] in {1, 2, 3}:
                check_score(i, nth)
                break
    elif d == 2:
        for j in range(N)[::-1]:
            if arr[N - 1 - nth][j] in {1, 2, 3}:
                check_score(N - 1 - nth, j)
                break
    else:
        for i in range(N):
            if arr[i][N - 1 - nth] in {1, 2, 3}:
                check_score(i, N - 1 - nth)
                break

print(ans)
