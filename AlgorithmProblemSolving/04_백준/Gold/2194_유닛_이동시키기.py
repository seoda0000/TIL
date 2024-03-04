from collections import deque


def go(si, sj):
    v = [[0] * M for _ in range(N)]
    q = deque([(si, sj)])
    k = 0
    v[si][sj] = 1

    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj = q.popleft()
            if ci == ei - 1 and cj == ej - 1:
                return k - 1
            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                can_move = True

                if d == 0:  # 오
                    if not (0 <= cj + B < M):
                        can_move = False
                    else:
                        for i in range(ci, ci + A):
                            if arr[i][cj + B]:
                                can_move = False
                                break

                elif d == 1:  # 왼
                    if not (0 <= cj - 1 < M):
                        can_move = False
                    else:
                        for i in range(ci, ci + A):
                            if arr[i][cj - 1]:
                                can_move = False
                                break
                elif d == 2:  # 하
                    if not (0 <= ci + A < N):
                        can_move = False
                    else:
                        for j in range(ci, ci + B):
                            if arr[ci + A][j]:
                                can_move = False
                                break
                else:  # 상
                    if not (0 <= ci - 1 < N):
                        can_move = False
                    else:
                        for j in range(cj, cj + B):
                            if arr[ci - 1][j]:
                                can_move = False
                                break

                if not can_move: continue
                if v[ni][nj]: continue
                v[ni][nj] = 1
                q.append((ni, nj))

    return -1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M, A, B, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    ki, kj = map(int, input().split())
    arr[ki - 1][kj - 1] = 1
si, sj = map(int, input().split())
ei, ej = map(int, input().split())

print(go(si - 1, sj - 1))
