"""
실행시간: 508 -> 484
풀이시간: 23분 -> 18분

함수화를 하지 않은 것, 이동로직에 1 증가 로직을 합친 것을 제외하면 똑같이 풀었다.
문제를 이해하기 어려울 때는 함수화가 도움이 되었는데, 아는 문제다보니 굳이 함수화로 로직을 구현할 필요성을 느끼지 못하고 있다.
새로 푸는 문제도 틈틈이 풀어봐야겠다.
"""

"""
2:04 시작
2:11 구상 완료
2:19 구현 완료
2:22 디버깅 완료 (배열 갱신 까먹음)
"""
# di = [0, 0, -1, -1, -1, 0, 1, 1, 1] # 코드트리
# dj = [0, 1, 1, 0, -1, -1, -1, 0, 1]
di = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # 백준
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]
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

"""
15:27 구상 시작
15:35 구현 시작
15:50 구현 완료

순서 등이 헷갈릴 수 있는 단계는 함수로 빼서 구현했다.
조건을 꼼꼼하게 따지려고 노력했다.
처음으로 코드를 치기 전에 주석부터 달았는데, 구현 코드를 짤 때는 좋은 방법 같다.
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
