"""
2:44 tc 5, 6 에러 발견
3:07 틀렸습니다
"""
import copy
import sys

input = sys.stdin.readline


def move_fish(ocean):
    new_ocean = [[list() for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for fd in ocean[i][j]:
                ni, nj, nfd = choose_fish_d(i, j, fd)
                new_ocean[ni][nj].append(nfd)

    return new_ocean


def choose_fish_d(i, j, first_fd):
    first_cnt = -1
    fd = first_fd
    while True:
        if fd == first_fd:
            first_cnt += 1
            if first_cnt == 1:
                break
        ni, nj = i + di[fd], j + dj[fd]

        if not (0 <= ni < N and 0 <= nj < N):
            fd = (fd - 1) % 8
            continue
        if smell_arr[ni][nj]:
            fd = (fd - 1) % 8
            continue
        if ni == si and nj == sj:
            fd = (fd - 1) % 8
            continue
        break

    if first_cnt == 1:
        return i, j, first_fd
    else:
        return ni, nj, fd


def go(ci, cj, ocean, fish, idx, lst):
    if idx >= 100:
        shark_choices.append((fish, idx))
        return

    for d in [2, 0, 6, 4]:
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < N and 0 <= nj < N): continue
        if ni * 4 + nj in lst:
            go(ni, nj, ocean, fish, idx * 10 + dir_to_idx[d], lst)
        else:
            go(ni, nj, ocean, fish + len(ocean[ni][nj]), idx * 10 + dir_to_idx[d], lst + [ni * 4 + nj])

    return


di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_to_idx = {2: 1, 0: 2, 6: 3, 4: 4}
idx_to_dir = {1: 2, 2: 0, 3: 6, 4: 4}
N = 4
ocean = [[list() for _ in range(N)] for _ in range(N)]
fish_cnt, S = map(int, input().split())
for _ in range(fish_cnt):
    x, y, d = map(int, input().split())
    ocean[x - 1][y - 1].append(d - 1)
si, sj = map(int, input().split())
si, sj = si - 1, sj - 1
smell_arr = [[0] * N for _ in range(N)]  # 냄새가 사라지기까지의 시간 배열
smell_time = 2  # 냄새 지속 시간
for _ in range(S):
    # 복제 마법
    copy_ocean = copy.deepcopy(ocean)

    # 물고기 이동
    ocean = move_fish(ocean)

    shark_choices = []  # (물고기 수, 경로의 index)

    # 냄새가 옅어진다
    for i in range(N):
        for j in range(N):
            if smell_arr[i][j]:
                smell_arr[i][j] -= 1

    # 상어 이동
    go(si, sj, ocean, 0, 0, [])
    shark_choices.sort(key=lambda x: (-x[0], x[1]))
    _, choice = shark_choices[0]

    for c in str(choice):
        d = idx_to_dir[int(c)]
        si, sj = si + di[d], sj + dj[d]
        if ocean[si][sj]:
            smell_arr[si][sj] = smell_time
        ocean[si][sj] = []
    pass

    # 물고기가 복제된다
    for i in range(N):
        for j in range(N):
            ocean[i][j].extend(copy_ocean[i][j])

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(ocean[i][j])

print(ans)
