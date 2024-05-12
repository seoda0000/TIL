from collections import deque


def check_outer_air():
    for si, sj in qa:
        arr[si][sj] = 2

    while qa:
        ci, cj = qa.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] > 0: continue
            arr[ni][nj] = 2
            qa.append((ni, nj))
    return


def melt_cheese():
    Nq = len(qc)

    for _ in range(Nq):
        ci, cj = qc.popleft()
        melt = False
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == 2:
                melt = True
                break
        if melt:
            qa.append((ci, cj))
        else:
            qc.append((ci, cj))


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = sum([sum(a) for a in arr])
qc = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            qc.append((i, j))
qa = deque([(0, 0)])
ans = 0
t = 0
while qc:
    t += 1
    check_outer_air()
    ans = len(qc)
    melt_cheese()
print(t)
print(ans)
