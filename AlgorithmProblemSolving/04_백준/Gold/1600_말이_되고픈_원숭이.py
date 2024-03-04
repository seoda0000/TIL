from collections import deque


def go_monkey():
    v = [[-1] * M for _ in range(N)]
    q = deque([(0, 0, K)])
    cnt = 0
    v[0][0] = K  # 남은 K 수

    while q:
        cnt += 1
        nq = len(q)

        for _ in range(nq):
            ci, cj, ck = q.popleft()

            if ci == N - 1 and cj == M - 1:
                return cnt - 1

            for d in range(4):  # 원숭이
                ni, nj = ci + di[d], cj + dj[d]

                if not (0 <= ni < N and 0 <= nj < M): continue
                if arr[ni][nj]: continue
                vk = v[ni][nj]
                if vk != -1 and vk >= ck: continue
                v[ni][nj] = ck
                q.append((ni, nj, ck))

            if ck == 0: continue  # 더 이상 K가 없다

            for e in range(8):  # 말
                ni, nj = ci + ei[e], cj + ej[e]

                if not (0 <= ni < N and 0 <= nj < M): continue
                if arr[ni][nj]: continue
                vk = v[ni][nj]
                if vk != -1 and vk >= ck - 1: continue
                v[ni][nj] = ck - 1
                q.append((ni, nj, ck - 1))

    return -1


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ei = [-1, -2, -2, -1, 1, 2, 2, 1]
ej = [-2, -1, 1, 2, -2, -1, 1, 2]
K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = go_monkey()

print(ans)
