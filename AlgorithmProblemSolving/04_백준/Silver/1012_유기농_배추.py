"""
https://www.acmicpc.net/problem/1012

백준 실버2 1012 유기농배추

차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
"""

import sys

sys.setrecursionlimit(10 * 6)
input = sys.stdin.readline

alst = [1, -1, 0, 0]
blst = [0, 0, 1, -1]


def check(i, j):
    isCheck[i][j] = 1

    for x in range(4):
        if 0 <= i + alst[x] < N and 0 <= j + blst[x] < M and isCheck[i + alst[x]][j + blst[x]] == 0 and \
                ground[i + alst[x]][j + blst[x]]:
            check(i + alst[x], j + blst[x])


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    isCheck = [[0] * M for _ in range(N)]
    ans = 0
    for _ in range(K):
        a, b = map(int, input().split())
        ground[b][a] = 1
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and isCheck[i][j] == 0:
                ans += 1
                check(i, j)
            isCheck[i][j] = 1
    print(ans)

"""
이건 dfs가 아니다 (아예 다음 간선으로 가야함.) 이렇게  짜지 말자
"""


def dfs(si, sj):
    v[si][sj] = 1
    stk = [(si, sj)]

    while stk:
        ci, cj = stk.pop()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                v[ni][nj] = 1
                stk.append((ni, nj))
    return


T = int(input())
for t in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    ans = 0

    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and v[i][j] == 0:
                dfs(i, j)
                ans += 1
    print(ans)
