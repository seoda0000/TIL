'''
구간합 구하기 5
https://www.acmicpc.net/problem/11660
백준 실버1 11660
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7
여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.
'''

import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sumarr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sumarr[i][j] = sumarr[i][j - 1] + sumarr[i - 1][j] - sumarr[i - 1][j - 1] + arr[i - 1][j - 1]
'''
해당 좌표까지의 숫자 합

0   0   0   0   0
0   1	3	6	10
0   3	8	15	23
0   6	17	29	41
0   10	26	44	63
'''
clst = [list(map(int, input().split())) for _ in range(M)]
ans = []
for c in clst:
    i1, j1, i2, j2 = c
    ans.append(sumarr[i2][j2] - sumarr[i2][j1 - 1] - sumarr[i1 - 1][j2] + sumarr[i1 - 1][j1 - 1])

for a in ans:
    print(a)

"""
1년 후 풀이
"""

N, M = map(int, input().split())
arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
smArr = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        smArr[i][j] = smArr[i][j - 1] + smArr[i - 1][j] - smArr[i - 1][j - 1] + arr[i][j]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sm = smArr[x2][y2] - smArr[x1 - 1][y2] - smArr[x2][y1 - 1] + smArr[x1 - 1][y1 - 1]
    print(sm)

"""
가로 세로 순회 2번 하는 풀이 (더 빠르다)
"""
N, M = map(int, input().split())
arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
smArr = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        smArr[i][j] = smArr[i][j - 1] + arr[i][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        smArr[i][j] = smArr[i - 1][j] + smArr[i][j]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sm = smArr[x2][y2] - smArr[x1 - 1][y2] - smArr[x2][y1 - 1] + smArr[x1 - 1][y1 - 1]
    print(sm)
