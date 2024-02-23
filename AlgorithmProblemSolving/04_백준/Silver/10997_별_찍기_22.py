N = int(input())
# 1, 5, 9, 13
# 1, 7, 11, 15
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
W = 1 + (N - 1) * 4
H = 1 if N == 1 else W + 2
d = 0
arr = [[' '] * W for _ in range(H)]
ci, cj = 0, W - 1
ei, ej = H - 1 - (N - 1) * 2, W // 2
arr[ci][cj] = '*'

while not (ci == ei and cj == ej):

    ni, nj = ci + di[d], cj + dj[d]

    if not (0 <= ni < H and 0 <= nj < W):
        d = (d + 1) % 4
        continue

    if arr[ni][nj] == '*':
        arr[ci][cj] = ' '
        ci, cj = ci - di[d], cj - dj[d]
        d = (d + 1) % 4
        continue

    arr[ni][nj] = '*'

    ci, cj = ni, nj

for h in range(H):
    print("".join(arr[h]).rstrip())
