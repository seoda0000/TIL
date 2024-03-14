'''
연구소 3
https://www.acmicpc.net/problem/17142
백준 골드4

인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다.
가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다.
연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
'''


import sys
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def f(com):  # 조합별 소모시간 구하는 함수
    arr = [item[:] for item in firstarr]
    q = deque([])
    for c in com:
        ci, cj = c
        q.append((ci, cj))
        arr[ci][cj] = 3  # 시작 바이러스 3으로 변경
    mxt = 3
    while q:
        vi, vj = q.popleft()

        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 네 방향 탐색
            ni = vi + a
            nj = vj + b
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:  # 빈칸이면 바이러스 퍼뜨리기
                    arr[ni][nj] = arr[vi][vj] + 1
                    q.append((ni, nj))
                    if arr[ni][nj] > mxt:  # 진행 시간 갱신
                        mxt = arr[ni][nj]
                elif arr[ni][nj] == 2:     # 바이러스가 있으면 활성화
                    arr[ni][nj] = arr[vi][vj] + 1
                    q.append((ni, nj))     # 이미 바이러스가 있으므로 진행 시간 갱신 x
    for a in arr:
        if 0 in a:
            return
    else:
        return mxt-3


N, M = map(int, input().split())
firstarr = [list(map(int, input().split())) for _ in range(N)]
virus = []
full = 0               # 이미 채워져있는지 확인하는 flag
for i in range(N):
    if 0 not in firstarr[i]:
        full += 1
    for j in range(N):
        if firstarr[i][j] == 2:
            virus.append((i, j))
combi = list(combinations(virus, M))    # 조합 구하기
if full == N:           # N개 행이 모두 채워져 있을 경우 0 return 후 종료
    answer = 0
else:
    answer = 2500       # 범위 내 최대시간
    for com in combi:
        if f(com) and answer > f(com):  # 최소시간 갱신
            answer = f(com)

    if answer == 2500:  # 갱신되지 않았다면 -1
        answer = -1
print(answer)

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
