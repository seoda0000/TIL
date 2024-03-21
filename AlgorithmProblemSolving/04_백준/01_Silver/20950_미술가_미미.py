import sys

input = sys.stdin.readline


def get_color(nth, before):
    # 차이 갱신
    check_color()

    if nth == 7:
        return

    for n in range(before + 1, N):
        if v[n]: continue

        v[n] = 1
        get_color(nth + 1, n)
        v[n] = 0

    return


def check_color():
    global ans

    cnt = sum(v)
    if cnt <= 1: return

    mr, mg, mb = 0, 0, 0
    for n in range(N):
        if v[n]:
            mr += colors[n][0]
            mg += colors[n][1]
            mb += colors[n][2]

    mr, mg, mb = mr // cnt, mg // cnt, mb // cnt
    res = abs(mr - tr) + abs(mg - tg) + abs(mb - tb)
    ans = min(ans, res)

    return


N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
tr, tg, tb = map(int, input().split())
v = [0] * N
ans = 255 * 3
get_color(0, -1)
print(ans)
