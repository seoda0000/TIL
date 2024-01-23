'''
13702. 델타검색 D2
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AX73EWcKxLYDFARO

N x N 2차원 리스트가 입력됩니다.
어느 한 요소에 대하여 상,하,좌,우로 이웃한 요소와의 차의 절대값들을 구하고 이들의 합을 구하려 합니다.

NxN 리스트에 있는 모든 요소들에 대해서 위처럼 조사하여 이들을 전부 더한 총합을 구해주세요.
단, [0][0] 처럼 이웃한 요소가 2개인 값은 2개 대해서만 합을 구해줍니다.

'''
import sys

sys.stdin = open('s_list2_연습문제1_iin.txt', 'r')

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):

            # 상하좌우 적용
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ni = i + di
                nj = j + dj

                # 범위를 벗어났는지 파악 후 계산
                if 0 <= ni < N and 0 <= nj < N:
                    ans += abs(arr[i][j] - arr[ni][nj])

    print(f"#{case}", ans)

"""
아이디어를 적용한 풀이
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 절댓값은 언제나 두 번 더해진다는 것에 주목

    # 가로 인접 계산
    for i in range(N):
        for j in range(N - 1):
            ans += abs(arr[i][j] - arr[i][j + 1]) * 2

    # 세로 인접 계산
    for j in range(N):
        for i in range(N - 1):
            ans += abs(arr[i][j] - arr[i + 1][j]) * 2

    print(f'#{test_case} {ans}')
