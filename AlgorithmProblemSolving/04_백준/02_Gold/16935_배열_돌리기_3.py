N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

for order in orders:
    if order == 1:
        arr = arr[::-1]
    elif order == 2:
        arr = [a[::-1] for a in arr]
    elif order == 3:
        arr = list(map(list, zip(*arr[::-1])))
        N, M = M, N
    elif order == 4:
        arr = list(map(list, zip(*arr)))[::-1]
        N, M = M, N
    else:
        squares = []

        for si in range(0, N, N // 2):
            for sj in range(0, M, M // 2):
                square = [a[sj:sj + M // 2] for a in arr[si:si + N // 2]]
                squares.append(square)

        if order == 5:
            squares = [squares[2]] + [squares[0]] + [squares[3]] + [squares[1]]
        else:
            squares = [squares[1]] + [squares[3]] + [squares[0]] + [squares[2]]

        for si in range(0, N, N // 2):
            for sj in range(0, M, M // 2):
                square = squares[0]

                for i in range(N // 2):
                    for j in range(M // 2):
                        arr[si + i][sj + j] = square[i][j]
                squares.pop(0)

for a in arr:
    print(*a)
