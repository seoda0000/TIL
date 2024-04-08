"""
실행시간: 381 -> 482
풀이시간: 33분 -> 36분
"""

"""
14:04 시작
14:10 구상 완료
14:27 구현 완료
14:38 디버깅 완료 (K 범위)
14:40 단계별 진행 확인

처음에 나무의 성장을 확인할 때 근처의 번식 가능한 칸의 수를 미리 세둬서 로직을 줄일 수 있었다.
구현이 모두 끝난 후에 tc가 통과되어도 각 단계가 그림과 같은지 일일이 확인했고, 이를 통해 오류(제초제 무시하고 번식하는 경우)를 잡을 수 있었다.
꼭 공개 tc와 아무리 사소한 것이라도 다른 건 없는지 단계뼐로 확인해보자.
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ei = [1, 1, -1, -1]
ej = [1, -1, 1, -1]
N, year_cnt, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 0 빈칸, -1 벽
time_arr = [[0] * N for _ in range(N)]
ans = 0

for _ in range(year_cnt):

    # 성장
    pass
    blank_cnt_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue
            cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue
                if arr[ni][nj] > 0:  # 나무가 있다
                    arr[i][j] += 1
                elif arr[ni][nj] == 0 and time_arr[ni][nj] == 0:  # 빈칸이 있다
                    cnt += 1
            blank_cnt_arr[i][j] = cnt

    # 번식
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue
            if blank_cnt_arr[i][j] == 0: continue
            tree = arr[i][j] // blank_cnt_arr[i][j]
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue
                if arr[ni][nj] != 0: continue
                if time_arr[ni][nj]: continue
                new_arr[ni][nj] += tree

    for i in range(N):
        for j in range(N):
            arr[i][j] += new_arr[i][j]

    # 제초제
    dead_cnt = xi = xj = -1
    for i in range(N):
        for j in range(N):
            # i, j에 제초제 뿌리기
            if arr[i][j] > 0:
                cnt = arr[i][j]

                for d in range(4):
                    for k in range(1, K + 1):
                        ni, nj = i + ei[d] * k, j + ej[d] * k
                        if OOB(ni, nj): break
                        if arr[ni][nj] <= 0: break
                        cnt += arr[ni][nj]

            else:
                cnt = 0

            if cnt > dead_cnt:
                dead_cnt, xi, xj = cnt, i, j

    ans += dead_cnt

    for i in range(N):
        for j in range(N):
            if time_arr[i][j]:
                time_arr[i][j] -= 1

    # xi, xj에 제초제 뿌리기
    time_arr[xi][xj] = C
    if arr[xi][xj] > 0: arr[xi][xj] = 0

    for d in range(4):
        for k in range(1, K + 1):
            ni, nj = xi + ei[d] * k, xj + ej[d] * k
            if OOB(ni, nj): break
            time_arr[ni][nj] = C
            if arr[ni][nj] <= 0:
                break
            else:
                arr[ni][nj] = 0
print(ans)

"""
3:10 구상 완료
3:31 1차 구현
3:43 점검 및 제출

단순한 문제라서 머리 굴리지 않고 단순하게 구현했다.
대각선 순회는 주말에 이영석 프로님과의 스터디에서 배운 아이디어를 활용했다. (가장 단순한 조회)
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
