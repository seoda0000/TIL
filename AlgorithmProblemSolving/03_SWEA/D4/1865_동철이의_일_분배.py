'''
1865. 동철이의 일 분배 D4
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc

동철이가 차린 전자회사에는 N명의 직원이 있다.

그런데 어느 날 해야할 일이 N개가 생겼다.

동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.

직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.

여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.

직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.

우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.
'''


def dfs(n, x):
    global mx
    if x <= mx:
        return
    if n == N:
        if x > mx:
            mx = x
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, x*arr[n][i]/100)
            v[i] = 0


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    mx = 0
    dfs(0, 1)
    ans = mx*100
    print(f'#{tc} {ans:06.6f}')


"""
1년 후 풀이
round 함수와 f formatting을 잘 알아두자
"""

def toPercent(n: str):
    return int(n) / 100


def work(nth, p):
    global ans

    if nth == N:
        ans = max(ans, p)
        return

    if p <= ans:
        return

    for i in range(N):
        if v[i]: continue
        v[i] = 1
        work(nth + 1, p * arr[nth][i])
        v[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(toPercent, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 0
    work(0, 1)
    ans = round(ans*100, 6)

    print(f'#{test_case} {ans:0.6f}')
