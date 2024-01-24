'''
2805. 농작물 수확하기 D3
https://swexpertacademy.com/main/code/problem/problemDetail.do
N X N크기의 농장이 있다.
이 농장에는 이상한 규칙이 있다.
규칙은 다음과 같다.


   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.

농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr=[list(map(int, list(input()))) for _ in range(N)]
    ans = 0

    for i in range(N//2+1):             # 첫열부터 중간열까지
        for j in range(-i, i+1):
            ans += arr[i][N//2+j]
    for i in range(N//2+1, N+1):        # 그 이후 열들
        for j in range(-N+i+1, N-i):
            ans += arr[i][N//2+j]
    print(f'#{tc}', ans)

"""
모든 영역 한번에 계산하기
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    center = N // 2  # 중앙값
    ans = 0
    for n in range(N):
        num = min(N-n-1, n)      # (행에 따라 중앙값을 중심으로 추가되어야 할 열 / 2)

        temp = arr[n][center]        # 중앙값을 먼저 더해준다

        for i in range(1, num+1):  # 양 옆의 추가 값을 더해준다
            temp += arr[n][center-i] + arr[n][center+i]

        ans += temp

    print(f'#{test_case} {ans}')