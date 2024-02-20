def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == K:
                return i, j


N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
ci = cj = (N - 1) // 2
arr[ci][cj] = n = 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
d = 0
for i in range(1, N):
    for _ in range(2):
        for j in range(i):
            ci = ci + di[d]
            cj = cj + dj[d]
            n += 1
            arr[ci][cj] = n
        d = (d + 1) % 4
for i in range(N - 1):
    ci = ci + di[d]
    cj = cj + dj[d]
    n += 1
    arr[ci][cj] = n


for a in arr:
    print(*a)


ai, aj = find()
print(ai + 1, aj + 1)
