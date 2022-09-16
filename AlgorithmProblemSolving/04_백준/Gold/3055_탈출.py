'''
탈출
https://www.acmicpc.net/problem/3055
백준 골드4 3055
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다.
이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다.
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다.
또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다.
즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.
'''


import sys
def input():
    return sys.stdin.readline().rstrip()
from collections import deque



R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

bi, bj = di, dj = si, sj = 0, 0

q = deque([])
qh = deque([])
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            bi, bj = i, j
            q.append((i, j))
        elif arr[i][j] == 'D':
            di, dj = i, j
        elif arr[i][j] == 'S':
            si, sj = i, j
            qh.append((i, j))



t = 0
bp = True
while bp and qh:
    t += 1
    for _ in range(len(q)):
        i, j = q.popleft()
        for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + a
            nj = j + b
            if 0<=ni<R and 0<=nj<C and (arr[ni][nj] == '.' or arr[ni][nj] == 'S'):
                arr[ni][nj] = '*'
                q.append((ni, nj))
    for _ in range(len(qh)):
        i, j = qh.popleft()
        for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + a
            nj = j + b
            if 0<=ni<R and 0<=nj<C :
                if arr[ni][nj] == '.':
                    arr[ni][nj] = 'S'
                    qh.append((ni, nj))
                if arr[ni][nj] == 'D':
                    bp = False
                    break
if bp:
    ans = 'KAKTUS'
else:
    ans = t
print(ans)



