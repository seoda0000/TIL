"""
15:27 구상 시작
15:35 구현 시작
"""


def move_clouds(clouds, d, s):  # s 만큼 d 방향으로 구름 이동
    moved_clouds = []

    for ci, cj in clouds:
        ni, nj = (ci + di[d] * s) % N, (cj + dj[d] * s) % N
        moved_clouds.append((ni, nj))

    return moved_clouds


def plus_water(ci, cj):  # 대각선 물 개수 만큼 증가
    cnt = 0

    for dx in [2, 4, 6, 8]:  # 대각선
        ni, nj = ci + di[dx], cj + dj[dx]

        if not (0 <= ni < N and 0 <= nj < N): continue
        if arr[ni][nj]:
            cnt += 1

    arr[ci][cj] += cnt

    return


di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(M)]
clouds = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]
for od, os in orders:

    clouds = move_clouds(clouds, od, os)  # 구름 이동

    for ci, cj in clouds:  # 구름 위치 물 양 1 증가
        arr[ci][cj] += 1

    for ci, cj in clouds:  # 대각선 물 개수 만큼 증가
        plus_water(ci, cj)

    # 새로운 구름 생성
    new_clouds = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and ((i, j) not in clouds):
                arr[i][j] -= 2
                new_clouds.append((i, j))

    clouds = new_clouds

ans = 0
for a in arr:
    ans += sum(a)

print(ans)
