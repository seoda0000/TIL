def print_pretty():
    for a in arr:
        print(*map(make_pretty, a))


def make_pretty(s):
    s = str(s)
    return s.rjust(wl)


r1, c1, r2, c2 = map(int, input().split())
mx_level = 0
mn_level = 5001
for idx in [c1, c2]:
    if idx > 0:
        mx_level = max(mx_level, idx - 1)
        mn_level = min(mn_level, idx - 1)
    else:
        mx_level = max(mx_level, abs(idx))
        mn_level = min(mn_level, abs(idx))

for idx in [r1, r2]:
    if idx >= 0:
        mx_level = max(mx_level, idx)
        mn_level = max(mn_level, idx)
    else:
        mx_level = max(mx_level, abs(idx + 1))
        mn_level = max(mn_level, abs(idx + 1))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
R = r2 - r1 + 1
C = c2 - c1 + 1
arr = [[0] * C for _ in range(R)]
remain = R * C

for l in range(max(0, mn_level - 50), mx_level + 1)[::-1]:
    if remain == 0:
        break
    num = ((l + 1) ** 2) * 4
    si, sj = -l - 1, -l
    ei, ej = l, l + 1
    ci, cj = si, sj
    dd = 0
    while num > (l ** 2) * 4:

        if r1 <= ci <= r2 and c1 <= cj <= c2:  # arr 범위 내

            # arr이 이미 찼을 경우 -> break
            if arr[ci - r1][cj - c1]:
                break

            # arr이 비었을 경우 -> arr에 기록
            else:
                arr[ci - r1][cj - c1] = num
                remain -= 1
        num -= 1
        ni, nj = ci + di[dd], cj + dj[dd]
        if not (si <= ni <= ei and sj <= nj <= ej):
            dd = (dd + 1) % 4
            ci, cj = ci + di[dd], cj + dj[dd]
            continue
        ci, cj = ni, nj

mxnum = 0
for i in range(R):
    mxnum = max(mxnum, max(arr[i]))

wl = len(str(mxnum))
print_pretty()
