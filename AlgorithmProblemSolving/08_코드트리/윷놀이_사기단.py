"""
2:20 시작
2:27 구상완료
2:37 디버깅 - 인덱스 오류
2:40 제출
"""


def move(cur, dice):
    if cur in blue.keys():  # 파란 칸
        cur = blue[cur]
        dice -= 1
    for _ in range(dice):
        cur = nxt[cur]

    if cur != 21 and cur in horses:
        cur = -1
    return cur


def dfs(turn, sm):
    global ans

    if turn == 10:
        ans = max(ans, sm)
        return

    for x in range(4):
        cur = horses[x]
        if cur == 21:
            continue
        nxt = move(cur, dice_lst[turn])
        if nxt >= 0:
            horses[x] = nxt
            dfs(turn + 1, sm + score[nxt])
            horses[x] = cur

    return


score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0,
         13, 16, 19, 25, 30, 35,
         22, 24,
         28, 27, 26]
nxt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
       12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21,
       23, 24, 25, 26, 27, 20,
       29, 25,
       31, 32, 25]
blue = {5: 22, 10: 28, 15: 30}
horses = [0] * 4
dice_lst = list(map(int, input().split()))
ans = 0
dfs(0, 0)
print(ans)
