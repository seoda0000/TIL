def check_cross(i, j):
    global remain

    mxh = min(i - 1, j - 1, M - j, N - i)
    ansh = 0
    for h in range(1, mxh + 1):
        for d in range(4):
            ni, nj = i + di[d] * h, j + dj[d] * h
            if arr[ni][nj] != '*':
                return ansh
        if not v[i][j]:
            v[i][j] = 1
            remain -= 1
        for d in range(4):
            ni, nj = i + di[d] * h, j + dj[d] * h
            if v[ni][nj]: continue
            v[ni][nj] = 1
            remain -= 1

        ansh = h
    return ansh


N, M = map(int, input().split())
arr = ['.' * (M + 1)] + ['.' + input() for _ in range(N)]
remain = 0
for i in range(1, N + 1):
    remain += arr[i].count('*')
v = [[0] * (M + 1) for _ in range(N + 1)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i][j] == '*':
            k = check_cross(i, j)
            if k > 0:
                ans.append((i, j, k))

if remain:
    print(-1)
else:
    print(len(ans))
    for a in ans:
        print(*a)
