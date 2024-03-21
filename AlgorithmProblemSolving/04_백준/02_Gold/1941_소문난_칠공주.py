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

"""
dfs를 활용한 풀이
"""

import sys

input = sys.stdin.readline


def find_princesses(lst):
    global ans

    lst.sort()
    if tuple(lst) in st:  # 이미 확인한 그룹이면 pass
        return
    else:
        st.add(tuple(lst))

    if len(lst) == 7:
        if check_s(lst):
            ans += 1
        return

    for li, lj in lst:
        for d in range(4):
            ni, nj = li + di[d], lj + dj[d]

            if not (0 <= ni < 5 and 0 <= nj < 5): continue  # 범위 밖
            if v[ni][nj]: continue
            v[ni][nj] = 1
            find_princesses(lst + [(ni, nj)])
            v[ni][nj] = 0

    return


def check_s(lst):  # 이다솜파가 4명 이상인지 여부
    s_cnt = 0
    for li, lj in lst:
        if arr[li][lj] == 'S':
            s_cnt += 1

    return s_cnt >= 4


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
arr = [input() for _ in range(5)]
st = set()  # 그룹 기록
ans = 0
v = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        v[i][j] = 1
        find_princesses([(i, j)])
        v[i][j] = 0

print(ans)
