"""
실행시간: 396 -> 444
풀이시간: 53분 -> 32분

이전에 재귀로 구현한 것을 while문으로 구현했다. 재귀는 꼭 필요할 때만 쓰도록 하자.
더 오래 걸리지만 명확한 코드인 것 같다

"""

"""
4:02 시작
4:08 구상 완료
4:18~4:26 휴식
4:34 코드 점검 및 제출
"""
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if arr[i][0] == -1:
        wi_tup = (i, i + 1)
        arr[i][0] = 0
        arr[i + 1][0] = 0
        break

for _ in range(T):
    # 먼지 확산
    nxt_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            nxt_lst = []
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if not (0 <= ni < N and 0 <= nj < M): continue
                if ni in wi_tup and nj == 0: continue
                nxt_lst.append((ni, nj))
            nxt_dust = arr[i][j] // 5

            for ni, nj in nxt_lst:
                nxt_arr[ni][nj] += nxt_dust
            nxt_arr[i][j] -= nxt_dust * len(nxt_lst)

    for i in range(N):
        for j in range(M):
            arr[i][j] += nxt_arr[i][j]

    # 위쪽 돌풍
    ci, cj = wi_tup[0] - 1, 0
    d = 2

    while True:
        if ci == wi_tup[0] and cj == 0: break  # 돌풍 자리

        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni <= wi_tup[0] and 0 <= nj < M):
            d = (d + 1) % 4
            ni, nj = ci + di[d], cj + dj[d]
        arr[ci][cj] = arr[ni][nj]
        ci, cj = ni, nj

    # 아래쪽 돌풍
    ci, cj = wi_tup[1] + 1, 0
    d = 0

    while True:
        if ci == wi_tup[1] and cj == 0: break  # 돌풍 자리

        ni, nj = ci + di[d], cj + dj[d]
        if not (wi_tup[1] <= ni < N and 0 <= nj < M):
            d = (d - 1) % 4
            ni, nj = ci + di[d], cj + dj[d]
        arr[ci][cj] = arr[ni][nj]
        ci, cj = ni, nj

print(sum([sum(a) for a in arr]))

"""
15:00~15:50 구상 + 구현
15:53 제출

미세먼지 이동을 구현하기 어려워서 반대 방향으로 흡수한다고 생각했다.
두 공기청정기가 함수를 공유할 수 있도록 만들었다. 이때 변수 설정을 세심하게 하지 못해서 디버깅 하면서 잡았다.
함수를 다양한 곳에서 활용할 때는 함수 내 변수에 유의하자...
"""

import sys

input = sys.stdin.readline


def clean_air(ci, cj, d):  # 현재 위치, 방향 번호

    ni, nj = ci + di[d], cj + dj[d]

    if not (si <= ni <= ei and 0 <= nj < M):  # 범위 밖 -> 다음 방향으로
        d = (d + 1) % 4
        ni, nj = ci + di[d], cj + dj[d]

    if arr[ni][nj] == -1:  # 다음 위치 공기청정기 -> 종료
        arr[ci][cj] = 0
        return

    dust = arr[ni][nj]  # 현재 위치로 움직일 먼지
    arr[ci][cj] = dust

    clean_air(ni, nj, d)

    return


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
di_up = [-1, 0, 1, 0]
di_down = [1, 0, -1, 0]

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
air_i_lst = []
for i in range(N):
    if -1 in arr[i]:
        air_i_lst.append(i)
ai, aj = air_i_lst[0], 0  # 위쪽 공기청정기 위치
bi, bj = air_i_lst[1], 0  # 아래쪽 공기청정기 위치

for _ in range(T):

    # [1] 확산
    plus_arr = [[0] * M for _ in range(N)]  # i, j를 향해 확산된 미세먼지

    for ci in range(N):
        for cj in range(M):
            dust = arr[ci][cj]  # 현재 미세먼지

            if dust < 0: continue  # 공기청정기 자리 -> skip

            cnt = 0  # 확산 방향 수

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if not (0 <= ni < N and 0 <= nj < M): continue  # 범위 밖 -> skip
                if arr[ni][nj] < 0: continue  # 공기청정기 -> skip
                cnt += 1
                plus_arr[ni][nj] += dust // 5

            arr[ci][cj] -= cnt * (dust // 5)

    for i in range(N):
        for j in range(M):
            arr[i][j] += plus_arr[i][j]

    # [2] 공기청정기 가동
    di = di_up  # 위쪽 흡수 방향
    si, ei = 0, ai  # 위쪽 세로 범위
    clean_air(ai - 1, aj, 0)  # 위쪽 가동

    di = di_down  # 아래쪽 흡수 방향
    si, ei = bi, N - 1  # 아래쪽 세로 범위
    clean_air(bi + 1, bj, 0)  # 아래쪽 가동

# 답: 공기청정기(-2)만큼 더해주기
ans = sum([sum(a) for a in arr]) + 2
print(ans)
