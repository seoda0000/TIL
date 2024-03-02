from collections import deque


def run(arr):
    fq = deque()
    pq = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == fire:
                fq.append((i, j))
            elif arr[i][j] == sanguen:
                pq.append((i, j))
                arr[i][j] = 0
    t = -1
    while fq or pq:
        t += 1
        nfq = len(fq)

        for _ in range(nfq):
            ci, cj = fq.popleft()

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if not (0 <= ni < N and 0 <= nj < M): continue
                if arr[ni][nj] == wall or arr[ni][nj] == fire: continue
                arr[ni][nj] = fire
                fq.append((ni, nj))

        npq = len(pq)

        for _ in range(npq):
            ci, cj = pq.popleft()

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if not (0 <= ni < N and 0 <= nj < M): return t + 1
                if arr[ni][nj] != blank: continue
                arr[ni][nj] = ':'  # 방문 표시
                pq.append((ni, nj))

    return -1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
T = int(input())
sanguen, fire, wall, blank = '@', '*', '#', '.'
for _ in range(T):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = run(arr)
    if ans < 0:
        print('IMPOSSIBLE')
    else:
        print(ans)
