"""
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


def check(cube):
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
