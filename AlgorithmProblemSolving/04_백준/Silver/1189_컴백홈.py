'''
컴백홈
https://www.acmicpc.net/problem/1189
백준 실버1 1189

한수는 캠프를 마치고 집에 돌아가려 한다. 한수는 현재 왼쪽 아래점에 있고 집은 오른쪽 위에 있다. 그리고 한수는 집에 돌아가는 방법이 다양하다.
단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.

      cdef  ...f  ..ef  ..gh  cdeh  cdej  ...f
      bT..  .T.e  .Td.  .Tfe  bTfg  bTfi  .Tde
      a...  abcd  abc.  abcd  a...  a.gh  abc.
거리 :  6     6     6     8     8    10    6
위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다. T로 표시된 부분은 가지 못하는 부분이다.
문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.
'''


def f(ci, cj, k):
    global ans
    if ci == 0 and cj == C - 1:
        if k == K:
            ans += 1
        return
    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = ci + a, cj + b
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == '.' and v[ni][nj] == 0:
            v[ni][nj] = 1
            f(ni, nj, k + 1)
            v[ni][nj] = 0


R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
v = [[0] * C for _ in range(R)]
si, sj = R - 1, 0
v[si][sj] = 1
ans = 0
f(si, sj, 1)
print(ans)

"""
1년 후 풀이
"""


def goHome(ci, cj, h):
    global ans
    if h == K:
        if ci == 0 and cj == M - 1:
            ans += 1
        return

    v[ci][cj] = 1

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M): continue
        if v[ni][nj]: continue
        if arr[ni][nj] == 'T': continue
        goHome(ni, nj, h + 1)

    v[ci][cj] = 0

    return


N, M, K = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
si, sj = N - 1, 0

goHome(si, sj, 1)
print(ans)
