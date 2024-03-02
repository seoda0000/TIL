def findMincho(ci, cj, cs, cnt):
    global ans
    if abs(ci - si) + abs(cj - sj) <= cs:
        ans = max(ans, cnt)

    if ans == len(minchos): return

    for i in range(Nm):
        if v[i]: continue
        mi, mj = minchos[i]
        needStemina = abs(mi - ci) + abs(mj - cj)
        if needStemina <= cs:
            v[i] = 1
            findMincho(mi, mj, cs - needStemina + H, cnt + 1)
            v[i] = 0

    return


N, M, H = map(int, input().split())
minchos = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            si, sj = i, j
        elif row[j] == 2:
            minchos.append((i, j))
Nm = len(minchos)
v = [0] * Nm
ans = 0
findMincho(si, sj, M, 0)

print(ans)
