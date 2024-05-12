"""
https://www.acmicpc.net/problem/17472
백준 골드1 17472 다리만들기2
"""
from collections import defaultdict

def checkLand(i, j, x):
    landMap[i][j] = x # 섬 넘버링 표시
    isChecked[i][j] = 1 # 섬 방문 여부 표시

    for a in range(4): # 4방향 탐색하여 같은 섬 표시
        ni = i + di[a]
        nj = j + dj[a]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and isChecked[ni][nj] == 0:
            checkLand(ni, nj, x)

def findBridge(i, j, x):
    for a in range(4): # 4방향 탐색
        ni = i + di[a]
        nj = j + dj[a]
        bridgeLength = 1 # 최소 다리 길이
        if 0 <= ni < N and 0 <= nj < M:
            if landMap[ni][nj] == x: # 같은 섬일 경우 pass
                continue

            if landMap[ni][nj] > 0: # 붙어 있는 섬일 경우 바로 추가 (길이: 0)
                bridges.add((x, landMap[ni][nj], 0))

            while 0<=ni<N and 0<=nj<M and landMap[ni][nj] == 0: # 바다일 경우 섬이 나올 때까지 같은 방향 탐색
                ni += di[a]
                nj += dj[a]
                bridgeLength += 1
            if 0 <= ni < N and 0 <= nj < M and landMap[ni][nj] > 0 and bridgeLength-1 != 1: # 다른 섬 발견 시 다리 체크 (길이가 1이 아닐 경우)
                bridges.add((x, landMap[ni][nj], bridgeLength-1))


def checkParent(land, parent): # 연결된 섬들의 최소값 갱신
    pastParent = parents[land]
    newParent = parents[parent]
    for p in range(len(parents)):
        if parents[p] == pastParent:
            parents[p] = newParent




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
isChecked = [[0] * M for _ in range(N)]
landMap = [[0] * M for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
bridges = set()

num = 1 # 섬 넘버링
for n in range(N):
    for m in range(M):
        if arr[n][m] > 0 and isChecked[n][m] == 0:
            checkLand(n, m, num) # 지도에 섬을 숫자로 표시
            num += 1

for n in range(N):
    for m in range(M):
        if landMap[n][m] > 0:
            findBridge(n, m, landMap[n][m]) # 섬 사이 다리 찾기

bridges = list(bridges)
bridges.sort(key=lambda x:x[2]) # 섬의 길이 순으로 오름차순 정렬
parents = [i for i in range(num)] # 연결된 섬들의 최소값
ans = 0

for b in bridges:
    land1, land2, length = b
    if (parents[max(land1, land2)] != parents[min(land1, land2)]): # 만약 두 섬이 연결되지 않았으면 정답에 포함
        ans += length
        checkParent(max(land1, land2), min(land1, land2)) # 두 섬의 연결 표시

parents = set(parents)
if len(parents) > 2: # 연결되지 않은 섬이 있는 경우
    print(-1)
else: # 모든 섬이 연결된 경우
    print(ans)
