def go(cur, x):  # cur에서 x번만큼 전진
    global route

    if cur in shortcut.keys():
        if cur == 10:
            route = 1
        cur = shortcut[cur]
        x -= 1

    for _ in range(x):
        if cur == 24 and route == 1:
            cur = shortcut[cur]
        else:
            cur = next_idx[cur]
    return cur


next_idx = list(range(1, 22)) + [21, 23, 24, 25, 26, 15] + [28, 24, 30, 20]
shortcut = {5: 22, 24: 29, 10: 27}

cur = 0
route = 0
is_win = False
turn = 1
while True:
    try:
        ipt = input()
        if len(ipt) < 4: break
    except EOFError:
        break

    back_cnt = ipt.count('0')
    if back_cnt == 1:
        cur = go(cur, 1)

    elif back_cnt == 2:
        cur = go(cur, 2)
    elif back_cnt == 3:
        cur = go(cur, 3)
    elif back_cnt == 4:
        cur = go(cur, 4)
        continue
    elif back_cnt == 0:
        cur = go(cur, 5)
        continue

    if turn <= 10 and cur == 21:
        is_win = True

    turn += 1

if is_win:
    print('WIN')
else:
    print('LOSE')
#
# """
# 상돈 프로님 풀이
# """
route = [
    [0] * 22,  # 4번
    [0] * 7,  # 2번
    [0] * 12,  # 3번
    [0] * 4  # 1번
]


def go(cur, x):
    global i

    if cur in route_dic[i].keys():
        i = route_dic[i][cur]
        cur = 0
        x -= 1

    cur += x
    return cur


i = cur = 0
route_dic = {0: {5: 2, 10: 1}, 1: {}, 2: {3: 3}, 3: {}}  # 현재 루트 i: {탈출장소: 다음 루트}
turn = 1
is_win = False
while True:
    try:
        ipt = input()
        if len(ipt) < 4: break
    except EOFError:
        break

    back_cnt = ipt.count('0')
    if back_cnt == 1:
        cur = go(cur, 1)

    elif back_cnt == 2:
        cur = go(cur, 2)
    elif back_cnt == 3:
        cur = go(cur, 3)
    elif back_cnt == 4:
        cur = go(cur, 4)
        continue
    elif back_cnt == 0:
        cur = go(cur, 5)
        continue

    if turn <= 10 and cur >= len(route[i]) - 1:
        is_win = True

    turn += 1

if is_win:
    print('WIN')
else:
    print('LOSE')

