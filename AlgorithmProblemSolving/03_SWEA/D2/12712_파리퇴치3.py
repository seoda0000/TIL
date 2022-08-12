'''
12712. 파리퇴치3 D2
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.

아래는 N=5 의 예이다.

파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.

한 번에 잡을 수 있는 최대 파리수를 출력하라.
'''

import sys
sys.stdin = open('s_in1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 십자

    for i in range(N):
        for j in range(N):
            tmp = 0
            for a in range(i-M+1, i+M): # 세로 분사
                if 0 <= a <= N-1: # 범위 내인지 판단
                    tmp += arr[a][j] # 파리 죽이기
            for b in range(j-M+1, j+M): # 가로 분사
                if 0 <= b <= N-1:
                    tmp += arr[i][b] # 파리 죽이기
            tmp -= arr[i][j] # 겹치는 지점 빼기
            if tmp > ans :
                ans = tmp

    # X자
    for i in range(N):
        for j in range(N):
            tmp = 0
            for c in range(-M+1, M): # 오른쪽 아래 분사
                if 0 <= i+c <= N-1 and 0 <= j+c <= N-1: # 범위 내인지 판단
                    tmp += arr[i+c][j+c] # 파리 죽이기
            for d in range(-M+1, M): # 왼쪽 아래 분사
                if 0 <= i-d <= N-1 and 0 <= j+d <= N-1: # 범위 내인지 판단
                    tmp += arr[i-d][j+d] # 파리 죽이기
            tmp -= arr[i][j] # 겹치는 지점 빼기
            if tmp > ans:
                ans = tmp

    print(f'#{tc}', ans)

