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
