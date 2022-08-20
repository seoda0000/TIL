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