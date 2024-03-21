def choose_K(nth, sm, bi, bj):
    global ans

    if nth == K:
        ans = max(ans, sm)
        return

    for j in range(bj + 2, M):
        if not is_able(bi, j): continue  # 선택할 수 있는지 확인

        v[bi][j] = 1
        choose_K(nth + 1, sm + arr[bi][j], bi, j)
        v[bi][j] = 0

    for i in range(bi + 1, N):
        for j in range(M):
            if not is_able(i, j): continue  # 선택할 수 있는지 확인

            v[i][j] = 1
            choose_K(nth + 1, sm + arr[i][j], i, j)
            v[i][j] = 0

    return


def is_able(si, sj):
    for d in range(2):
        ni, nj = si + di[d], sj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M): continue
        if v[ni][nj]: return False
    return True


di = [-1, 0]
dj = [0, -1]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = -10_000 * N * M

choose_K(0, 0, 0, -2)
print(ans)
