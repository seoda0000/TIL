N, M = map(int, input().split())
arr = [['.'] * (M + 2)] + [['.'] + list(input()) + ['.'] for _ in range(N)] + [['.'] * (M + 2)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
to_sea = []
mxi, mxj, mni, mnj = 0, 0, N + 1, M + 1

for i in range(N + 2):
    for j in range(M + 2):
        if arr[i][j] == '.': continue
        cnt = 0
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]

            if not (0 <= ni < N + 2, 0 <= nj < M + 2): continue
            if arr[ni][nj] == 'X': continue
            cnt += 1
        if cnt >= 3:
            to_sea.append((i, j))
        else:
            mxi = max(mxi, i)
            mxj = max(mxj, j)
            mni = min(mni, i)
            mnj = min(mnj, j)
for si, sj in to_sea:
    arr[si][sj] = '.'



for i in range(mni, mxi + 1):
    print(''.join(arr[i][mnj:mxj + 1]))
