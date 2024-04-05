"""
실행시간: 626->690
풀이시간: 48분 -> 17분

백준대로 구현했다가 코드트리의 테스트케이스가 안 나와서 다시 풀었다. 문제 좀 제대로 읽자!

코드트리는 선택한 구역을 4등분하여 그 영역이 유지된 채 돌아야 한다. 체감상 2배 이상 어려웠다. 어떤 게 진짜 기출일지...
4등분된 영역을 한 요소라고 생각하고 zip으로 그냥 돌렸다.
시작점만 명확하면 구현할 수 있는 난이도다. zip을 쓰려면 행을 묶어서 넣어야 한다는 점만 잊지 말자!

"""

"""
10:35 시작
10:39 구상 완료
10:52 구현 완료
11:27 (코드트리 추가 구현)
"""
"""
10:35 시작
10:39 구상 완료
10:52 구현 완료
"""
from collections import deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_group(arr, si, sj):  # group 크기 return
    q = deque([(si, sj)])
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if OOB(ni, nj): continue
            if v[ni][nj]: continue
            if not arr[ni][nj]: continue

            v[ni][nj] = 1
            q.append((ni, nj))
            cnt += 1

    return cnt


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
X, Q = map(int, input().split())
N = 2 ** X
arr = [list(map(int, input().split())) for _ in range(N)]
levels = list(map(int, input().split()))

for level in levels:
    if level:  # 돈다
        qn = 2 ** level  # 도는 크기

        for si in range(0, N, qn):
            for sj in range(0, N, qn):
                square = []  # 돌릴 사각형
                sqn = qn // 2
                for ssi in range(si, si + qn, sqn):
                    row = []
                    for ssj in range(sj, sj + qn, sqn):
                        s = []
                        for i in range(ssi, ssi + sqn):
                            s.append(arr[i][ssj:ssj + sqn])
                        row.append(s)
                    square.append(row)

                c_square = list(zip(*square[::-1]))

                for a in range(2):
                    for b in range(2):
                        block = c_square[a][b]
                        ssi = si + a * sqn
                        ssj = sj + b * sqn

                        for i in range(sqn):
                            for j in range(sqn):
                                arr[ssi + i][ssj + j] = block[i][j]

    # 녹는다
    near_cnt_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]:  # 얼음 있다 -> 4방향 표시
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if OOB(ni, nj): continue
                    near_cnt_arr[ni][nj] += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] and near_cnt_arr[i][j] < 3:  # 녹는 얼음
                arr[i][j] -= 1

v = [[0] * N for _ in range(N)]
mx_cnt = 0
for i in range(N):
    for j in range(N):
        if v[i][j] or not arr[i][j]: continue
        mx_cnt = max(mx_cnt, find_group(arr, i, j))
print(sum([sum(a) for a in arr]))
print(mx_cnt)

"""
마법사 상어와 파이어스톰
"""

"""
14:36~14:51 구상
14:51~15:24 구현

깡구현 문제라 구상은 어렵지 않았다.
다만 구현에서 실수가 많았다. sj를 써야 하는데 빼먹었다던가...
얼음이 있을 때만 q에 넣어야 하는데 조건을 빼먹었다던가...
제대로 구현해두고 갑자기 체크무늬인 줄 착각해서 조건 추가했다 뺐다던가...
테스트케이스가 없었다면 네번은 더 틀렸을 것 같다...

구현 문제는 제출 전 적어도 한번은 디버거를 통해 잘 작동하는지 확인하도록 하자

그래도 침착하게 디버깅 하려고 노력했다. 조금 더 차분하고 꼼꼼하게 읽어야겠다.

배열을 돌릴 때 시간초과가 걱정되어서 행을 통으로 바꿨다.
시작좌표는 무조건 si, sj를 써오고 있는데 이 습관이 좋은 것 같다.

시험 시작 전 간식을 까먹어서 중간에 너무 배고팠다... 시험 전 간식을 잊지 말자
"""
from collections import deque


def go_round(l, arr):
    mN = 2 ** l

    for si in range(0, aN, mN):
        for sj in range(0, aN, mN):
            cut_arr = []
            for mi in range(mN):
                cut_arr.append(arr[si + mi][sj:sj + mN])
            cut_arr = list(map(list, zip(*cut_arr[::-1])))

            for mi in range(mN):
                arr[si + mi][sj:sj + mN] = cut_arr[mi]
    return


def get_ice_size(si, sj):  # si, sj와 연결된 얼음 크기 return
    v[si][sj] = 1
    q = deque([(si, sj)])
    cnt = 1

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < aN and 0 <= nj < aN): continue
            if arr[ni][nj] == 0: continue
            if v[ni][nj]: continue

            v[ni][nj] = 1
            q.append((ni, nj))
            cnt += 1

    return cnt


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, Q = map(int, input().split())
aN = 2 ** N
arr = [list(map(int, input().split())) for _ in range(aN)]
magic_lst = list(map(int, input().split()))

for l in magic_lst:
    # 회전
    if l > 0:
        go_round(l, arr)

    melt = [[False] * aN for _ in range(aN)]  # 녹으면 True

    # 얼음 check
    for i in range(aN):
        for j in range(aN):

            if arr[i][j] == 0: continue

            cnt = 0  # i, j에서 인접한 얼음 수

            for d in range(4):
                ni, nj = i + di[d], j + dj[d]

                if not (0 <= ni < aN and 0 <= nj < aN): continue
                if arr[ni][nj] > 0:
                    cnt += 1

            if cnt < 3:
                melt[i][j] = True

    # 얼음 녹이기
    for i in range(aN):
        for j in range(aN):
            if melt[i][j]: arr[i][j] -= 1

# 답안 출력하기
v = [[0] * aN for _ in range(aN)]
biggest = 0
remain = 0
for i in range(aN):
    remain += sum(arr[i])

    for j in range(aN):
        if arr[i][j] == 0: continue
        if v[i][j]: continue

        biggest = max(biggest, get_ice_size(i, j))

print(remain)
print(biggest)
