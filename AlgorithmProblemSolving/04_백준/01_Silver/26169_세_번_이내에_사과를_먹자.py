from collections import deque


def canEatApple(ci, cj, cnt, nth):
    global ans
    if cnt >= 2:
        ans = 1
        return
    if nth == 3:
        return

    v[ci][cj] = 1
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < 5 and 0 <= nj < 5): continue
        if arr[ni][nj] < 0: continue
        if v[ni][nj]: continue
        canEatApple(ni, nj, cnt + arr[ni][nj], nth + 1)
    v[ci][cj] = 0

    return


arr = [list(map(int, input().split())) for _ in range(5)]
v = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0
canEatApple(r, c, 0, 0)

print(ans)
