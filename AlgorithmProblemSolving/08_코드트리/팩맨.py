"""
3:54 시작
4:03 구상 완료
4:26 1차 구현 완료
4:57 디버깅 완료 : 물고기 없어도 죽이고 있었음
"""


def OOB(i, j):
    return not (0 <= i < 4 and 0 <= j < 4)


def go(ci, cj, ij_set: set, ds: str):
    if len(ds) == 3:  # 3번 이동 완료
        sm = 0
        for i, j in list(ij_set):
            sm += sum(moved_arr[i][j])
        move_lst.append((sm, ds))
        return

    for d in [0, 2, 4, 6]:
        ni, nj = ci + di[d], cj + dj[d]
        if OOB(ni, nj): continue
        go(ni, nj, ij_set | {(ni, nj)}, ds + str(d))


di = [-1, -1, 0, 1, 1, 1, 0, -1]  # 코드트리
dj = [0, -1, -1, -1, 0, 1, 1, 1]
baekjun_dic = {1: 2, 2: 1, 3: 0, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3}

monster_cnt, T = map(int, input().split())
# pi, pj = map(int, input().split()) # 코드트리

dead_arr = [[0] * 4 for _ in range(4)]
arr = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
for _ in range(monster_cnt):
    i, j, d = map(int, input().split())
    arr[i - 1][j - 1][baekjun_dic[d]] += 1

pi, pj = map(int, input().split())  # 백준

pi -= 1
pj -= 1

for t in range(T):
    moved_arr = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

    # 몬스터 이동
    for ci in range(4):
        for cj in range(4):
            for ck in range(8):
                if not arr[ci][cj][ck]: continue
                cnt = arr[ci][cj][ck]
                d = ck

                for _ in range(8):
                    ni, nj = ci + di[d], cj + dj[d]
                    if OOB(ni, nj) or dead_arr[ni][nj] or (pi == ni and pj == nj):  # 이동불가
                        d = (d + 1) % 8
                        continue
                    # 갈 수 있다
                    moved_arr[ni][nj][d] += cnt
                    break
                else:  # 이동 불가
                    moved_arr[ci][cj][ck] += cnt

    # 팩맨 이동
    move_lst = []
    go(pi, pj, set(), '')
    move_lst.sort(key=lambda x: (-x[0], x[1]))
    ds = move_lst[0][1]
    for d in map(int, ds):
        pi, pj = pi + di[d], pj + dj[d]
        if sum(moved_arr[pi][pj]):
            moved_arr[pi][pj] = [0] * 8
            dead_arr[pi][pj] = 3

    # 몬스터 시체 소멸
    for i in range(4):
        for j in range(4):
            if dead_arr[i][j]:
                dead_arr[i][j] -= 1

    # 몬스터 복제 완성
    for i in range(4):
        for j in range(4):
            for k in range(8):
                arr[i][j][k] += moved_arr[i][j][k]

ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(arr[i][j])
print(ans)
