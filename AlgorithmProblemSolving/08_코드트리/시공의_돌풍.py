"""
4:02 시작
4:08 구상 완료
4:18~4:26 휴식
4:34 코드 점검 및 제출
"""
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if arr[i][0] == -1:
        wi_tup = (i, i + 1)
        arr[i][0] = 0
        arr[i + 1][0] = 0
        break

for _ in range(T):
    # 먼지 확산
    nxt_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            nxt_lst = []
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if not (0 <= ni < N and 0 <= nj < M): continue
                if ni in wi_tup and nj == 0: continue
                nxt_lst.append((ni, nj))
            nxt_dust = arr[i][j] // 5

            for ni, nj in nxt_lst:
                nxt_arr[ni][nj] += nxt_dust
            nxt_arr[i][j] -= nxt_dust * len(nxt_lst)

    for i in range(N):
        for j in range(M):
            arr[i][j] += nxt_arr[i][j]

    # 위쪽 돌풍
    ci, cj = wi_tup[0] - 1, 0
    d = 2

    while True:
        if ci == wi_tup[0] and cj == 0: break  # 돌풍 자리

        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni <= wi_tup[0] and 0 <= nj < M):
            d = (d + 1) % 4
            ni, nj = ci + di[d], cj + dj[d]
        arr[ci][cj] = arr[ni][nj]
        ci, cj = ni, nj

    # 아래쪽 돌풍
    ci, cj = wi_tup[1] + 1, 0
    d = 0

    while True:
        if ci == wi_tup[1] and cj == 0: break  # 돌풍 자리

        ni, nj = ci + di[d], cj + dj[d]
        if not (wi_tup[1] <= ni < N and 0 <= nj < M):
            d = (d - 1) % 4
            ni, nj = ci + di[d], cj + dj[d]
        arr[ci][cj] = arr[ni][nj]
        ci, cj = ni, nj

print(sum([sum(a) for a in arr]))
