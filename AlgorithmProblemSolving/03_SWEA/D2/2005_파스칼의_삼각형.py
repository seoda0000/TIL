'''
2005. 파스칼의 삼각형 D2
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

'''

import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    ans = [[1]] + [[] for _ in range(N-1)] # 첫 줄과 나머지 빈칸 줄 생성
    
    for i in range(1, N):                  # 1부터 N-1까지
        ans[i].append(1)                        # 첫 1 추가
        for j in range(1, i):                   # 중간 줄 추가
            n = ans[i-1][j-1] + ans[i-1][j]         # 윗줄 두 숫자의 합 추가
            ans[i].append(n)
        ans[i].append(1)                        # 마지막 1 추가

    for a in ans:
        print(*a)