from collections import deque

di = [0, 1]
dj = [1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
si = sj = 0
v = [[0] * N for _ in range(N)]
q = deque([(si, sj)])
v[si][sj] = 1
ans = 'Hing'
while q:
    ci, cj = q.popleft()
    if ci == N - 1 and cj == N - 1:
        ans = 'HaruHaru'
        break

    k = arr[ci][cj]

    for d in range(2):
        ni, nj = ci + di[d] * k, cj + dj[d] * k
        if not (0 <= ni < N and 0 <= nj < N): continue
        if v[ni][nj]: continue

        v[ni][nj] = 1
        q.append((ni, nj))

print(ans)
