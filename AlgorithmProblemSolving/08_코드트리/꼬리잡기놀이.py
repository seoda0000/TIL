"""
실행시간: 326(248) -> 286
풀이시간: 57분 -> 37분

이전에 어떤 그룹에 소속된 칸인지 확인하려고 딕셔너리를 전부 순회한 게 마음에 걸려서, group_arr을 만들어 어떤 그룹의 길인지 표기했다.
또 예전에는 for문을 4개 짰는데 이번엔 while 문으로 합쳤다. (시간은 오래 걸려도 깔끔하다)
예전엔 q를 하나만 쓰고 pop을 하지 않았다! 예전의 나 똑똑했네... 좋은 방법 같다. 단, 1방향으로 추가되는 경우에만 이래야 한다

"""

"""
11:00 시작
11:07 구상 완료
11:30 1차 구현 완료
11:37 자체 tc 디버깅 완료
"""

from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_group(si, sj, tid):
    team_arr[si][sj] = tid
    q = deque([(si, sj)])
    member_q = deque([(si, sj)])

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj): continue
            if arr[ni][nj] == 0: continue
            if team_arr[ni][nj]: continue
            if not (abs(arr[ni][nj] - arr[ci][cj]) <= 1): continue

            team_arr[ni][nj] = tid
            q.append((ni, nj))

            if arr[ni][nj] <= 3:  # 멤버 넣기
                member_q.append((ni, nj))
            break

    return member_q


di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
N, team_cnt, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
team_arr = [[0] * N for _ in range(N)]
team_dic = dict()
tid = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 1: continue
        tid += 1
        team_dic[tid] = find_group(i, j, tid)

ans = 0
for k in range(1, K + 1):

    # 이동
    for tid in range(1, team_cnt + 1):
        member_q = team_dic[tid]
        hi, hj = member_q[0]

        for d in range(4):
            ni, nj = hi + di[d], hj + dj[d]
            if OOB(ni, nj): continue
            if abs(arr[ni][nj] - arr[hi][hj]) < 2: continue

            arr[hi][hj] = 2
            arr[ni][nj] = 1
            member_q.appendleft((ni, nj))
            break

        ti, tj = member_q.pop()
        if arr[ti][tj] == 3:
            arr[ti][tj] = 4
        ti, tj = member_q[-1]
        arr[ti][tj] = 3

    # 공 던지기
    x = k % (N * 4)  # 어떤 라인을 따라 던질 건지
    dtype, num = divmod(x - 1, N)  # 방향 유형, 선의 순서

    if dtype == 0:
        ci, cj = num, 0
    elif dtype == 2:
        ci, cj = N - 1 - num, N - 1
    elif dtype == 1:
        ci, cj = N - 1, num
    else:
        ci, cj = 0, N - 1 - num

    while True:
        if OOB(ci, cj): break
        if 1 <= arr[ci][cj] <= 3:  # 사람과 맞았다
            tid = team_arr[ci][cj]  # 맞은 그룹
            member_q = team_dic[tid]
            ans += (member_q.index((ci, cj)) + 1) ** 2
            member_q.reverse()
            hi, hj = member_q[0]
            ti, tj = member_q[-1]
            arr[hi][hj], arr[ti][tj] = 1, 3
            break
        ci, cj = ci + di[dtype], cj + dj[dtype]
print(ans)

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
