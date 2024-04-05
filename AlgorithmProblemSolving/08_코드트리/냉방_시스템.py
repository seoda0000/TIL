"""
2:39 시작
2:47 구상 완료
3:13 구현 완료
3:20 디버깅 완료 (wind_arr 갱신 오류)
3:26 디버깅 완료 (d->ad 오타)
"""

from collections import defaultdict, deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < M)


def check_wall(i, j, d):
    if d == 0:
        return wall_dic[(i, j)][1]
    elif d == 2:
        return wall_dic[(i, j)][0]
    elif d == 4:
        return wall_dic[(i, j + 1)][1]
    else:
        return wall_dic[(i + 1, j)][0]


def wind(wind_arr, ai, aj, ad):
    v = [[0] * M for _ in range(N)]
    si, sj = ai + di[ad], aj + dj[ad]
    wind_arr[si][sj] += 5
    v[si][sj] = 5
    q = deque([(si, sj)])
    for k in range(1, 5)[::-1]:
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()

            for x in [-1, 0, 1]:
                d = (ad + x) % 8
                ni, nj = ci + di[d], cj + dj[d]  # 다음 칸
                if OOB(ni, nj): continue
                if v[ni][nj]: continue
                if check_wall(ni, nj, (ad + 4) % 8): continue  # 다음 칸의 벽 확인
                if check_wall(ci, cj, (d + x) % 8): continue  # 이번 칸의 벽 확인

                v[ni][nj] = k
                wind_arr[ni][nj] += k
                q.append((ni, nj))

    return


di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
N, wall_cnt, K = map(int, input().split()) # 코드트리
M=N
# N, M, K = map(int, input().split())  # 백준
room_lst = []
ac_lst = []
# baekjun_dic = {2: 0, 3: 2, 1: 4, 4: 6}  # 백준
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(M):
        if ipt[j] == 1: # 코드트리
        # if ipt[j] == 5:  # 백준
            room_lst.append((i, j))
        elif ipt[j] >= 2: # 코드트리
        # elif ipt[j] >= 1:  # 백준
            ac_lst.append((i, j, (ipt[j] - 2) * 2)) # 코드트리
            # ac_lst.append((i, j, baekjun_dic[ipt[j]]))  # 백준
# wall_cnt = int(input())  # 백준
arr = [[0] * M for _ in range(N)]
wall_dic = defaultdict(lambda: [0, 0])
for _ in range(wall_cnt):
    i, j, s = map(int, input().split())
    wall_dic[(i - 1, j - 1)][s] = 1 # 코드트리
    # if s:  # 백준
    #     wall_dic[(i - 1, j)][s] = 1
    # else:
    #     wall_dic[(i - 1, j - 1)][s] = 1

ans = -1  # 코드트리
# ans = 101  # 백준
for t in range(1, 101):

    # 바람이 분다
    wind_arr = [[0] * M for _ in range(N)]
    for ai, aj, ad in ac_lst:
        wind(wind_arr, ai, aj, ad)

    for i in range(N):
        for j in range(M):
            arr[i][j] += wind_arr[i][j]

    # 공기가 섞인다
    wind_arr = [[0] * M for _ in range(N)]
    for i in range(N)[::-1]:
        for j in range(M)[::-1]:
            nxt_lst = [(i - 1, j), (i, j - 1)]
            for d in range(2):
                ni, nj = nxt_lst[d]
                if OOB(ni, nj) or wall_dic[(i, j)][d]: continue
                h = abs(arr[i][j] - arr[ni][nj]) // 4
                if arr[i][j] > arr[ni][nj]:
                    wind_arr[i][j] -= h
                    wind_arr[ni][nj] += h
                else:
                    wind_arr[i][j] += h
                    wind_arr[ni][nj] -= h

    for i in range(N):
        for j in range(M):
            arr[i][j] += wind_arr[i][j]

    # 가장자리 시원함 1 감소
    for i in range(N):
        if arr[i][0]:
            arr[i][0] -= 1
        if arr[i][M - 1]:
            arr[i][M - 1] -= 1

    for j in range(1, M - 1):
        if arr[0][j]:
            arr[0][j] -= 1
        if arr[N - 1][j]:
            arr[N - 1][j] -= 1

    # 사무실 점검
    is_end = True
    for ri, rj in room_lst:
        if arr[ri][rj] < K:
            is_end = False
            break
    if is_end:
        ans = t
        break

print(ans)
