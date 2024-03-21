"""
https://www.acmicpc.net/problem/7562
백준 실버1 7562 나이트의 이동

체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다.
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

"""


def bfs(si, sj):
    q = [(si, sj, 0)]
    while True:

        ci, cj, h = q.pop(0)
        if ci == ei and cj == ej: return h
        for d in range(8):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 > ni or ni >= N or 0 > nj or nj >= N: continue
            if arr[ni][nj] == -1:
                arr[ni][nj] = h + 1
                q.append((ni, nj, h + 1))


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[-1] * N for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    di = [-2, -1, 1, 2, -2, -1, 1, 2]
    dj = [1, 2, 2, 1, -1, -2, -2, -1]

    print(bfs(si, sj))
