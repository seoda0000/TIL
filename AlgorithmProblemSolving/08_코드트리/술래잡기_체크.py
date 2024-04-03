"""
3:18 시작
3:25 구상 완료
3:45 구현 완료
5:01 디버깅 완료
"""


def solve(arr, si, sj, sd, score):
    global ans


    ans = max(ans, score)  # 정답 갱신



    # 도둑말 이동
    for id in range(1, 17):
        move(arr, si, sj, id)


    # 술래말 이동
    ci, cj = si, sj
    while True:
        ci, cj = ci + di[sd], cj + dj[sd]

        if OOB(ci, cj): return
        if arr[ci][cj][0] == 0: continue  # 먹을 물고기 없음
        fid, fd = arr[ci][cj]  # 먹을 물고기
        arr[ci][cj] = (0, 0)  # 꿀꺽
        solve([a[:] for a in arr], ci, cj, fd, score + fid)
        arr[ci][cj] = (fid, fd)  # 꿀꺽 초기화

    return


def move(arr, si, sj, id):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] != id: continue  # 이동할 도둑말 찾기

            d = arr[i][j][1]
            for _ in range(8):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj) or (ni == si and nj == sj):  # 이동불가
                    d = (d + 1) % 8
                else:  # 이동 가능
                    arr[i][j] = (id, d)  # 방향 갱신
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                    return

            return


def OOB(i, j):
    return not (0 <= i < 4 and 0 <= j < 4)


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
arr = [[(0, 0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    ipt = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = (ipt[j * 2], ipt[j * 2 + 1] - 1)

# 0, 0 먹기
si, sj = 0, 0
sid, sd = arr[0][0]
arr[0][0] = (-1, -1)

ans = 0
solve(arr, si, sj, sd, sid)
print(ans)
