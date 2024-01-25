"""
https://www.acmicpc.net/problem/17069
백준 골드4 파이프 옮기기 2

파이프 옮기기 1의 dfs 코드는 시간초과가 나서 dp를 이용했다.
"""

N = int(input())
arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
N += 2
arr.insert(0, [0] * N)
arr.append([0] * N)

hori = [[0] * N for i in range(N)]
vert = [[0] * N for i in range(N)]
diag = [[0] * N for i in range(N)]

hori[1][2] = 1

for i in range(1, N - 1):
    for j in range(1, N - 1):
        if arr[i][j] == 0:

            # 가로
            hori[i][j] += hori[i][j - 1]
            hori[i][j] += diag[i][j - 1]

            # 세로
            vert[i][j] += vert[i - 1][j]
            vert[i][j] += diag[i - 1][j]

            # 대각선
            # 만약 왼쪽과 위쪽이 비어있다면
            if arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
                diag[i][j] += diag[i - 1][j - 1]
                diag[i][j] += vert[i - 1][j - 1]
                diag[i][j] += hori[i - 1][j - 1]

print(hori[N - 2][N - 2] + vert[N - 2][N - 2] + diag[N - 2][N - 2])
