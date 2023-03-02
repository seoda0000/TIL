"""
백준 골드5 17836
공주님을 구해라
https://www.acmicpc.net/problem/17836

용사는 마왕이 숨겨놓은 공주님을 구하기 위해 (N, M) 크기의 성 입구 (1,1)으로 들어왔다.
마왕은 용사가 공주를 찾지 못하도록 성의 여러 군데 마법 벽을 세워놓았다.
용사는 현재의 가지고 있는 무기로는 마법 벽을 통과할 수 없으며, 마법 벽을 피해 (N, M) 위치에 있는 공주님을 구출해야만 한다.

마왕은 용사를 괴롭히기 위해 공주에게 저주를 걸었다. 저주에 걸린 공주는 T시간 이내로 용사를 만나지 못한다면 영원히 돌로 변하게 된다.
공주님을 구출하고 프러포즈 하고 싶은 용사는 반드시 T시간 내에 공주님이 있는 곳에 도달해야 한다. 용사는 한 칸을 이동하는 데 한 시간이 걸린다.
공주님이 있는 곳에 정확히 T시간만에 도달한 경우에도 구출할 수 있다. 용사는 상하좌우로 이동할 수 있다.



성에는 이전 용사가 사용하던 전설의 명검 "그람"이 숨겨져 있다.
용사가 그람을 구하면 마법의 벽이 있는 칸일지라도, 단숨에 벽을 부수고 그 공간으로 갈 수 있다.
"그람"은 성의 어딘가에 반드시 한 개 존재하고, 용사는 그람이 있는 곳에 도착하면 바로 사용할 수 있다. 그람이 부술 수 있는 벽의 개수는 제한이 없다.

우리 모두 용사가 공주님을 안전하게 구출 할 수 있는지, 있다면 얼마나 빨리 구할 수 있는지 알아보자.
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def f(i, j, t):
    global mn
    if mn <= t:
        return

    if i == N-1 and j == M-1:
        if t < mn:
            mn = t
        return


    for a, b in ab:
        ni, nj = i+a, j+b
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] > t+1:
            if arr[ni][nj] == 0:
                visited[ni][nj] = t+1
                f(ni, nj, t+1)
            elif arr[ni][nj] == 2:
                mn = min(mn, t+1 + abs(N-ni-1) + abs(M-nj-1))


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ab = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[M*N+1] * M for _ in range(N)]
mn = N * M + 1

visited[0][0] = 0
f(0, 0, 0)

if mn == N*M + 1 or mn > T:
    print("Fail")
else:
    print(mn)


