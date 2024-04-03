from collections import deque
import sys

sys.stdin = open("input.txt", "r")


def solve(nth, arr, remain_cnt):
    global ans

    ans = min(ans, remain_cnt)

    if nth == K:
        return

    if ans == 0:
        return

    for j in range(M):
        new_arr, new_cnt = shoot(arr, j)
        if new_cnt > 0:
            solve(nth + 1, new_arr, remain_cnt - new_cnt)

    return


def shoot(arr, tj):
    new_arr = [a[:] for a in arr]
    v = [[0] * M for _ in range(N)]
    q = deque()
    cnt = 0

    for i in range(N):
        if arr[i][tj]:  # 블럭 발견
            new_arr[i][tj] = 0
            v[i][tj] = 1
            q.append((i, tj))
            cnt += 1
            break

    while q:
        ci, cj = q.popleft()
        num = arr[ci][cj]
        for d in range(4):
            for x in range(1, num):
                ni, nj = ci + di[d] * x, cj + dj[d] * x
                if not (0 <= ni < N and 0 <= nj < M): break
                if v[ni][nj]: continue
                if not arr[ni][nj]: continue  # 공백

                v[ni][nj] = 1
                new_arr[ni][nj] = 0
                q.append((ni, nj))
                cnt += 1

    return gravity(new_arr), cnt


def gravity(arr):
    t_arr = list(map(list, zip(*arr)))
    new_arr = []
    for i in range(M):
        row = []
        for j in range(N):
            if t_arr[i][j]:
                row.append(t_arr[i][j])

        row = [0] * (N - len(row)) + row
        new_arr.append(row)

    return list(map(list, zip(*new_arr)))


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    block_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                block_cnt += 1
    ans = block_cnt
    solve(0, arr, block_cnt)
    print(f'#{test_case} {ans}')
