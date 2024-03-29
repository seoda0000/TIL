"""
2:40 시작
3:03 구상 완료
3:35 1차 구현 완료, 휴식 시작
3:37 휴식 끝 -> 디버깅 (정사각형 리스트 누락, 회전 후 인덱스 에러)
3:49 전체 tc 확인 완료
3:55 자체 tc로 종료조건 위치 조정  (1000라운드 중 2라운드에서 종료하는 경우)
4:01 제출 -> 틀렸습니다 후 문제 정독
4:04 코드 점검 시작
4:14 정사각형 찾는 로직 새로 짜기 (완전 탐색)
4:20 완전탐색 로직 구현 완료. 기존 로직과 같은 결과가 출력되어서 다른 곳에 오류 있다는 사실 확인
4:21 문제 정독 및 방향 선정 오류 디버깅
4:23 제출

<실수한 부분>
위아래로 무조건 먼저 움직이고, 벽이 있으면 못 간다고 생각했다.
그러나 왼오로 이동할 수 있으면 그쪽으로 가도 된다. 문제를 잘 이해하지 못했다.

오류난 부분을 찾는 게 까다로웠는데, 기존 로직을 하나하나 무조건 통과할만한 완전탐색으로 바꾸어서 소거법으로 확인했던 것이 도움이 되었다.
기존 로직이 맞은 부분도 있었지만, 기존 로직이 틀리고 완전탐색 로직이 맞은 부분도 있었다.
아이디어를 완전히 믿지 말고 되도록 완탐 로직을 택하는 것이 안전할 것이다.

오류를 못 찾아서 당황할 때는 오늘처럼 부분부분의 로직을 완탐으로 바꿔보는 것도 좋은 것 같다. (시간만 있다면)
혹은 애초에 완탐 로직으로 짜는 것도 좋겠다.

애초에 문제를 잘 읽으면 될 일이다...
"""
from collections import deque


def move_ppl(arr, ei, ej):  # 출구 좌표 -> 이동 후 남은 사람 좌표 리스트 return
    global ans

    move_arr = [[0] * N for _ in range(N)]  # 이동 후 좌표
    for ci in range(N):
        for cj in range(N):
            if arr[ci][cj] <= 0: continue  # 사람 없음 -> skip

            dis_i = ei - ci  # 행 차이
            dis_j = ej - cj  # 열 차이
            d_lst = []  # 가야하는 방향 리스트

            if dis_i < 0:
                d_lst.append(0)  # 출구가 위쪽
            elif dis_i > 0:
                d_lst.append(1)  # 출구가 아래쪽

            if dis_j < 0:
                d_lst.append(2)  # 출구가 왼쪽
            elif dis_j > 0:
                d_lst.append(3)  # 출구가 오른쪽

            for d in d_lst:
                ni, nj = ci + di[d], cj + dj[d]
                if EXIT < arr[ni][nj] < 0: continue  # 벽일 경우 -> skip

                cnt = arr[ci][cj]  # 해당 칸의 사람 수
                arr[ci][cj] = 0  # 이동
                ans += cnt

                if arr[ni][nj] != EXIT:  # 출구가 아닐 때 -> 이동 표시
                    move_arr[ni][nj] += cnt
                break

    remain_ppl = []  # 남은 사람 좌표 리스트
    for i in range(N):
        for j in range(N):
            arr[i][j] += move_arr[i][j]  # 이동 표시
            if arr[i][j] > 0:  # 사람 발견
                remain_ppl.append((i, j))

    return remain_ppl


def find_square(ei, ej, ppl_lst):  # 정사각형 왼쪽 위 좌표, 정사각형 길이 return
    square_lst = []  # (가능한 정사각형 길이, 좌표 i, j)
    for pi, pj in ppl_lst:
        dis_i = abs(ei - pi)  # 행 차이
        dis_j = abs(ej - pj)  # 열 차이

        if dis_i > dis_j:  # 세로로 딱 맞다
            si = min(ei, pi)
            sj = max(max(ej, pj) - dis_i, 0)
            sn = dis_i + 1
        else:  # 가로로 딱 맞다
            sj = min(ej, pj)
            si = max(max(ei, pi) - dis_j, 0)
            sn = dis_j + 1

        square_lst.append((sn, si, sj))

    square_lst.sort()
    return square_lst[0]


EXIT = -10
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, ppl_cnt, K = map(int, input().split())
arr = []  # 0:빈칸, 음수:벽, 양수:사람 수

for _ in range(N):
    ipt = list(map(int, input().split()))
    row = [0] * N
    for j in range(N):
        if ipt[j]:
            row[j] = -ipt[j]
    arr.append(row)
for _ in range(1, ppl_cnt + 1):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] += 1

ei, ej = map(int, input().split())
ei, ej = ei - 1, ej - 1
arr[ei][ej] = EXIT

ans = 0
for k in range(K):

    # 모든 사람이 1칸 이동한다
    remain_ppl = move_ppl(arr, ei, ej)  # 이동 후 남은 사람 좌표 리스트

    if not remain_ppl: break  # 종료 조건: 모든 사람이 탈출

    # 미로가 회전한다
    sn, si, sj = find_square(ei, ej, remain_ppl)  # 가장 작은 정사각형 왼쪽 위 좌표, 정사각형 길이, 남은 사람들의 좌표
    square = []  # 대상 정사각형
    for i in range(si, si + sn):
        square.append(arr[i][sj:sj + sn])
    t_square = list(map(list, zip(*square[::-1])))  # 회전

    for i in range(sn):
        for j in range(sn):
            if t_square[i][j] == EXIT:  # 출구 -> 좌표 갱신
                ei, ej = si + i, sj + j
            elif t_square[i][j] < 0:  # 벽 -> 내구도 감소
                t_square[i][j] += 1

            arr[si + i][sj + j] = t_square[i][j]  # 기존 배열 업데이트

print(ans)
print(ei + 1, ej + 1)
