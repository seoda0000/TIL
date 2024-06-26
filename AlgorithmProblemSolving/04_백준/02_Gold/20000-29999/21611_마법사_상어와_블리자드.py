"""
실행시간: 180(168) -> 176
풀이시간: 143분 -> 37분

문제를 읽지 않아서 고생한 문제라서, 문제를 읽어서 고생하지 않았다.
cnt, kind lst 를 만드는 함수만 구현해서 메인 로직에서 여기저기 썼다.

동일 로직인데 살짝 다른 경우, return 자료형을 통일해서 같은 함수로 처리하면 쉽다.
이번에도 (cnt, kind lst -> cnt, kind lst) 로직과 (cnt, kind lst -> flat lst)로 변하는 로직이 있었는데,
전자를 후자로 통일해서 깔끔하게 풀 수 있었다.
"""

"""
2:31 시작
2:35 구상 완료
3:01 1차 구현 완료
3:08 제출
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def get_idx_arr_and_flat_lst(N, arr):
    di = [0, 1, 0, -1]  # 백준
    dj = [1, 0, -1, 0]  # 백준
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


# di = [0, 1, 0, -1] # 코드트리
# dj = [1, 0, -1, 0]
di = [0, -1, 1, 0, 0]  # 백준
dj = [0, 0, 0, -1, 1]
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
        flat_lst.pop(idx)  # 백준
        # ans += flat_lst.pop(idx) # 코드트리

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

"""
0:00 시작
0:10 구상 완료
0:44 1차 구현 완료
0:45 tc1 오류 확인 및 디버깅 시작 - 0번 구슬 skip 로직 추가, 폭파 로직 조건 분기)
1:05 자체 테스트 케이스로 디버깅 시작 - 마지막 폭파 처리
1:13 전체 tc 확인 및 제출, 휴식 시작
1:16 휴식 끝, 코드 점검 및 최적화
1:36 문제 다시 읽기 -> 범위 제한 확인 및 디버깅
1:38 43퍼 틀렸습니다 후 변수명, 매직넘버 수정
1:44 문제 다시 읽으면서 예외 사항 점검
2:00 문제 다시 정독
2:10 폭파 로직 전면 수정 시작
2:18 구현 완료 및 63퍼 인덱스 에러 확인 후 코드 점검
2:22 에러 코드 확인 및 디버깅
2:23 자체 테스트케이스 점검 및 제출



<실수한 부분>
개인적으로 스택을 좋아해서 구상 중 스택이다!라는 생각이 들자마자 구현에 들어갔고 이것이 패착이었다...
배열과 스택 구현까지는 쉽게 했으나 마지막에 범위를 벗어난 구슬들을 없애지 않아서 시간초과가 났다.
이를 스택의 효율성 문제로 착각했고 기나긴 뻘짓이 시작되었다...
이후 문제를 읽고 범위 제한을 구현하였으나, 그 윗 문단을 제대로 읽지 않아서 또 에러가 났다.
폭파 -> 이동 -> 폭파 -> 이동 순서대로 처리해야 했는데,
스택을 잘 쓴 최적화를 한답시고 폭발과 이동을 동시에 처리한 것이다.
만용을 부리지 않고 무조건 문제를 잘 읽고 시키는대로 구현해야 한다.

<잘한 부분>
쎄한 부분을 자체 테스트 케이스를 만들어서 잡았다

<교훈>
좋아하는 알고리즘이나 풀었던 문제다 싶으면 경솔해지는 경향이 있는데 언제나 신중하고 겸손한 태도로 문제를 대해야 한다.
문제에서 시키는대로 하자. 문제가 반영되지 않으면 그냥 아무 의미 없는 코드다!
시간초과는 성능보다는 독해력의 문제다.
"""
import sys

input = sys.stdin.readline


def make_num_arr_and_marbles(start):  # 숫자판 만들기 + 구슬 배열 만들기

    num_arr = [[0] * N for _ in range(N)]
    num = N * N - 1  # 가장 큰 숫자부터 표기
    ci = cj = d = 0
    num_arr[ci][cj] = num
    marbles = [start[ci][cj]]  # 구슬 배열
    num -= 1
    while num:  # 달팽이로 채우기
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
di = [0, 1, 0, -1]  # 달팽이 방향
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
start = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
md_dic = {4: 0, 2: 1, 3: 2, 1: 3}  # 마법 방향을 달팽이 방향으로
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
    cnt_stk = []  # 연속된 색깔의 수 리스트
    for m in range(1, len(marbles)):
        marble = marbles[m]
        if marble:  # 구슬이 있으면
            if color_stk and color_stk[-1] == marble:  # 직전 구슬과 같은 색이다
                cnt_stk[-1] += 1

            else:  # 직전 구슬과 다른 색이다
                color_stk.append(marble)
                cnt_stk.append(1)

    while True:
        is_moved = False  # 구슬의 위치에 변화가 있는지

        # 폭파
        for x in range(len(color_stk))[::-1]:
            if cnt_stk[x] >= 4:
                ans_lst[color_stk.pop(x)] += cnt_stk.pop(x)
                is_moved = True

        if not is_moved or not color_stk: break  # 남은 구슬이 없거나, 이동할 필요 없을 때 종료

        # 이동
        new_color_stk = [color_stk[0]]  # 구슬 색깔 리스트
        new_cnt_stk = [cnt_stk[0]]  # 연속된 색깔의 수 리스트

        for x in range(1, len(color_stk)):
            if new_color_stk and new_color_stk[-1] == color_stk[x]:  # 직전 구슬과 같은 색이다
                new_cnt_stk[-1] += cnt_stk[x]

            else:  # 직전 구슬과 다른 색이다
                new_color_stk.append(color_stk[x])
                new_cnt_stk.append(cnt_stk[x])

        color_stk = new_color_stk
        cnt_stk = new_cnt_stk

        if is_moved is False: break

    # 구슬 변화
    marbles = [MAGICIAN]

    if color_stk:
        for m in range(min(len(color_stk), (N * N) // 2)):  # N*N까지만 채우기
            marbles.append(cnt_stk[m])
            marbles.append(color_stk[m])

print(ans_lst[1] + ans_lst[2] * 2 + ans_lst[3] * 3)
