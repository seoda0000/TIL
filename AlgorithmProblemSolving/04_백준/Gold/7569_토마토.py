'''
토마토
https://www.acmicpc.net/problem/7569
백준 골드5 7569

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.


창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
box = deque([])
start = 1
for _ in range(H):
    arr = deque([list(map(int, input().split())) for _ in range(N)])
    for a in arr:
        if 0 in a:    # 덜 익은 게 있으면 0으로 바꿔줌
            start = 0
    box.append(arr)

if start:             # 처음부터 모두 익어있는 경우 0 return
    ans = 0
else:
    a = 1
    q = deque([])
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == a:
                    q.append((h, n, m, a))    # 익은 토마토 (h, n, m : 좌표, a : 며칠째) q에 push
    while q:
        # q에서 꺼내고 상하좌우앞뒤가 0인지 파악. 0이면 box를 a로 바꾸고 (좌표, a+1) push
        z, y, x, a = q.popleft()
        if 0 <= z + 1 < H and 0 <= y < N and 0 <= x < M and box[z + 1][y][x] == 0:
            box[z + 1][y][x] = a
            q.append((z + 1, y, x, a+1))
        if 0 <= z - 1 < H and 0 <= y < N and 0 <= x < M and box[z - 1][y][x] == 0:
            box[z - 1][y][x] = a
            q.append((z - 1, y, x, a+1))
        if 0 <= z < H and 0 <= y + 1 < N and 0 <= x < M and box[z][y + 1][x] == 0:
            box[z][y + 1][x] = a
            q.append((z, y+ 1, x, a+1))
        if 0 <= z < H and 0 <= y - 1 < N and 0 <= x < M and box[z][y - 1][x] == 0:
            box[z][y - 1][x] = a
            q.append((z, y-1, x, a+1))
        if 0 <= z < H and 0 <= y < N and 0 <= x + 1 < M and box[z][y][x + 1] == 0:
            box[z][y][x + 1] = a
            q.append((z, y, x+1, a+1))
        if 0 <= z < H and 0 <= y < N and 0 <= x - 1 < M and box[z][y][x - 1] == 0:
            box[z][y][x - 1] = a
            q.append((z, y, x-1, a+1))

    ZeroInEnd = 0
    mx = deque([])
    for a in box:            # 마지막 점검
        for b in a:
            mx.append(max(b))    # 행 중 가장 큰 값 mx 리스트에 추가하기
            if 0 in b:           # 0이 남아있다면 ZeroInEnd 처리
                ZeroInEnd = 1
    if ZeroInEnd:                # 0이 남아있다면 -1 return
        ans = -1
    else:                        # 아니라면 전체 최대값 return
        ans = max(mx)
print(ans)