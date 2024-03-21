from collections import defaultdict


def go_from(n, cnt):
    global mx

    cnts[n] = cnt

    if n == 100:
        return

    if bridges[n]:
        if cnts[bridges[n]] > cnt:
            go_from(bridges[n], cnt)
    else:
        for x in range(1, 7)[::-1]:
            if n + x <= 100 and cnts[n + x] > cnt + 1:
                go_from(n + x, cnt + 1)


N, M = map(int, input().split())
bridges = defaultdict(int)
cnts = [1000] * 101
for _ in range(N + M):
    a, b = map(int, input().split())
    bridges[a] = b
go_from(1, 0)
print(cnts[-1])
