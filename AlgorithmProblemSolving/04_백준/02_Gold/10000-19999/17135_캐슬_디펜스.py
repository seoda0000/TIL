from collections import deque
import sys

input = sys.stdin.readline


def pick(nth, start):
    if nth == 3:
        simulate()
        return

    for m in range(start, M):
        archer_idx[nth] = m
        pick(nth + 1, m + 1)

    return


def simulate():  # 게임 시뮬레이션
    global ans

    narr = [row[:] for row in arr]
    e_cnt = enemy_cnt  # 남은 적 수
    kill_cnt = 0  # 죽인 적 수

    while e_cnt:  # 적이 남아있으면 진행

        kill_set = set()  # 죽일 적
        for cj in archer_idx:  # 궁수에게 가장 가깝고, 가장 왼쪽인 적 찾기
            ei, ej = find_close_enemy(cj, narr)
            if ei >= 0:
                kill_set.add((ei, ej))

        kill_cnt += len(kill_set)
        e_cnt -= len(kill_set)
        for ki, kj in kill_set:
            narr[ki][kj] = 0

        last = narr.pop()  # 적 이동
        e_cnt -= last.count(1)  # 놓친 적

    ans = max(ans, kill_cnt)

    return


def find_close_enemy(sj, arr):  # 궁수가 서 있는 열, 적 목록
    N, M = len(arr), len(arr[0])
    q = deque([(N, sj)])
    v = [[0] * M for _ in range(N + 1)]
    v[N][sj] = 1
    enemy_lst = []

    k = -1  # 궁수와의 거리
    while True:
        k += 1
        if k > D:  # 공격 범위 초과: 종료
            break
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()
            if (0 <= ci < N and 0 <= cj < M) and arr[ci][cj]:
                enemy_lst.append((ci, cj))

            for d in range(3):
                ni, nj = ci + di[d], cj + dj[d]
                if not (0 <= ni < N and 0 <= nj < M): continue
                if v[ni][nj]: continue
                v[ni][nj] = 1
                q.append((ni, nj))

        if enemy_lst:  # 최단거리 적 발견 시 탐색 종료
            break

    if enemy_lst:
        enemy_lst.sort(key=lambda x: x[1])
        return enemy_lst[0]  # 가장 왼쪽 적
    return -1, -1  # 적 발견 실패


di = [0, 0, -1]
dj = [1, -1, 0]
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
enemy_cnt = 0
for a in arr:
    enemy_cnt += sum(a)

archer_idx = [0] * 3
ans = 0
pick(0, 0)  # 궁수 배치하는 모든 경우의 수 구하기

print(ans)
