"""
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYlGU56XOkDFARc
"""

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = 0

    for i in range(N):
        for j in range(M):
            temp = arr[i][j]

            for n in range(4):
                ni, nj = i + dx[n], j + dy[n]

                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]

            ans = max(temp, ans)

    print(f'#{test_case} {ans}')
