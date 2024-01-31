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

"""
이건 dfs가 아니다. 이렇게 풀면 안됨
"""
def dfs(ti, tj):  # 연결된 영역 구하고 넓이를 return
    v[ti][tj] = 1
    b = 1  # 넓이
    stk = [(ti, tj)]

    while stk:
        ci, cj = stk.pop()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and v[ni][nj] == 0:
                v[ni][nj] = 1
                stk.append((ni, nj))
                b += 1
    return b


M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0

for _ in range(K):  # 영역 그리기
    si, sj, ei, ej = map(int, input().split())

    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = 1

blst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and v[i][j] == 0:  # 0인 새로운 영역 발견
            blst.append(dfs(i, j))
            ans += 1
blst.sort()
print(ans)
print(*blst)
