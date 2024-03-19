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
