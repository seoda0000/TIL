"""
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXAerAPaVXMDFARP
SWEA D2 풍선팡
"""

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    ans = 0

    for i in range(N):
        for j in range(M):
            num = temp = arr[i][j]

            for n in range(4):
                for t in range(1, num + 1):  # 풍선 숫자만큼 4방향 배수 count
                    ni, nj = i + di[n] * t, j + dj[n] * t
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += arr[ni][nj]
            ans = max(ans, temp)

    print(f'#{test_case} {ans}')
