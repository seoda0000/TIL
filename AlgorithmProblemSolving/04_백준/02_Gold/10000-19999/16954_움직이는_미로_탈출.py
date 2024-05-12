"""
백준 골드3 16954
움직이는 미로 탈출
https://www.acmicpc.net/problem/16954

욱제는 학교 숙제로 크기가 8×8인 체스판에서 탈출하는 게임을 만들었다. 체스판의 모든 칸은 빈 칸 또는 벽 중 하나이다. 욱제의 캐릭터는 가장 왼쪽 아랫 칸에 있고, 이 캐릭터는 가장 오른쪽 윗 칸으로 이동해야 한다.

이 게임의 특징은 벽이 움직인다는 점이다. 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 아래에 행이 없다면 벽이 사라지게 된다. 욱제의 캐릭터는 1초에 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있다. 이동할 때는 빈 칸으로만 이동할 수 있다.

1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다. 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.

욱제의 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해보자.
"""

import sys
from collections import deque
input = sys.stdin.readline

arr = [input().strip() for _ in range(8)]
wall = set()
answer = 0

for i in range(8):
    for j in range(8):
        if arr[i][j] == '#':
            wall.add((i, j))

ab = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
visited = set()
q = deque()
q.append((7, 0))

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        if (x, y) in wall:
            continue
        if x == 0  and y == y:
            answer = 1
            break

        for a, b in ab:
            nx = x + a
            ny = y + b
            if 0 <= nx < 8 and 0 <= ny < 8 and not (nx, ny) in visited and not (nx, ny) in wall:
                visited.add((nx, ny))
                q.append((nx, ny))
    if wall:
        visited = set()
    next_wall = set()
    for x, y in wall:
        if x < 7:
            next_wall.add((x+1, y))
    wall = next_wall
print(answer)
