"""
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

ab = [(-1, 0), (0, -1), (0, 1), (1, 0)]

size = 2
visited = [[0]*N for _ in range(N)]

# 물고기 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0
            q = deque([(si, sj)])
            visited[si][sj] = 1
            break

ans = 0
t = 0
cnt = 0              # 먹은 물고기 수

while q:
    if cnt == size:  # 물고기 성장
        size += 1
        cnt = 0
    t += 1
    tlst = []        # 먹잇감 리스트
    nlst = []        # 다음 이동지 리스트

    while q:
        i, j = q.popleft()

        for a, b in ab:
            if 0<=i+a<N and 0<=j+b<N and visited[i+a][j+b] == 0:
                if 0 < arr[i+a][j+b] < size:     # 먹잇감 발견
                    tlst.append((i+a, j+b))
                elif arr[i + a][j + b] <= size:  # 이동 가능
                    nlst.append((i + a, j + b))
                visited[i+a][j+b] = 1
    if tlst:                                     # 먹잇감 후보가 있다면
        tlst.sort()
        si, sj = tlst[0]                            # 우선순위 적용해서 먹기
        arr[si][sj] = 0
        ans = t                                     # 시간 갱신
        cnt += 1                                    # 먹은 물고기 수 증가
        q = deque([(si, sj)])                       # 초기화
        visited = [[0] * N for _ in range(N)]
        visited[si][sj] = 1
    else:                                       # 없다면 이동
        q = deque(nlst)


print(ans)


