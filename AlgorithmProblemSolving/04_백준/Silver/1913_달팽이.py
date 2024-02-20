"""
https://www.acmicpc.net/problem/1913
백준 실버3 1913 달팽이
"""

"""
안에서 바깥으로
"""


def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == K:
                return i, j


N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
ci = cj = (N - 1) // 2
arr[ci][cj] = n = 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
d = 0
for i in range(1, N):
    for _ in range(2):
        for j in range(i):
            ci = ci + di[d]
            cj = cj + dj[d]
            n += 1
            arr[ci][cj] = n
        d = (d + 1) % 4
for i in range(N - 1):
    ci = ci + di[d]
    cj = cj + dj[d]
    n += 1
    arr[ci][cj] = n

for a in arr:
    print(*a)

ai, aj = find()
print(ai + 1, aj + 1)

"""
바깥에서 안으로
"""


def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == K:
                return i, j


N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
d = 0
ci, cj = 0, 0
n = N ** 2
arr[ci][cj] = n
while n > 1:
    ni, nj = ci + di[d], cj + dj[d]

    if not (0 <= ni < N and 0 <= nj < N) or (arr[ni][nj]):
        d = (d + 1) % 4
        continue
    n -= 1
    arr[ni][nj] = n
    ci, cj = ni, nj

for a in arr:
    print(*a)

ai, aj = find()
print(ai + 1, aj + 1)
