"""
3:45 시작
3:55 구상 완료
4:29 1차 구현 완료

43퍼 틀렸습니다
"""
import sys

input = sys.stdin.readline


def make_num_arr_and_marbles(start):  # 숫자판 만들기 + 구슬 배열 만들기

    num_arr = [[0] * N for _ in range(N)]
    num = N * N - 1  # 가장 큰 숫자
    ci = cj = d = 0
    num_arr[ci][cj] = num
    marbles = [start[ci][cj]]  # 구슬 배열
    num -= 1
    while num:
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < N) or num_arr[ni][nj]:
            d = (d + 1) % 4
            continue

        num_arr[ni][nj] = num
        marbles.append(start[ni][nj])
        num -= 1
        ci, cj = ni, nj

    marbles.append(MAGICIAN)

    return num_arr, marbles[::-1]


MAGICIAN = -1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
start = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
md_dic = {4: 0, 2: 1, 3: 2, 1: 3}
ans_lst = [0] * 4
num_arr, marbles = make_num_arr_and_marbles(start)
mi = mj = N // 2
for d, ms in magics:
    md = md_dic[d]  # 방향 설정

    # 블리자드 마법
    crush_nums = []
    ci, cj = mi, mj
    for _ in range(ms):
        ci, cj = ci + di[md], cj + dj[md]
        if not (0 <= ci < N and 0 <= cj < N): break
        crush_nums.append(num_arr[ci][cj])

    # 구슬 깨진다
    for num in crush_nums:
        if num < len(marbles):
            marbles[num] = 0
        else:
            break

    # 구슬 이동
    color_stk = []  # 구슬 색깔 리스트
    cnt_stk = []  # 연속된 색깔의 수
    nm = len(marbles)
    for m in range(1, nm):
        marble = marbles[m]
        if marble:  # 구슬이 있으면
            if color_stk and color_stk[-1] != marble:  # 다른 색 구슬 넣을 때
                color_stk.append(marble)
                cnt_stk.append(1)

            elif color_stk and color_stk[-1] == marble:  # 같은 색 구슬 넣을 때
                cnt_stk[-1] += 1

            else:  # 첫번째 구슬 넣을 때
                color_stk.append(marble)
                cnt_stk.append(1)

    while True:
        ns = len(color_stk)
        is_move = False
        for x in range(ns)[::-1]:
            if cnt_stk[x] >= 4:
                ans_lst[color_stk.pop(x)] += cnt_stk.pop(x)
                is_move = True

        if not color_stk: break

        new_color_stk = [color_stk[0]]  # 구슬 색깔 리스트
        new_cnt_stk = [cnt_stk[0]]  # 연속된 색깔의 수

        ns = len(color_stk)
        for x in range(1, ns):
            if new_color_stk and new_color_stk[-1] == color_stk[x]:  # 전이랑 같으면
                new_cnt_stk[-1] += cnt_stk[x]
                is_move = True
            else:  # 다르면
                new_color_stk.append(color_stk[x])
                new_cnt_stk.append(cnt_stk[x])

        color_stk = new_color_stk
        cnt_stk = new_cnt_stk

        if is_move is False: break

    # 구슬 변화
    marbles = [MAGICIAN]

    if color_stk:
        ns = len(color_stk)
        for m in range(ns):
            marbles.append(cnt_stk[m])
            marbles.append(color_stk[m])

    if len(marbles) > N * N:  # 범위 밖 자르기
        marbles = marbles[:N * N]

print(ans_lst[1] + ans_lst[2] * 2 + ans_lst[3] * 3)
