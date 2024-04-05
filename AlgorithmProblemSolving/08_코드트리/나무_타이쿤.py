"""
2:04 시작
2:11 구상 완료
2:19 구현 완료
2:22 디버깅 완료 (배열 갱신 까먹음)
"""
di = [0, 0, -1, -1, -1, 0, 1, 1, 1] # 코드트리
dj = [0, 1, 1, 0, -1, -1, -1, 0, 1]
# di = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # 백준
# dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
N, years = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
nut_lst = [(N - 1, 0), (N - 2, 0), (N - 1, 1), (N - 2, 1)]
for _ in range(years):
    cd, cp = map(int, input().split())
    moved_nut_lst = []
    for ci, cj in nut_lst:
        ni, nj = (ci + di[cd] * cp) % N, (cj + dj[cd] * cp) % N
        moved_nut_lst.append((ni, nj))
        arr[ni][nj] += 1
    nut_lst = moved_nut_lst

    for ci, cj in nut_lst:
        cnt = 0
        for d in [2, 4, 6, 8]:
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < N): continue
            if not arr[ni][nj]: continue
            cnt += 1
        arr[ci][cj] += cnt

    nxt_nut_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] < 2: continue
            if (i, j) in nut_lst: continue
            nxt_nut_lst.append((i, j))
            arr[i][j] -= 2
    nut_lst = nxt_nut_lst

print(sum([sum(a) for a in arr]))
