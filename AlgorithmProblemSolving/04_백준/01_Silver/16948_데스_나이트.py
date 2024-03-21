from collections import deque


def move_knight(si, sj):
    arr[si][sj] = 1
    q = deque([(si, sj)])

    while q:

        ci, cj = q.popleft()

        if ci == ei and cj == ej:
            return arr[ci][cj] - 1

        for d in range(6):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if arr[ni][nj]: continue

            arr[ni][nj] = arr[ci][cj] + 1
            q.append((ni, nj))

    return -1


di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]

N = int(input())
si, sj, ei, ej = map(int, input().split())
arr = [[0] * N for _ in range(N)]

ans = move_knight(si, sj)
print(ans)
