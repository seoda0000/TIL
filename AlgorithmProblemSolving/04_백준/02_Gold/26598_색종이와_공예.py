from collections import deque


def check():  # 둘러싼 직사각형 면적과 실제 면적이 다르면 False return
    for i in range(N):
        for j in range(M):
            if v[i][j]: continue
            ei, ej, cnt = bfs(i, j)
            b = (ei + 1 - i) * (ej + 1 - j)
            if b != cnt:
                return False
    return True


def bfs(si, sj):  # 방문 체크 + 오른쪽 끝 좌표, 면적 return
    alpha = arr[si][sj]
    v[si][sj] = 1
    q = deque([(si, sj)])
    ei, ej = si, sj
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] != alpha: continue
            if v[ni][nj]: continue

            cnt += 1
            v[ni][nj] = 1
            q.append((ni, nj))
            ei = max(ei, ni)
            ej = max(ej, nj)

    return ei, ej, cnt


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
v = [[0] * M for _ in range(N)]

if check():
    print('dd')
else:
    print('BaboBabo')
