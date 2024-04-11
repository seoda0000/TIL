'''
연구소2
https://www.acmicpc.net/problem/17141
백준 골드4 17141

인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
'''


from itertools import combinations
from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ableLst = []
answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            ableLst.append((i, j))
combiLst = list(combinations(ableLst, M))    # 처음 놓는 자리 조합

for combi in combiLst:     # 각 조합을 고려
    lab = deepcopy(arr)         # arr 카피본 생성 (딥카피 유의)
    q = deque([])               # q
    for c in combi:
        i, j = c
        q.append((i, j, 3))     # 시작 숫자 3
    while q:
        x, y, cnt = q.popleft()
        if lab[x][y] == 0 or lab[x][y] == 2:               # 만약 바이러스를 둘 수 있는 곳이면 시간 기록
            lab[x][y] = cnt

            for a, b in ((0, 1), (1, 0), (0, -1), (-1, 0)):    # 상하좌우 처리
                if 0<=x+a<N and 0<=y+b<N and (lab[x+a][y+b] == 0 or lab[x+a][y+b] == 2):
                    q.append((x+a, y+b, cnt+1))                # q에 enqueue

    mx = []
    for a in lab:
        if 0 in a:    # 0이면 실패
            break
        mx.append(max(a))
    else:             # 시작값을 빼서 저장한다
        ans = max(mx)-3

        answer.append(ans)

if answer:
    A = min(answer)
else:
    A = -1
print(A)