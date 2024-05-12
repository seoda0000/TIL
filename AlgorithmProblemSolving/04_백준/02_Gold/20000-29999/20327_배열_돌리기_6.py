X, R = map(int, input().split())
N = 2 ** X
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    K, L = map(int, input().split())
    n = 2 ** L  # 부분집합 길이
    brr = []  # 부분집합 배열

    for si in range(0, N, n):
        row = []
        for sj in range(0, N, n):
            square = [a[sj:sj + n] for a in arr[si:si + n]]
            row.append(square)
        brr.append(row)

    if K == 1:
        for bi in range(N // n):
            for bj in range(N // n):
                brr[bi][bj] = brr[bi][bj][::-1]
    elif K == 2:
        for bi in range(N // n):
            for bj in range(N // n):
                brr[bi][bj] = [b[::-1] for b in brr[bi][bj]]
    elif K == 3:
        for bi in range(N // n):
            for bj in range(N // n):
                brr[bi][bj] = list(map(list, zip(*brr[bi][bj][::-1])))
    elif K == 4:
        for bi in range(N // n):
            for bj in range(N // n):
                brr[bi][bj] = list(map(list, zip(*brr[bi][bj])))[::-1]
    elif K == 5:
        brr = brr[::-1]
    elif K == 6:
        brr = [b[::-1] for b in brr]
    elif K == 7:
        brr = list(map(list, zip(*brr[::-1])))
    else:
        brr = list(map(list, zip(*brr)))[::-1]

    for si in range(N // n):
        for sj in range(N // n):
            square = brr[si][sj]
            for i in range(n):
                for j in range(n):
                    arr[si * n + i][sj * n + j] = square[i][j]

for a in arr:
    print(*a)
