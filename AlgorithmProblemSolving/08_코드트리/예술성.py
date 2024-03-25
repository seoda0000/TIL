"""
2:01 시작
2:07 구상 완료
"""
from collections import deque


def cal_artistic():
    global group_dic, v

    # id 부여하기
    group_dic = dict()
    v = [[0] * N for _ in range(N)]
    id = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                id += 1
                find_group(i, j, id)

    # 맞닿은 변의 수 구하기
    contact_arr = [[0] * (id + 1) for _ in range(id + 1)]  # group별 인접하는 면의 수 (행: 자신/ 열: 상대)
    for i in range(N):
        for j in range(N):
            group = v[i][j]
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue
                nxt = v[ni][nj]
                if nxt == group: continue
                contact_arr[group][nxt] += 1

    # 예술 점수 구하기
    score = 0
    for a in range(1, id):
        for b in range(a + 1, id + 1):
            if not contact_arr[a][b]: continue
            a_cnt, a_val = group_dic[a]
            b_cnt, b_val = group_dic[b]
            score += (a_cnt + b_cnt) * a_val * b_val * contact_arr[a][b]
    return score


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_group(si, sj, id):
    q = deque([(si, sj)])
    v[si][sj] = id
    val = arr[si][sj]
    cnt = 1
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj): continue
            if v[ni][nj]: continue
            if arr[ni][nj] != val: continue

            v[ni][nj] = id
            q.append((ni, nj))
            cnt += 1

    group_dic[id] = (cnt, val)
    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = cal_artistic()

for _ in range(3):
    # 그림 회전
    rclock_arr = list(map(list, zip(*arr)))[::-1]  # 반시계 전체 회전

    for x in range(2):
        for y in range(2):  # 4분할 시계 회전
            si, sj = x * (N // 2 + 1), y * (N // 2 + 1)
            target = []
            for i in range(si, si + N // 2):
                target.append(arr[i][sj:sj + N // 2])
            clock_target = list(map(list, zip(*target[::-1])))
            for i in range(N // 2):
                rclock_arr[si + i][sj:sj + N // 2] = clock_target[i]
    arr = rclock_arr
    ans += cal_artistic()

print(ans)
