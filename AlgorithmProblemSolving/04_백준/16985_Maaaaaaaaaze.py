from collections import deque


def make_cube(nth):
    if nth == 5:
        if tuple(temp)[::-1] not in idx_lst:
            idx_lst.append(tuple(temp))
        return

    for n in range(5):
        if v_temp[n]: continue
        v_temp[n] = 1
        temp[nth] = n
        make_cube(nth + 1)
        v_temp[n] = 0
        temp[nth] = 0

    return


def solve_cube():
    for a1 in range(4):
        for a2 in range(4):
            for a3 in range(4):
                for a4 in range(4):
                    for a5 in range(4):

                        for b1, b2, b3, b4, b5 in idx_lst:
                            cube = [arrs[b1][a1]] \
                                   + [arrs[b2][a2]] \
                                   + [arrs[b3][a3]] \
                                   + [arrs[b4][a4]] \
                                   + [arrs[b5][a5]]
                            for p in range(4):
                                escape_cube(cube, p)
                            if ans == FLOOR:
                                return
    return


def escape_cube(cube, p):
    global ans

    sk, si, sj = start_point[p]
    ek, ei, ej = end_point[p]
    if cube[sk][si][sj] == 0 or cube[ek][ei][ej] == 0: return

    v = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    v[sk][si][sj] = 1
    q = deque([(sk, si, sj)])

    k = -1
    while q:
        k += 1
        nq = len(q)

        if k >= ans: return  # 가지치기

        for _ in range(nq):
            ck, ci, cj = q.popleft()
            if (ck, ci, cj) == (ek, ei, ej):
                ans = min(ans, k)
                return

            for d in range(6):
                nk, ni, nj = ck + dk[d], ci + di[d], cj + dj[d]
                if not (0 <= nk < 5 and 0 <= ni < 5 and 0 <= nj < 5): continue
                if cube[nk][ni][nj] == 0: continue
                if v[nk][ni][nj]: continue
                v[nk][ni][nj] = 1
                q.append((nk, ni, nj))
    return


di = [0, 0, 1, -1, 0, 0]
dj = [1, -1, 0, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]
start_point = [(0, 0, 0), (0, 0, 4), (0, 4, 0), (0, 4, 4)]
end_point = [(4, 4, 4), (4, 4, 0), (4, 0, 4), (4, 0, 0)]
arrs = [[[list(map(int, input().split())) for _ in range(5)]] for _ in range(5)]

for a in range(5):
    for _ in range(3):
        arrs[a].append(list(zip(*arrs[a][-1][::-1])))
INF = 5 * 5 * 5 + 1
FLOOR = 12
ans = INF
temp = [0] * 5
v_temp = [0] * 5
idx_lst = []
make_cube(0)
solve_cube()

if ans != INF:
    print(ans)
else:
    print(-1)
