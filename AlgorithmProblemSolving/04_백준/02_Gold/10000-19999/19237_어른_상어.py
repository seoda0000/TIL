"""
실행시간: 248 -> 220
풀이시간: 66분 -> 55분

방향 인덱스 배열을 잘못 짜서 디버깅에 오랜 시간이 걸렸다.
기초적인 곳에서 실수를 하면 찾기 어렵다. 기초적인 곳에서는 특히 유념하자.

시간 표시하는 로직과 한 사람만 남기는 로직을 합쳤는데, 분리하는 편이 덜 헷갈리는 것 같다. 단계별로 웬만하면 분리하자.
특히 전체 순회가 아닌 것에 전체 순회 로직을 합치면 귀찮아진다.
"""

"""
5:20 시작
5:27 구상 완료
20:29 디버깅 완료
"""
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
N, player_cnt, K = map(int, input().split())
time_arr = [[0] * N for _ in range(N)]
contract_arr = [list(map(int, input().split())) for _ in range(N)]
player_lst = []  # 좌표 i, j, 방향, id
d_dic = dict()
d_lst = [0] + list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if contract_arr[i][j]:  # 플레이어 발견
            player_lst.append((i, j, d_lst[contract_arr[i][j]], contract_arr[i][j]))
            time_arr[i][j] = K
for id in range(1, player_cnt + 1):
    dic = dict()
    for d in range(1, 5):
        dic[d] = list(map(int, input().split()))
    d_dic[id] = dic

ans = -1
for turn in range(1, 1001):

    # 이동한다...
    nxt_player_lst = []

    for pi, pj, pd, pid in player_lst:
        d_lst = d_dic[pid][pd]
        blank_lst = []
        my_lst = []

        for d in d_lst:
            ni, nj = pi + di[d], pj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if contract_arr[ni][nj] == 0:
                blank_lst.append((ni, nj, d))
                break
            elif contract_arr[ni][nj] == pid:
                my_lst.append((ni, nj, d))
        if blank_lst:
            xi, xj, xd = blank_lst[0]
        else:
            xi, xj, xd = my_lst[0]

        nxt_player_lst.append((xi, xj, xd, pid))

    player_lst = nxt_player_lst

    # 계약 기간이 감소한다...
    for i in range(N):
        for j in range(N):
            if time_arr[i][j]:
                time_arr[i][j] -= 1
                if time_arr[i][j]: continue
                contract_arr[i][j] = 0

    # 한놈만 남긴다...
    player_lst.sort(key=lambda x: (x[0], x[1], x[-1]))
    np = len(player_lst)
    for x in range(1, np)[::-1]:
        pi, pj, pd, pid = player_lst[x]
        bi, bj, bd, bid = player_lst[x - 1]
        if pi == bi and pj == bj:
            player_lst.pop(x)
        else:
            contract_arr[pi][pj] = pid
            time_arr[pi][pj] = K

    pi, pj, pd, pid = player_lst[0]
    contract_arr[pi][pj] = pid
    time_arr[pi][pj] = K

    if len(player_lst) == 1:
        ans = turn
        break

print(ans)

"""
2:41 문제 읽기 시작
2:55 구상 중 휴식
2:59 휴식 끝
3:30 구현 끝
3:44 디버깅 완료 (정렬 실수 / 자기 냄새칸 찾았을 때 break 하면 안됨)
3:47 마지막 코드 검토 완료

초기 설계와 구현의 차이점을 고려하지 못하고 오류가 있었다. 설계와 구현이 달라졌을 때는 그 부분을 유의해서 확인해보자
문제와 똑같은 모양의 배열이 나오도록 풀자. 그 편이 확인하기 쉽다.
"""
from collections import defaultdict
import sys

input = sys.stdin.readline

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
N, shark_cnt, K = map(int, input().split())
sharks = []  # (상어 위치 si, sj, 상어 방향 sd, 상어 id)
arr = [list(map(int, input().split())) for _ in range(N)]  # 초기 바다 정보
sharks_dir = [0] + list(map(int, input().split()))  # 초기 상어 방향

preference_dic = defaultdict(dict)  # 상어 우선순위 저장 id: {방향: [우선순위]}
for id in range(1, shark_cnt + 1):
    for x in range(1, 5):
        preference_dic[id][x] = list(map(int, input().split()))

smell_arr = [[0] * N for _ in range(N)]  # i, j에 냄새 뿌린 상어의 id
time_arr = [[0] * N for _ in range(N)]  # i, j의 냄새 없어지는데 앞으로 걸리는 시간

for i in range(N):
    for j in range(N):
        if arr[i][j]:  # 상어 정보 저장 + 초기 냄새 뿌리기
            id = arr[i][j]
            sharks.append((i, j, sharks_dir[id], id))
            smell_arr[i][j] = id
            time_arr[i][j] = K

ans = -1
for t in range(1, 1001):
    # 상어 이동
    nxt_sharks = []
    for si, sj, sd, id in sharks:
        prefer = preference_dic[id][sd]  # 우선 순위

        # 자기 냄새
        my_smell_lst = []
        # 아예 빈 공간
        blank_lst = []

        for pd in prefer:
            ni, nj = si + di[pd], sj + dj[pd]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if smell_arr[ni][nj] == 0:
                blank_lst.append((ni, nj, pd))
                break
            elif smell_arr[ni][nj] == id:
                my_smell_lst.append((ni, nj, pd))

        if blank_lst:  # 빈 공간 존재
            ni, nj, nd = blank_lst[0]
        else:  # 자기 냄새
            ni, nj, nd = my_smell_lst[0]

        nxt_sharks.append((ni, nj, nd, id))

    # 한 칸에 한마리만 남기기
    sharks = nxt_sharks
    sharks.sort(key=lambda x: (x[0], x[1], x[3]))  # 좌표, id 순서
    ns = len(sharks)
    for x in range(1, ns)[::-1]:
        cur = sharks[x]
        bef = sharks[x - 1]  # 앞이랑 비교해서 같은 위치면 제거

        if cur[0] == bef[0] and cur[1] == bef[1]:  # 같은 위치
            sharks.pop(x)

    if len(sharks) == 1:  # 상어가 한마리만 남았다
        ans = t
        break

    # 냄새가 옅어진다
    for i in range(N):
        for j in range(N):
            if time_arr[i][j]:
                time_arr[i][j] -= 1

                if time_arr[i][j] == 0:  # K초가 지나서 냄새가 없어진다
                    smell_arr[i][j] = 0

    # 냄새를 뿌린다
    for si, sj, sd, id in sharks:
        time_arr[si][sj] = K
        smell_arr[si][sj] = id

print(ans)
