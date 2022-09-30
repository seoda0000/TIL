'''
5688. 세제곱근을 찾아라 D3
https://swexpertacademy.com/main/code/problem/problemDetail.do

양의 정수 N에 대해 N = X3가 되는 양의 정수X 를 구하여라.
'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = N ** (1/3)
    for i in range(int(x), int(x)+2):
        if i**3 == N:
            ans = i
            break
    else:
        ans = -1
    print(f'#{tc}', ans)
