from collections import deque


def move(xi, xj, yi, yj, d):
    ci, cj = xi, xj
    cnt = 0
    back = 0
    while True:
        cnt += 1
        ci, cj = ci + di[d], cj + dj[d]
        if arr[ci][cj] == '#':  # 벽
            back -= 1
            return cnt + back
        elif arr[ci][cj] == 'O':  # 출구
            return cnt
        elif ci == yi and cj == yj:
            back -= 1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            oi, oj = i, j

v = set()
v.add((ri, rj, bi, bj))
q = deque([(ri, rj, bi, bj, 0)])
ans = 11
while q:
    ri, rj, bi, bj, ck = q.popleft()
    if ck == 11:
        break
    if ri == oi and rj == oj:
        ans = ck
        break
    for d in range(4):
        rcnt = move(ri, rj, bi, bj, d)
        bcnt = move(bi, bj, ri, rj, d)
        nri, nrj = ri + di[d] * rcnt, rj + dj[d] * rcnt
        nbi, nbj = bi + di[d] * bcnt, bj + dj[d] * bcnt
        if nbi == oi and nbj == oj:  # 게임 오버
            continue
        else:
            if (nri, nrj, nbi, nbj) in v: continue
            v.add((nri, nrj, nbi, nbj))
            q.append((nri, nrj, nbi, nbj, ck + 1))
if ans == 11:
    ans = -1
print(ans)
