from collections import deque


def move_tree(v_row, v_col):
    k = 1
    while q:
        k += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj, cs = q.popleft()

            if ci == ei and cj == ej and cs == es:
                return k - 2
            if cs:  # 현재 세로
                for di, dj in [(-2, 0), (2, 0)]:  # 위아래
                    ni, nj = ci + di, cj + dj
                    if not (0 <= ni < N and 0 <= nj < N): continue
                    if arr[ni][nj] == '1': continue
                    # 다음 좌표
                    ni, nj = ci + di // 2, cj + dj // 2
                    if v_col[ni][nj]: continue
                    v_col[ni][nj] = k
                    q.append((ni, nj, cs))

                can_move_cnt = 0
                for dj in [1, -1]:  # 왼오
                    can_move = True
                    for di in [-1, 1, 0]:
                        ni, nj = ci + di, cj + dj
                        if not (0 <= ni < N and 0 <= nj < N):
                            can_move = False
                            break
                        if arr[ni][nj] == '1':
                            can_move = False
                            break
                    if can_move:
                        can_move_cnt += 1
                    else:
                        continue
                    if v_col[ni][nj]: continue
                    v_col[ni][nj] = k
                    q.append((ni, nj, cs))

                if can_move_cnt < 2: continue  # 회전
                if v_row[ci][cj]: continue
                v_row[ci][cj] = k
                q.append((ci, cj, cs ^ 1))

            else:  # 현재 가로
                for dj, di in [(-2, 0), (2, 0)]:  # 왼오
                    ni, nj = ci + di, cj + dj
                    if not (0 <= ni < N and 0 <= nj < N): continue
                    if arr[ni][nj] == '1': continue

                    # 다음 좌표
                    ni, nj = ci + di // 2, cj + dj // 2
                    if v_row[ni][nj]: continue
                    v_row[ni][nj] = k
                    q.append((ni, nj, cs))

                can_move_cnt = 0
                for di in [1, -1]:  # 위아래
                    can_move = True
                    for dj in [-1, 1, 0]:
                        ni, nj = ci + di, cj + dj
                        if not (0 <= ni < N and 0 <= nj < N):
                            can_move = False
                            break
                        if arr[ni][nj] == '1':
                            can_move = False
                            break
                    if can_move:
                        can_move_cnt += 1
                    else:
                        continue
                    if v_row[ni][nj]: continue
                    v_row[ni][nj] = k
                    q.append((ni, nj, cs))

                if can_move_cnt < 2: continue  # 회전
                if v_col[ci][cj]: continue
                v_col[ci][cj] = k
                q.append((ci, cj, cs ^ 1))
    return 0


N = int(input())
arr = [input() for _ in range(N)]

fbi = fbj = fei = fej = 0  # 첫번째 B, E 좌표
bi = bj = ei = ej = 0  # 가운데 B, E 좌표
cnt_b = cnt_e = 0

for i in range(N):  # 초기 B, E 위치 확인
    for j in range(N):
        if arr[i][j] == 'B':
            if cnt_b == 0:
                fbi, fbj = i, j
            elif cnt_b == 1:
                bi, bj = i, j
            cnt_b += 1
        elif arr[i][j] == 'E':
            if cnt_e == 0:
                fei, fej = i, j
            elif cnt_e == 1:
                ei, ej = i, j
            cnt_e += 1

bs = 0 if fbi == bi else 1  # 초기 B, E 상태 (0: 가로, 1: 세로)
es = 0 if fei == ei else 1

v_row = [[0] * N for _ in range(N)]  # 가로 v 체크
v_col = [[0] * N for _ in range(N)]  # 세로 v 체크

q = deque([(bi, bj, bs)])
if bs:
    v_col[bi][bj] = 1
else:
    v_row[bi][bj] = 1

ans = move_tree(v_row, v_col)

print(ans)
