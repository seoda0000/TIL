"""
https://www.acmicpc.net/problem/16509
백준 골드5 16509 장군

"""

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ei = [-1, 1, 1, -1]
ej = [1, 1, -1, -1]

N, M = 10, 9
v = [[-1] * M for _ in range(N)]
si, sj = map(int, input().split())
Ki, Kj = map(int, input().split())
q = deque([(si, sj)])
ans = 0
v[si][sj] = 0

while q:
    ci, cj = q.popleft()
    if ci == Ki and cj == Kj:
        ans = v[ci][cj]
        break

    for d in range(4):
        i1, j1 = ci + di[d], cj + dj[d]

        # 사방 이동 불가능
        if not (0 <= i1 < N and 0 <= j1 < M): continue
        if i1 == Ki and j1 == Kj: continue

        # 사방 이동 가능
        for e in [d - 1, d]:
            i2, j2 = i1 + ei[e], j1 + ej[e]

            # 한칸 이동 불가능
            if not (0 <= i2 < N and 0 <= j2 < M): continue
            if i2 == Ki and j2 == Kj: continue

            # 한칸 이동 가능
            i3, j3 = i2 + ei[e], j2 + ej[e]

            # 두칸 이동 불가능
            if not (0 <= i3 < N and 0 <= j3 < M): continue
            if v[i3][j3] >= 0: continue

            # 두칸 이동 가능
            v[i3][j3] = v[ci][cj] + 1
            q.append((i3, j3))

print(ans)
