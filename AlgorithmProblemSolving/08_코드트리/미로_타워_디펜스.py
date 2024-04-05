"""
2:31 시작
2:35 구상 완료
3:01 1차 구현 완료
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def get_idx_arr_and_flat_lst(N, arr):
    # di = [0, 1, 0, -1]  # 백준
    # dj = [1, 0, -1, 0]
    idx_arr = [[0] * N for _ in range(N)]
    num, d = N * N - 1, 0
    ci, cj = 0, 0
    idx_arr[ci][cj] = num
    flat_lst = []
    if arr[ci][cj]: flat_lst.append(arr[ci][cj])

    while True:
        if ci == cj == N // 2:
            break
        num -= 1

        ni, nj = ci + di[d], cj + dj[d]
        if OOB(ni, nj) or idx_arr[ni][nj]:
            d = (d + 1) % 4
            ni, nj = ci + di[d], cj + dj[d]

        idx_arr[ni][nj] = num
        if arr[ni][nj]:
            flat_lst.append(arr[ni][nj])
        ci, cj = ni, nj
    return idx_arr, [0] + flat_lst[::-1]


def get_cnt_kind_lst(flat_lst):
    cnt_lst = []
    kind_lst = []

    for monster in flat_lst[1:]:
        if kind_lst and kind_lst[-1] == monster:  # 종류가 같다
            cnt_lst[-1] += 1
        else:  # 종류가 다르다
            kind_lst.append(monster)
            cnt_lst.append(1)

    return cnt_lst, kind_lst


di = [0, 1, 0, -1] # 코드트리
dj = [1, 0, -1, 0]
# di = [0, -1, 1, 0, 0] # 백준
# dj = [0, 0, 0, -1, 1]
N, rounds = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
TI, TJ = N // 2, N // 2
idx_arr, flat_lst = get_idx_arr_and_flat_lst(N, arr)
for _ in range(rounds):
    cd, cp = map(int, input().split())

    # 공격
    kill_idx_lst = []
    for p in range(1, cp + 1):
        ni, nj = TI + di[cd] * p, TJ + dj[cd] * p
        if OOB(ni, nj): break
        kill_idx_lst.append(idx_arr[ni][nj])

    for idx in kill_idx_lst[::-1]:
        if idx >= len(flat_lst): continue
        # flat_lst.pop(idx) # 백준
        ans += flat_lst.pop(idx) # 코드트리

    # 4연속 몬스터 없애기
    while True:
        cnt_lst, kind_lst = get_cnt_kind_lst(flat_lst)

        have_to_move = False
        flat_lst = [0]
        nl = len(kind_lst)
        for x in range(nl):
            if cnt_lst[x] < 4:
                flat_lst += [kind_lst[x]] * cnt_lst[x]
            else:
                ans += kind_lst[x] * cnt_lst[x]
                have_to_move = True

        if not have_to_move: break

    cnt_lst, kind_lst = get_cnt_kind_lst(flat_lst)
    flat_lst = [0]
    nl = len(kind_lst)
    for x in range(nl):
        flat_lst.append(cnt_lst[x])
        flat_lst.append(kind_lst[x])

    if len(flat_lst) > N * N:
        flat_lst = flat_lst[:N * N]
print(ans)
