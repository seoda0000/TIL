"""
https://www.acmicpc.net/problem/18428
백준 골드5 18428 감시 피하기
"""


def catchByTeacher(si, sj):
    for d in range(4):
        h = 1
        while h < N:
            ni, nj = si + di[d] * h, sj + dj[d] * h
            if not (0 <= ni < N and 0 <= nj < N): break
            if arr[ni][nj] == 'S':
                return True
            elif arr[ni][nj] == 'O':
                break
            else:
                h += 1
    return False


def buildWall(nth):
    if nth == 3:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'T' and catchByTeacher(i, j):
                    return False
        else:
            return True

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 'X': continue
            arr[i][j] = 'O'
            if buildWall(nth + 1):
                return True
            else:
                arr[i][j] = 'X'
    return False


N = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
arr = [list(input().split()) for _ in range(N)]
if buildWall(0):
    print("YES")

else:
    print("NO")
