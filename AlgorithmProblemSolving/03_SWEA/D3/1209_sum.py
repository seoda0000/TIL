'''
1209. [S/W 문제해결 기본] 2일차 - Sum D3
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
'''

import sys
sys.stdin = open('s_input.txt', 'r')

for tc in range(1, 3):
    N = int(input())
    ary = [list(map(int, input().split())) for _ in range(100)]
    ans = 0

    # 행
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += ary[i][j]
        if tmp > ans:
            ans = tmp

    # 열
    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += ary[i][j]
        if tmp > ans:
            ans = tmp

    # 오른쪽 아래 방향 대각선
    tmp = 0
    for i in range(100):
        tmp += ary[i][i]
    if tmp > ans:
        ans = tmp

    # 왼쪽 위 방향 대각선
    tmp = 0
    for i in range(100):
        tmp += ary[i][99-i]
    if tmp > ans:
        ans = tmp

    print(f'#{tc}', ans)