from collections import deque


def find_cool_place(si, sj):
    cnt = 0

    q = deque()
    if v[si][sj] == 0:
        cnt += 1
        v[si][sj] = 1
        for d in range(4):
            dir_v[si][sj] += 1 << d
            q.append((si, sj, d))
    else:
        for d in range(4):
            if dir_v[si][sj] & 1 << d:
                continue
            dir_v[si][sj] += 1 << d
            q.append((si, sj, d))

    while q:
        ci, cj, cd = q.popleft()

        ni, nj = ci + di[cd], cj + dj[cd]

        if not (0 <= ni < N and 0 <= nj < M): continue
        if v[ni][nj]:
            if dir_v[ni][nj] & 1 << cd:
                continue
            else:
                dir_v[ni][nj] += 1 << cd
        else:
            cnt += 1
            v[ni][nj] = 1
            dir_v[ni][nj] += 1 << cd

        if arr[ni][nj] == 1:  # 1: 세로 물건
            if cd % 2:  # 동서
                cd = (cd + 2) % 4  # 반향 반대로

        elif arr[ni][nj] == 2:  # 2: 가로 물건
            if cd % 2 == 0:  # 남북
                cd = (cd + 2) % 4  # 반향 반대로

        elif arr[ni][nj] == 3:  # 3: 우상 대각선 물건
            # 위 0 -> 오른쪽 1
            # 아래 2 -> 왼쪽 3
            # 오른 1 -> 위쪽 0
            # 왼 3 -> 아래쪽 2
            if cd % 2:
                cd = (cd - 1) % 4
            else:
                cd = (cd + 1) % 4
        elif arr[ni][nj] == 4:  # 4: 우하 대각선 물건
            if cd % 2:
                cd = (cd + 1) % 4
            else:
                cd = (cd - 1) % 4

        q.append((ni, nj, cd))

    return cnt


di = [-1, 0, 1, 0]  # 위, 오른쪽, 아래, 왼쪽
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 9: 에어컨
# 0: 빈 공간
conditioners = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            conditioners.append((i, j))

v = [[0] * M for _ in range(N)]
dir_v = [[0] * M for _ in range(N)]
ans = 0
for si, sj in conditioners:
    ans += find_cool_place(si, sj)

print(ans)
