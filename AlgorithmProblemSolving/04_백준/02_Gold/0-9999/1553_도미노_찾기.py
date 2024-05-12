from collections import defaultdict


def put_domino(bi, bj, cnt, v):
    global ans

    ci, cj = bi, bj
    while v[ci][cj]:  # 다음 위치 설정
        cj += 1
        if cj > 6:
            ci += 1
            cj = 0
        if ci > 7:  # 모든 도미노 완료
            ans += 1
            return

    if cj + 1 <= 6 and v[ci][cj + 1] == 0:  # 가로
        a, b = arr[ci][cj], arr[ci][cj + 1]
        a, b = min(a, b), max(a, b)
        if dic[(a, b)] == 0:
            dic[(a, b)] = 1
            v[ci][cj] = 1
            v[ci][cj + 1] = 1
            put_domino(ci, cj, cnt + 1, v)
            dic[(a, b)] = 0
            v[ci][cj] = 0
            v[ci][cj + 1] = 0

    if ci + 1 <= 7 and v[ci + 1][cj] == 0:  # 세로
        a, b = arr[ci][cj], arr[ci + 1][cj]
        a, b = min(a, b), max(a, b)
        if dic[(a, b)] == 0:
            dic[(a, b)] = 1
            v[ci][cj] = 2
            v[ci + 1][cj] = 2
            put_domino(ci, cj, cnt + 1, v)
            dic[(a, b)] = 0
            v[ci][cj] = 0
            v[ci + 1][cj] = 0

    return


arr = [list(map(int, input())) for _ in range(8)]
v = [[0] * 7 for _ in range(8)]
dic = defaultdict(int)
ans = 0
put_domino(0, 0, 0, v)
print(ans)
