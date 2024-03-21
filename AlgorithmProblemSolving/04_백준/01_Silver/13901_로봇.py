N, M = map(int, input().split())
K = int(input())
things = [list(map(int, input().split())) for _ in range(K)]
si, sj = map(int, input().split())
dirs = list(map(int, input().split()))
di = []
dj = []

sdi = [0, -1, 1, 0, 0]
sdj = [0, 0, 0, -1, 1]
for dir in dirs:
    di.append(sdi[dir])
    dj.append(sdj[dir])
v = [[0] * M for _ in range(N)]
v[si][sj] = 1
d = 0
for ti, tj in things:
    v[ti][tj] = 1

cnt = 0
while cnt <= 3:
    ni, nj = si + di[d], sj + dj[d]

    if not (0 <= ni < N and 0 <= nj < M):
        d = (d + 1) % 4
        cnt += 1
        continue
    if v[ni][nj]:
        d = (d + 1) % 4
        cnt += 1
        continue

    v[ni][nj] = 1
    si, sj = ni, nj
    cnt = 0


print(si, sj)
