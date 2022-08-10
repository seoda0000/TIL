'''
1954. 달팽이 숫자 D2
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

'''
import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    ary = [[0]*N for _ in range(N)]

    i, j = 0, -1 # 좌표 초기값
    d = 1 # 방향 1:오른쪽 2:아래쪽 3:왼쪽 4:위쪽
    n = 1 # 숫자 초기값
    while n <= N**2:

        if d == 1: # 오른쪽으로
            j += 1
            if j == N-1 or ary[i][j+1] != 0: # 끝에 다다른 경우 방향 전환
                d = 2
        elif d == 2: # 아래쪽으로
            i += 1
            if i == N-1 or ary[i+1][j] != 0: # 끝에 다다른 경우 방향 전환
                d = 3
        elif d == 3: # 왼쪽으로
            j -= 1
            if i == 0 or ary[i][j-1] != 0: # 끝에 다다른 경우 방향 전환
                d = 4
        elif d == 4: # 위쪽으로
            i -= 1
            if ary[i-1][j] != 0: # 끝에 다다른 경우 방향 전환
                d = 1
        ary[i][j] = n # 숫자 배정
        n += 1
    for a in ary:
        print(*a)


