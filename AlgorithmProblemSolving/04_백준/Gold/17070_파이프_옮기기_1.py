"""
https://www.acmicpc.net/problem/17070

백준 17070 골드5 파이프 옮기기 1
bfs로 풀자 시간초과가 떠서 dfs로 다시 풀었다.

"""


def dfs(i, j, s):
    global ans
    if i == N - 1 and j == N - 1:
        ans += 1

    if s == hori:  # 현재 가로
        if 0 <= j + 1 < N and arr[i][j + 1] == 0:
            # 가로 이동 처리
            dfs(i, j + 1, hori)

            if 0 <= i + 1 < N and arr[i + 1][j] == 0 and arr[i + 1][j + 1] == 0:
                # 대각선 이동 처리
                dfs(i + 1, j + 1, diag)

    elif s == vert:  # 현재 세로
        if 0 <= i + 1 < N and arr[i + 1][j] == 0:
            # 세로 이동 처리
            dfs(i + 1, j, vert)

            if 0 <= j + 1 < N and arr[i][j + 1] == 0 and arr[i + 1][j + 1] == 0:
                # 대각선 이동 처리
                dfs(i + 1, j + 1, diag)

    else:  # 현재 대각선
        flag1 = flag2 = False
        if 0 <= j + 1 < N and arr[i][j + 1] == 0:
            # 가로 이동 처리
            dfs(i, j + 1, hori)
            flag1 = True
        if 0 <= i + 1 < N and arr[i + 1][j] == 0:
            # 세로 이동 처리
            dfs(i + 1, j, vert)
            flag2 = True
        if flag1 and flag2 and arr[i + 1][j + 1] == 0:
            # 대각선 이동 처리
            dfs(i + 1, j + 1, diag)

    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
hori, vert, diag = 0, 1, 2  # 가로, 세로, 대각선 값
ei, ej = 0, 1
status = hori
ans = 0

dfs(ei, ej, status)

print(ans)
