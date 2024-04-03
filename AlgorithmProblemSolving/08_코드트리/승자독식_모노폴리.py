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
