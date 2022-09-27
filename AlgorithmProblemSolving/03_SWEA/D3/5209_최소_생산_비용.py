'''
5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.
'''
import sys
sys.stdin = open('s_input (1).txt', 'r')


def f(n, s):
    global mn
    if s > mn:
        return

    if n == N:
        mn = s
        return
    for i in range(N):
        if not v[i]:
            v[i] = 1
            f(n+1, s+arr[n][i])
            v[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    mn = 99 * N * N
    f(0, 0)
    print(f'#{tc}', mn)