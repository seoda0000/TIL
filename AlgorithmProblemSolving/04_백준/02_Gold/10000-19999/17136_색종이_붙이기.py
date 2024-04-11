def is_square(ci, cj, h):
    for i in range(ci, ci + h):
        for j in range(cj, cj + h):
            if not arr[i][j] or v[i][j]:
                return False
    return True


def check(si, sj, cnt, v):
    global ans
    if cnt >= ans:
        return

    for cj in range(sj, 10):
        ci = si
        if not v[ci][cj] and arr[ci][cj]:  # 색종이 발견

            mxh = min(4, min(9 - ci, 9 - cj)) + 1

            for h in range(1, mxh + 1)[::-1]:
                if is_square(ci, cj, h):

                    for i in range(ci, ci + h):
                        for j in range(cj, cj + h):
                            v[i][j] = 1

                    if remain[h] != 0:
                        remain[h] -= 1
                        check(ci, cj + 1, cnt + 1, v)
                        remain[h] += 1

                    for i in range(ci, ci + h):
                        for j in range(cj, cj + h):
                            v[i][j] = 0
            return

    for ci in range(si + 1, 10):
        for cj in range(10):
            if not v[ci][cj] and arr[ci][cj]:  # 색종이 발견

                mxh = min(4, min(9 - ci, 9 - cj)) + 1

                for h in range(1, mxh + 1)[::-1]:

                    if is_square(ci, cj, h):
                        for i in range(ci, ci + h):
                            for j in range(cj, cj + h):
                                v[i][j] = 1

                        if remain[h] != 0:
                            remain[h] -= 1
                            check(ci, cj + 1, cnt + 1, v)
                            remain[h] += 1

                        for i in range(ci, ci + h):
                            for j in range(cj, cj + h):
                                v[i][j] = 0
                return

    for i in range(10):
        for j in range(10):
            if arr[i][j] and not v[i][j]:
                return
    ans = min(ans, cnt)

    return


arr = [list(map(int, input().split())) for _ in range(10)]
SM = sum([sum(a) for a in arr])
ans = 101
v = [[0] * 10 for _ in range(10)]
remain = [0] + [5] * 5
check(0, 0, 0, v)
if ans == 101:
    ans = -1
print(ans)
