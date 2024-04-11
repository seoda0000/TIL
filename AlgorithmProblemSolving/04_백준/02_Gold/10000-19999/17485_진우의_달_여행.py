import sys
input = sys.stdin.readline



N, M = map(int, input().split())
arr = []
check = [[[list() for _ in range(3)] for _ in range(M)] for _ in range(N)]
inf = 100*10000
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(M):
    for j in range(3):
        check[0][i][j] = arr[0][i]

for n in range(1, N):
    for m in range(M):

        # 왼쪽에서 오는 경우
        if m == 0:
            check[n][m][0] = inf
        else:
            check[n][m][0] = min(check[n-1][m-1][1], check[n-1][m-1][2]) + arr[n][m]

        # 위에서 오는 경우
        check[n][m][1] = min(check[n-1][m][0], check[n-1][m][2]) + arr[n][m]

        # 오른쪽에서 오는 경우
        if m == M-1:
            check[n][m][2] = inf
        else:
            check[n][m][2] = min(check[n-1][m+1][0], check[n-1][m+1][1]) + arr[n][m]

answer = inf
for m in range(M):
    answer = min(answer, min(check[N-1][m]))
print(answer)


