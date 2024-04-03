"""
실행시간: 236 -> 228
풀이시간: 27분 -> 17분
"""

"""
10:17 시작
10:23 구상 완료
10:31 1차 구현 완료
10:34 디버깅 - ans 갱신 시점 수정

바이러스가 병원은 지나가는데 벽은 지나갈 수 없다. 또한 바이러스가 모두 없어지는 순간 끝내야 하는 점이 까다로웠다.
이를 맨 처음 바이러스의 개수를 세어서 개수로 관리하고자 했다.

조합 코드는 배영석 프로님 코드를 도입했다.
"""

from collections import deque


def pick(nth, si):  # 뽑기
    if nth == K:
        simulation()
        return

    for idx in range(si, hN):
        idx_lst[nth] = idx
        pick(nth + 1, idx + 1)


def simulation():
    global ans
    v = [[0] * N for _ in range(N)]
    q = deque()
    for idx in idx_lst:
        hi, hj = hospitals[idx]
        v[hi][hj] = 1
        q.append((hi, hj))
    z = zero_cnt

    t = -1
    while q:
        t += 1
        nq = len(q)

        if not z:  # 바이러스 모두 소탕
            ans = min(ans, t)
            return

        for _ in range(nq):
            ci, cj = q.popleft()

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]

                if not (0 <= ni < N and 0 <= nj < N): continue
                if v[ni][nj]: continue
                if arr[ni][nj] == 1: continue  # 벽

                if arr[ni][nj] == 0:  # 바이러스
                    z -= 1
                v[ni][nj] = 1
                q.append((ni, nj))

    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hospitals = []
zero_cnt = 0
ans = N * N + 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            hospitals.append((i, j))
        elif arr[i][j] == 0:
            zero_cnt += 1
hN = len(hospitals)
idx_lst = [0] * K
pick(0, 0)

if ans == N * N + 1:
    ans = -1
print(ans)

"""
3:40 구상 시작
4:07 구현 완료

조합 실수를 하지 않기 위해 설계에 엄청 강조했다...휴
보수적으로 설게했고 그래서 구현이 쉬웠다.

타임스탬프 또 까먹었다! 다음엔 잊지 말자
해슬 프로님 코드를 참고하여 간결한 조합 코드를 도입했다. 이거 좋다
"""

"""
첫번째 풀이
모든 칸 시간 갱신 후 바이러스 칸만 1로 수정
"""
import sys
from collections import deque

input = sys.stdin.readline


def pick(cnt, start):
    if cnt == M:
        combinations.append(tuple(temp))
        return

    for n in range(start, vN):
        temp.append(n)
        pick(cnt + 1, n + 1)
        temp.pop()


def spread(combi):
    v = [[0] * N for _ in range(N)]
    q = deque()

    for idx in combi:
        vi, vj = virus_lst[idx]
        q.append((vi, vj))
        v[vi][vj] = 1

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if arr[ni][nj] == 1: continue
            if v[ni][nj]: continue

            v[ni][nj] = v[ci][cj] + 1
            q.append((ni, nj))

    for vi, vj in virus_lst:
        v[vi][vj] = 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and v[i][j] == 0:
                return INF
    mx = 0
    for vv in v:
        mx = max(mx, max(vv))

    return mx - 1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_lst.append((i, j))

vN = len(virus_lst)
temp = []
combinations = []
pick(0, 0)

INF = N * N + 1
ans = INF

for combi in combinations:
    ans = min(ans, spread(combi))

if ans == INF:
    ans = -1
print(ans)

"""
다른 방식의 풀이
바이러스 칸이 아닐 때 시간 갱신
"""

import sys
from collections import deque

input = sys.stdin.readline


def pick(cnt, start):
    if cnt == M:
        combinations.append(tuple(temp))
        return

    for n in range(start, vN):
        temp.append(n)
        pick(cnt + 1, n + 1)
        temp.pop()


def spread(idx_lst):
    v = [[0] * N for _ in range(N)]
    q = deque()

    for idx in idx_lst:  # 선택된 바이러스 큐에 넣기
        vi, vj = virus_lst[idx]
        q.append((vi, vj))
        v[vi][vj] = 1

    mxt = 0
    b_cnt = blank_cnt

    while q:
        ci, cj = q.popleft()

        if arr[ci][cj] != 2:  # 바이러스 칸이 아니면 시간 갱신
            mxt = max(mxt, v[ci][cj])

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue
            if arr[ni][nj] == 1: continue
            if v[ni][nj]: continue
            if arr[ni][nj] == 0:  # 빈칸 제거
                b_cnt -= 1
            v[ni][nj] = v[ci][cj] + 1
            q.append((ni, nj))

    if b_cnt:  # 남은 빈칸이 있으면 실패
        return INF

    return mxt - 1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus_lst = []
blank_cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_lst.append((i, j))
        elif arr[i][j] == 0:
            blank_cnt += 1

if blank_cnt == 0:
    print(0)
else:
    vN = len(virus_lst)
    temp = []
    combinations = []
    pick(0, 0)

    INF = N * N + 1
    ans = INF

    for combi in combinations:
        ans = min(ans, spread(combi))

    if ans == INF:
        ans = -1
    print(ans)
