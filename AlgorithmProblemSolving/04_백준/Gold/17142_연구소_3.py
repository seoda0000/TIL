'''
연구소 3
https://www.acmicpc.net/problem/17142
백준 골드4

인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다.
가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다.
연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
'''


import sys
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def f(com):  # 조합별 소모시간 구하는 함수
    arr = [item[:] for item in firstarr]
    q = deque([])
    for c in com:
        ci, cj = c
        q.append((ci, cj))
        arr[ci][cj] = 3  # 시작 바이러스 3으로 변경
    mxt = 3
    while q:
        vi, vj = q.popleft()

        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 네 방향 탐색
            ni = vi + a
            nj = vj + b
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:  # 빈칸이면 바이러스 퍼뜨리기
                    arr[ni][nj] = arr[vi][vj] + 1
                    q.append((ni, nj))
                    if arr[ni][nj] > mxt:  # 진행 시간 갱신
                        mxt = arr[ni][nj]
                elif arr[ni][nj] == 2:     # 바이러스가 있으면 활성화
                    arr[ni][nj] = arr[vi][vj] + 1
                    q.append((ni, nj))     # 이미 바이러스가 있으므로 진행 시간 갱신 x
    for a in arr:
        if 0 in a:
            return
    else:
        return mxt-3


N, M = map(int, input().split())
firstarr = [list(map(int, input().split())) for _ in range(N)]
virus = []
full = 0               # 이미 채워져있는지 확인하는 flag
for i in range(N):
    if 0 not in firstarr[i]:
        full += 1
    for j in range(N):
        if firstarr[i][j] == 2:
            virus.append((i, j))
combi = list(combinations(virus, M))    # 조합 구하기
if full == N:           # N개 행이 모두 채워져 있을 경우 0 return 후 종료
    answer = 0
else:
    answer = 2500       # 범위 내 최대시간
    for com in combi:
        if f(com) and answer > f(com):  # 최소시간 갱신
            answer = f(com)

    if answer == 2500:  # 갱신되지 않았다면 -1
        answer = -1
print(answer)