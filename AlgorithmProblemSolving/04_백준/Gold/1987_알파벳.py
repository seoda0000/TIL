"""
https://www.acmicpc.net/problem/1987
백준 골드4 1987 알파벳
"""

import sys

input = sys.stdin.readline


def getIdx(a: str):
    return ord(a) - 65  # ord('A')


def findRoute(i, j, v, cnt):
    global ans

    if ans == 26:
        return

    ans = max(ans, cnt)

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if not (0 <= ni < N and 0 <= nj < M): continue
        nAlpha = arr[ni][nj]
        if v & 1 << nAlpha: continue

        findRoute(ni, nj, v | 1 << nAlpha, cnt + 1)

    return


N, M = map(int, input().split())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
arr = [list(map(getIdx, input())) for _ in range(N)]
ans = 0

findRoute(0, 0, 1 << arr[0][0], 1)

print(ans)

"""
큐 이용
"""

import sys

input = sys.stdin.readline


def getIdx(a: str):
    return ord(a) - 65


N, M = map(int, input().split())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
arr = [list(map(getIdx, input())) for _ in range(N)]
ans = 0

stk = [(0, 0, 1 << arr[0][0], 1)]

while ans != 26 and stk:
    ci, cj, cv, cCnt = stk.pop()
    ans = max(cCnt, ans)
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M): continue
        nAlpha = arr[ni][nj]
        if cv & 1 << nAlpha: continue
        stk.append((ni, nj, cv | 1 << arr[ni][nj], cCnt + 1))

print(ans)
