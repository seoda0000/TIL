'''
 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 D2
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

예를 들어 다음과 같이 배열이 주어진다.

2 1 2
5 8 5
7 2 2

이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.
'''

import sys
sys.stdin = open('s_input.txt', 'r')

def solve(i, N, b, s):
    global ans
    if s >= ans:
        return
    if i == N:
        if ans > s:
            ans = s
        else:
            return

    else:
        for n in range(N):
            if n not in b:
                tmpbit = b[:]
                tmpbit[i] = n
                solve(i+1, N, tmpbit, s+arr[i][n])

            '''
            if not visited[n]:              # visited = [0]*N
                visited[n] = 1
                solve(i+1, N, s+arr[i][n])
                visited[n] = 0              # clear 해줘야 함!!
            '''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = {n:list(map(int, input().split())) for n in range(N)}
    ans = 10*N
    bit = [-1] * N
    solve(0, N, bit, 0)
    print(f'#{tc}', ans)


# ===============================================================


def dfs(n, s):
    global mn
    if n == N:
        if mn > s:
            mn = s
    elif s < mn:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(n+1, s+arr[n][i])
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    mn = 10 * N
    dfs(0, 0)


    print(f'#{tc}', mn)
