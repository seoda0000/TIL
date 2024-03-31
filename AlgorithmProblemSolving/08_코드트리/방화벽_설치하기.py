from collections import deque


def solve(arr):
    q = deque(fire_lst)
    v = [[0] * M for _ in range(N)]
    cnt = 0
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if arr[ni][nj]: continue

            cnt += 1
            v[ni][nj] = 1
            q.append((ni, nj))

    return bN - cnt


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = []
blank_lst = []
fire_lst = []
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(M):
        if ipt[j] == 0:
            blank_lst.append((i, j))
        elif ipt[j] == 2:
            fire_lst.append((i, j))
    arr.append(ipt)
bN = len(blank_lst)

ans = 0
for a in range(bN - 2):
    ai, aj = blank_lst[a]
    arr[ai][aj] = 1
    for b in range(a + 1, bN - 1):
        bi, bj = blank_lst[b]
        arr[bi][bj] = 1
        for c in range(b + 1, bN):
            ci, cj = blank_lst[c]
            arr[ci][cj] = 1

            ans = max(ans, solve(arr))

            arr[ci][cj] = 0
        arr[bi][bj] = 0
    arr[ai][aj] = 0
print(ans - 3)
