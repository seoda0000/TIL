"""
16:39 시작
16:48 구상 완료
17:00 구현 완료
17:04 자체 tc 시험
17:08 제출
"""


def move(i, j, s, d):
    i_idx, j_idx = (i + di[d] * s) % len(i_idx_lst), (j + dj[d] * s) % len(j_idx_lst)
    ni, nj = i_idx_lst[i_idx], j_idx_lst[j_idx]
    if i_idx >= N or j_idx >= M:
        d ^= 1
    return ni, nj, d


di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
N, M, K = map(int, input().split())
i_idx_lst = list(range(N)) + list(range(1, N - 1)[::-1])
j_idx_lst = list(range(M)) + list(range(1, M - 1)[::-1])
virus_lst = []  # (좌표 i, j, 속도, 방향, 크기)
for _ in range(K):
    x, y, s, d, b = map(int, input().split())
    virus_lst.append((x - 1, y - 1, s, d - 1, b))

ans = 0
virus_lst.sort()
for j in range(M):

    vN = len(virus_lst)

    for x in range(vN):
        vi, vj, vs, vd, vb = virus_lst[x]
        if vj == j:  # 곰팡이 발견
            ans += vb
            virus_lst.pop(x)
            break

    # 곰팡이 이동
    nxt_virus_lst = []
    for vi, vj, vs, vd, vb in virus_lst:
        ni, nj, nd = move(vi, vj, vs, vd)
        nxt_virus_lst.append((ni, nj, vs, nd, vb))

    virus_lst = nxt_virus_lst
    virus_lst.sort(key=lambda x: (x[0], x[1], -x[-1]))
    vN = len(virus_lst)

    # 곰팡이 잡아먹기
    for x in range(1, vN)[::-1]:
        if virus_lst[x][0] == virus_lst[x - 1][0] and virus_lst[x][1] == virus_lst[x - 1][1]:
            virus_lst.pop(x)

print(ans)
