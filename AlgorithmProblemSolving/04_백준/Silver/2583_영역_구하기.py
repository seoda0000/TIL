"""
https://www.acmicpc.net/problem/2583
백준 실버1 2583 영역 구하기
"""

M, N, K = map(int, input().split())
arr = [[0] * (M) for _ in range(N)]
for k in range(K):
    ax, ay, bx, by = map(int, input().split())
    for x in range(ax, bx):
        for y in range(ay, by):
            arr[x][y] = 1

v = [[0] * (M) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = []

for i in range(N):
    for j in range(M):

        if v[i][j] == 1:
            continue

        v[i][j] = 1

        if arr[i][j] == 1:
            continue

        q = [(i, j)]
        size = 1

        while q:
            a, b = q.pop(0)

            for n in range(4):
                na, nb = a + dx[n], b + dy[n]

                if 0 <= na < N and 0 <= nb < M and v[na][nb] == 0:
                    v[na][nb] = 1
                    if arr[na][nb] == 0:
                        q.append((na, nb))
                        size += 1
        ans.append(size)
ans.sort()

print(len(ans))
print(*ans)