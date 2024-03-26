"""
3:10 구상 완료
3:31 1차 구현
3:43 점검 및 제출
"""

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

kill_di = [1, 1, -1, -1]
kill_dj = [-1, 1, -1, 1]
N, year_cnt, K, C = map(int, input().split())
tree_arr = [list(map(int, input().split())) for _ in range(N)]
poison_arr = [[0] * N for _ in range(N)]
kill_cnt = 0


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


for _ in range(year_cnt):

    # 나무 성장
    for i in range(N):
        for j in range(N):
            if tree_arr[i][j] <= 0: continue  # 벽이거나 나무 없는 경우

            near_cnt = 0  # 인접한 나무의 수

            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue
                if tree_arr[ni][nj] > 0:
                    near_cnt += 1

            tree_arr[i][j] += near_cnt

    # 나무 번식
    new_tree_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if tree_arr[i][j] <= 0: continue  # 벽이거나 나무 없는 경우

            new_lst = []  # 번식할 수 있는 칸의 좌표 목록

            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue  # 범위 밖
                if tree_arr[ni][nj]: continue  # 벽, 나무
                if poison_arr[ni][nj]: continue  # 제초제

                new_lst.append((ni, nj))

            for ni, nj in new_lst:
                new_tree_arr[ni][nj] += tree_arr[i][j] // len(new_lst)

    for i in range(N):
        for j in range(N):
            tree_arr[i][j] += new_tree_arr[i][j]

    # 제초제 뿌릴 위치 찾기
    xi = xj = x_cnt = -1  # 제초제 뿌릴 위치, 제초제로 죽일 수 있는 나무의 수

    for i in range(N):
        for j in range(N):
            if tree_arr[i][j] <= 0:  # 벽이거나 나무가 없는 경우
                cnt = 0
            else:  # 나무가 있는 경우
                cnt = tree_arr[i][j]  # i, j에서 죽일 수 있는 나무의 수

                for d in range(4):  # 대각선 K번 점검
                    for k in range(1, K + 1):
                        ni, nj = i + kill_di[d] * k, j + kill_dj[d] * k
                        if OOB(ni, nj): break
                        if tree_arr[ni][nj] <= 0: break  # 벽이거나 나무가 없는 경우

                        cnt += tree_arr[ni][nj]

            if cnt > x_cnt:  # 최대값 갱신
                xi, xj, x_cnt = i, j, cnt

    # 제초제 옅어지기
    for i in range(N):
        for j in range(N):
            if poison_arr[i][j]:
                poison_arr[i][j] -= 1

    # 제초제 뿌리기
    kill_cnt += x_cnt
    poison_arr[xi][xj] = C

    if tree_arr[xi][xj] > 0:  # 나무가 있는 경우만 죽인 후 확산
        tree_arr[xi][xj] = 0

        for d in range(4):  # 대각선 K번 점검
            for k in range(1, K + 1):
                ni, nj = xi + kill_di[d] * k, xj + kill_dj[d] * k
                if OOB(ni, nj): break

                poison_arr[ni][nj] = C  # 제초제 뿌리기
                if tree_arr[ni][nj] <= 0:  # 벽이거나 나무가 없는 경우: 중지
                    break
                else:  # 나무가 있는 경우: 죽인 후 확산
                    tree_arr[ni][nj] = 0

print(kill_cnt)
