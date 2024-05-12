N, M = map(int, input().split())
arr1 = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]

arr = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(arr1[i][j]^arr2[i][j])
    arr.append(row)

ans = 0
for i in range(N - 2):
    for j in range(M - 2):
        if arr[i][j]:
            ans += 1
            for ci in range(i, i + 3):
                for cj in range(j, j + 3):
                    arr[ci][cj] ^= 1
    if 1 in arr[i]:
        ans = -1
        break

if 1 in arr[i]:
    ans = -1
print(ans)