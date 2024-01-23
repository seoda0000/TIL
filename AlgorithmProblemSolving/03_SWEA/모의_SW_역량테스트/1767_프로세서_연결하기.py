def drawline(i, j, n, ary, before, after):
    cnt = 0
    ni, nj = i, j
    while True:
        ni += dx[n]
        nj += dy[n]
        if 0 <= ni < N and 0 <= nj < N and ary[ni][nj] == before:
            ary[ni][nj] = after
            cnt += 1
        else:
            break
    return cnt


def f(nth, corecnt, sm, arr):
    global ans_wire, ans_core
    if nth == Nc:
        if corecnt > ans_core:
            ans_wire = sm
            ans_core = corecnt
        elif corecnt == ans_core:
            ans_wire = min(ans_wire, sm)
        return
    i, j = where[nth]
    if i == 0 or i == N - 1 or j == 0 or j == N - 1:
        # 모서리라 자동 연결
        f(nth + 1, corecnt + 1, sm, arr)
    else:
        # 코어 4방향 탐색
        for n in range(4):
            ni, nj = i, j
            while True:
                ni += dx[n]
                nj += dy[n]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    # 모서리 도착
                    newsm = drawline(i, j, n, arr, 0, 2)
                    f(nth + 1, corecnt + 1, sm + newsm, arr)
                    drawline(i, j, n, arr, 2, 0)
                    break

                elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                    break

        # 연결하지 않고 다음으로
        f(nth + 1, corecnt, sm, arr)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans_wire = 0
    ans_core = 0

    where = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                where.append((i, j))
    Nc = len(where)
    f(0, 0, 0, arr)

    print(f'#{test_case} {ans_wire}')
