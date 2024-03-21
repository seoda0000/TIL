'''
주지수
https://www.acmicpc.net/problem/15724
백준 실버1 15724


네모 왕국의 왕인 진경대왕은 왕국의 영토를 편하게 통치하기 위해서 1X1의 단위 구역을 여러 개 묶어서 하나의 거대 행정구역인 주지수(州地數, 마을의 땅을 셈)를 만들 예정이다.
진경대왕은 주지수를 만들기 위해서 일정한 직사각형 범위 내에 살고 있는 사람 수를 참고 자료로 쓰고 싶어한다.



진경대왕은 굉장히 근엄한 왕이기 때문에 당신에게 4개의 숫자로 직사각형 범위를 알려줄 것이다.

예를 들어, 위와 같이 사람이 살고 있다고 가정할 때 <그림 1>의 직사각형 범위의 사람 수를 알고 싶다면 진경대왕은 네 개의 정수 1 1 3 2를 부를 것이다.
마찬가지로 <그림 2>는 1 1 1 4, <그림 3>은 1 1 4 4가 될 것이다.

진경대왕을 위하여 이 참고 자료를 만들어내는 프로그램을 작성해보자.
'''


import sys
def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sumarr = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sumarr[i][j] = sumarr[i][j-1] + sumarr[i-1][j] - sumarr[i-1][j-1] + arr[i-1][j-1]
'''
해당 좌표까지의 숫자 합

0   0   0   0   0
0   1	3	6	10
0   3	8	15	23
0   6	17	29	41
0   10	26	44	63
'''
C = int(input())
clst = [list(map(int, input().split())) for _ in range(C)]
ans = []
for c in clst:
    i1, j1, i2, j2 = c
    ans.append(sumarr[i2][j2] - sumarr[i2][j1-1] - sumarr[i1-1][j2] + sumarr[i1-1][j1-1])

for a in ans:
    print(a)