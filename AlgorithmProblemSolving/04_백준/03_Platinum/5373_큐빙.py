"""
풀이시간: 62분 -> 26분 (문제가 달라서 큰 의미 없음)

이전엔 열 단위로 접근했지만, 이번에는 아예 input부터 인덱스가 부여되어서 그냥 인덱스로 접근했다.
돌리면 대상 인덱스가 2칸씩 밀리거나 땡겨진다는 점을 이용했다.
뒷면 인덱스 파악하는데 헷갈려서 미칠뻔 했다...! input이 이렇게 주어지지 않는다면 인덱스가 아닌 기존 방식대로 풀 것 같다
각 인덱스마다 총 2번 등장한다는 점을 통해 디버깅하면 좋을 것 같다
"""

"""
백준 16939 2x2x2 큐브
10:05 시작 10:13 구상 완료
10:31 1차 구현 완료
"""


def turn(cube, idx_lst):  # 해당 면을 시계방향, 반시계방향으로 각각 돌린 후 완료 여부 return
    # 시계
    turned_cube = cube[:]
    for i in range(8):
        turned_cube[idx_lst[i]] = cube[idx_lst[(i + 2) % 8]]
    if check(turned_cube):
        return True

    # 반시계
    turned_cube = cube[:]
    for i in range(8):
        turned_cube[idx_lst[i]] = cube[idx_lst[(i - 2) % 8]]
    if check(turned_cube):
        return True

    return False


def check(cube):  # 큐브 완료 여부 return
    for i in range(1, 25, 4):
        if len(set(cube[i:i + 4])) > 1:
            return False
    return True


cube = [0] + list(map(int, input().split()))

# 앞면을 돌릴 때 영향 받는 면
front = [3, 4, 17, 19, 10, 9, 16, 14]
# 뒤
back = [18, 20, 12, 11, 15, 13, 1, 2]
# 오
right = [6, 8, 10, 12, 23, 21, 2, 4]
# 왼
left = [5, 7, 9, 11, 24, 22, 1, 3]
# 위
up = [13, 14, 5, 6, 17, 18, 21, 22]
# 아래
down = [15, 16, 7, 8, 19, 20, 23, 24]

ans = 0
# 돌린다
for idx_lst in [front, back, right, left, up, down]:
    if turn(cube, idx_lst):
        ans = 1
        break

print(ans)

"""
9:06 시작
9:09 읽기 완료
9:30 구상 완료
10:00 tc 오류 발견
10:08 디버깅 - 마주하는 면 회전 누락

주사위 굴리기2를 어제 풀어서 어렵지 않게 풀었다.
면이 어디서부터 시작하는지 기준을 분명히 잡고 각 상황 별로 모두 적고 들어갔다.
"""

import sys

input = sys.stdin.readline


def change_col(nth, target, after):
    for i in range(3):
        target[i][nth] = after[i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    methods = list(input().split())
    pass

    up = [list('www') for _ in range(3)]
    down = [list('yyy') for _ in range(3)]
    front = [list('rrr') for _ in range(3)]
    back = [list('ooo') for _ in range(3)]
    left = [list('ggg') for _ in range(3)]
    right = [list('bbb') for _ in range(3)]

    for method in methods:
        word, pm = method

        if word == 'U':
            if pm == '+':
                up = list(map(list, zip(*up[::-1])))
                front[0], right[0], back[0], left[0] = right[0], back[0], left[0], front[0]

            else:
                up = list(map(list, zip(*up)))[::-1]
                front[0], right[0], back[0], left[0] = left[0], front[0], right[0], back[0]

        elif word == 'D':
            if pm == '+':
                down = list(map(list, zip(*down[::-1])))
                front[-1], right[-1], back[-1], left[-1] = left[-1], front[-1], right[-1], back[-1]

            else:
                down = list(map(list, zip(*down)))[::-1]
                front[-1], right[-1], back[-1], left[-1] = right[-1], back[-1], left[-1], front[-1]

        elif word == 'F':
            u_end_row = up[-1]
            r_fst_col = [row[0] for row in right]
            d_fst_row = down[0]
            l_end_col = [row[-1] for row in left]

            if pm == '+':
                front = list(map(list, zip(*front[::-1])))
                up[-1] = l_end_col[::-1]
                change_col(0, right, u_end_row)
                down[0] = r_fst_col[::-1]
                change_col(-1, left, d_fst_row)

            else:
                front = list(map(list, zip(*front)))[::-1]
                up[-1] = r_fst_col
                change_col(0, right, d_fst_row[::-1])
                down[0] = l_end_col
                change_col(-1, left, u_end_row[::-1])

        elif word == 'B':
            u_fst_row = up[0]
            r_end_col = [row[-1] for row in right]
            d_end_row = down[-1]
            l_fst_col = [row[0] for row in left]

            if pm == '+':
                back = list(map(list, zip(*back[::-1])))
                up[0] = r_end_col
                change_col(-1, right, d_end_row[::-1])
                down[-1] = l_fst_col
                change_col(0, left, u_fst_row[::-1])

            else:
                back = list(map(list, zip(*back)))[::-1]
                up[0] = l_fst_col[::-1]
                change_col(-1, right, u_fst_row)
                down[-1] = r_end_col[::-1]
                change_col(0, left, d_end_row)

        elif word == 'L':
            u_fst_col = [row[0] for row in up]
            f_fst_col = [row[0] for row in front]
            d_fst_col = [row[0] for row in down]
            b_end_col = [row[-1] for row in back]

            if pm == '+':
                left = list(map(list, zip(*left[::-1])))
                change_col(0, up, b_end_col[::-1])
                change_col(0, front, u_fst_col)
                change_col(0, down, f_fst_col)
                change_col(-1, back, d_fst_col[::-1])

            else:
                left = list(map(list, zip(*left)))[::-1]
                change_col(0, up, f_fst_col)
                change_col(0, front, d_fst_col)
                change_col(0, down, b_end_col[::-1])
                change_col(-1, back, u_fst_col[::-1])

        elif word == 'R':
            u_end_col = [row[-1] for row in up]
            f_end_col = [row[-1] for row in front]
            d_end_col = [row[-1] for row in down]
            b_fst_col = [row[0] for row in back]

            if pm == '+':
                right = list(map(list, zip(*right[::-1])))
                change_col(-1, up, f_end_col)
                change_col(-1, front, d_end_col)
                change_col(-1, down, b_fst_col[::-1])
                change_col(0, back, u_end_col[::-1])

            else:
                right = list(map(list, zip(*right)))[::-1]
                change_col(-1, up, b_fst_col[::-1])
                change_col(-1, front, u_end_col)
                change_col(-1, down, f_end_col)
                change_col(0, back, d_end_col[::-1])

    for row in up:
        print(''.join(row))
