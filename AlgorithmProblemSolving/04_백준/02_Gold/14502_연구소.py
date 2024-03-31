"""
실행시간: 1072(최적화: 460) -> 520
풀이시간: 24분 -> 20분

이전에 했던 순열조합 실수를 안했다는 것에 의의를 둔다...
이전엔 총합에서 퍼진 칸을 빼주는 식이었다면 이번엔 퍼진 칸을 합한 후 마지막에 빼줬다. 훨씬 직관적인 것 같다!
"""
from collections import deque


def solve(arr):
    q = deque(fire_lst)
    v = [[0] * M for _ in range(N)]
    cnt = 0
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if arr[ni][nj]: continue

            cnt += 1
            v[ni][nj] = 1
            q.append((ni, nj))

    return bN - cnt


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = []
blank_lst = []
fire_lst = []
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(M):
        if ipt[j] == 0:
            blank_lst.append((i, j))
        elif ipt[j] == 2:
            fire_lst.append((i, j))
    arr.append(ipt)
bN = len(blank_lst)

ans = 0
for a in range(bN - 2):
    ai, aj = blank_lst[a]
    arr[ai][aj] = 1
    for b in range(a + 1, bN - 1):
        bi, bj = blank_lst[b]
        arr[bi][bj] = 1
        for c in range(b + 1, bN):
            ci, cj = blank_lst[c]
            arr[ci][cj] = 1

            ans = max(ans, solve(arr))

            arr[ci][cj] = 0
        arr[bi][bj] = 0
    arr[ai][aj] = 0
print(ans - 3)

"""
15:23~15:32: 구상
15:32~15:47: 구현

원상복구가 귀찮아서 배열 복사를 했다. visited + 원상복구도 구현해보자!
-> return 전에 원상복구 잊지 말자! / 아예 check와 원상복구를 밖으로 빼도 된다.

deque로 만들 거면 set이 아닌 list여도 된다.

왜 이렇게 오래 걸리시는지...?
-> 맞은 게 신기하다. 조합을 구해야 하는데 순열을 구했다. 헐...
-> 제출 전 손코딩과 최종 결과물을 꼭 비교하자!!!

하나하나 세는 것보다 count 메서드가 빠르다.
"""

from collections import deque
import sys

input = sys.stdin.readline


def check_virus():
    global ans

    v = [[0] * M for _ in range(N)]
    for vi, vj in viruses:
        v[vi][vj] = 1

    z = zero_cnt - 3
    q = deque(viruses)

    while q:

        if z <= ans: return  # 가지치기

        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] != 0: continue
            if v[ni][nj]: continue
            v[ni][nj] = 1
            q.append((ni, nj))
            z -= 1

    ans = max(ans, z)
    return


N, M = map(int, input().split())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
arr = [list(map(int, input().split())) for _ in range(N)]
viruses = []
blanks = []
zero_cnt = 0
for i in range(N):
    zero_cnt += arr[i].count(0)
    for j in range(M):
        if arr[i][j] == 2:
            viruses.append((i, j))
        elif arr[i][j] == 0:
            blanks.append((i, j))

ans = 0
bn = len(blanks)
for a in range(bn - 2):
    for b in range(a + 1, bn - 1):
        for c in range(b + 1, bn):
            walls = [blanks[a], blanks[b], blanks[c]]
            for wi, wj in walls:  # 벽 세우기
                arr[wi][wj] = 1
            check_virus()
            for wi, wj in walls:  # 원상복구
                arr[wi][wj] = 0

print(ans)
