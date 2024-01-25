"""
SWEA D4 4613 러시아 국기 같은 깃발
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj
"""
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    base = 2 * M - flag[0].count('W') - flag[-1].count('R')

    cnt = 50 * 50

    for s in range(1, N - 1):
        for e in range(s, N - 1):
            temp = M * (N - 2)

            # 흰색
            for i in range(1, s):
                temp -= flag[i].count('W')

            # 파란색
            for i in range(s, e + 1):
                temp -= flag[i].count('B')

            # 빨간색
            for i in range(e + 1, N - 1):
                temp -= flag[i].count('R')

            cnt = min(cnt, temp)

    print(f'#{test_case} {base + cnt}')

"""
count 배열 활용
"""

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    base = 2 * M - flag[0].count('W') - flag[-1].count('R')
    flagCnt = [[0] * M for _ in range(N)]

    for n in range(N):  # count 배열 만들기
        flagCnt[n][0] = flag[n].count('W')
        flagCnt[n][1] = flag[n].count('B')
        flagCnt[n][2] = M - flagCnt[n][0] - flagCnt[n][1]

    cnt = 50 * 50

    for s in range(1, N - 1):
        for e in range(s, N - 1):
            temp = M * (N - 2)

            # 흰색
            for i in range(1, s):
                temp -= flagCnt[i][0]

            # 파란색
            for i in range(s, e + 1):
                temp -= flagCnt[i][1]

            # 빨간색
            for i in range(e + 1, N - 1):
                temp -= flagCnt[i][2]

            cnt = min(cnt, temp)

    print(f'#{test_case} {base + cnt}')
