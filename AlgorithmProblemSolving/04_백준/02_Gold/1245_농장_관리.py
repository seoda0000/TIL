"""
https://www.acmicpc.net/problem/1245
백준 골드5 1245 농장 관리

농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다.
이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.

산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다.
(여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.)
또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.

문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.
"""
from collections import deque


# 봉우리가 될 가능성이 없는 곳 체크 & 더 높은 봉우리 리스트 return
def colorAndSearch(si, sj):
    h = arr[si][sj]
    v[si][sj] = 1
    q = deque([(si, sj)])
    nxtLst = []
    while q:
        ci, cj = q.popleft()
        for d in range(8):  # (si, sj)와 인접한 같은 높이 & 낮은 높이를 모두 v에 체크
            ni, nj = ci + di[d], cj + dj[d]
            if 0 > ni or 0 > nj or ni >= N or nj >= M or v[ni][nj]: continue
            if arr[ni][nj] > h:
                nxtLst.append((ni, nj))  # 더 높은 봉우리가 있다면 리스트에 넣는다.
            elif arr[ni][nj] == h:
                v[ni][nj] = 1
                q.append((ni, nj))
            elif arr[ni][nj] < h:
                colorAndSearch(ni, nj)  # 지금보다 더 낮은 곳이면 봉우리가 아니다
    return nxtLst


def findMountain(si, sj):  # 봉우리 찾기
    global ans

    nxtLst = colorAndSearch(si, sj)  # 더 높은 인접 지역이 있는지 확인

    if nxtLst:  # 더 높은 인접 지역 탐색
        for nxt in nxtLst:
            ni, nj = nxt
            if v[ni][nj]: continue
            findMountain(ni, nj)
    else:  # 더 높은 인접 지역이 없다면 봉우리 count
        ans += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]
ans = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0 and arr[i][j] > 0:
            findMountain(i, j)

print(ans)
