'''
직사각형 탈출
https://www.acmicpc.net/problem/16973
백준 골드4 16973

크기가 N×M인 격자판에 크기가 H×W인 직사각형이 놓여 있다. 격자판은 크기가 1×1인 칸으로 나누어져 있다. 격자판의 가장 왼쪽 위 칸은 (1, 1), 가장 오른쪽 아래 칸은 (N, M)이다. 직사각형의 가장 왼쪽 위칸은 (Sr, Sc)에 있을 때, 이 직사각형의 가장 왼쪽 위칸을 (Fr, Fc)로 이동시키기 위한 최소 이동 횟수를 구해보자.

격자판의 각 칸에는 빈 칸 또는 벽이 있다. 직사각형은 벽이 있는 칸에 있을 수 없다. 또한, 직사각형은 격자판을 벗어날 수 없다.

직사각형은 한 번에 왼쪽, 오른쪽, 위, 아래 중 한 방향으로 한 칸 이동시킬 수 있다.
'''

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
h, w, r, c, fr, fc = map(int, input().split())
h -= 1
w -= 1
r -= 1
c -= 1
fr -= 1
fc -= 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[-1]*m for _ in range(n)]


def inside(Y, X):
    return 0 <= Y and 0 <= X and Y+h < n and X+w < m


def check(Y, X):
    for i in range(Y, Y+h+1):
        if a[i][X] == 1 or a[i][X+w] == 1:
            return False
    for j in range(X, X+w+1):
        if a[Y][j] == 1 or a[Y+h][j] == 1:
            return False
    return True


q = deque()
q.append((r, c))
visited[r][c] = 0


while q:
    y, x = q.popleft()
    if y == fr and x == fc:
        break
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not inside(ny, nx):
            continue
        if visited[ny][nx] != -1:
            continue
        if not check(ny, nx):
            continue
        visited[ny][nx] = visited[y][x]+1
        q.append((ny, nx))

print(visited[fr][fc])
