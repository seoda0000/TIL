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
