from collections import deque


def somCntMoreThanFour(lst):
    cnt = 0
    for l in lst:
        cnt += isSomByIdx(l)
    return (cnt >= 4)


def closeEachOther(lst):
    for l in lst:
        li, lj = l // 5, l % 5
        v[li][lj] = 1

    s = lst.pop()
    si, sj = s // 5, s % 5
    q = deque([(si, sj)])
    v[si][sj] = 2

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if not (0 <= ni < 5 and 0 <= nj < 5): continue
            if v[ni][nj] != 1: continue
            v[ni][nj] = 2
            q.append((ni, nj))

    for row in v:
        if row.count(1):
            return False

    return True


def isSomByIdx(n: int):
    i, j = n // 5, n % 5
    return int(arr[i][j] == 'S')


arr = [input() for _ in range(5)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0
for s1 in range(19):
    for s2 in range(s1 + 1, 20):
        for s3 in range(s2 + 1, 21):
            for s4 in range(s3 + 1, 22):
                for s5 in range(s4 + 1, 23):
                    for s6 in range(s5 + 1, 24):
                        for s7 in range(s6 + 1, 25):
                            lst = [s1, s2, s3, s4, s5, s6, s7]
                            if not somCntMoreThanFour(lst):
                                continue
                            v = [[0] * 5 for _ in range(5)]
                            if not closeEachOther(lst):
                                continue
                            ans += 1
print(ans)
