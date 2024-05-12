"""
실행시간: 564(556) -> 208
풀이시간: 79분 -> 63분

물고기가 없어도 죽이는 오류 + 시간 배열을 감소시키는 타이밍
두가지 오류가 겹쳐서 디버깅이 오래 걸렸다.
솔직히 문제가 이상하게 설명하고 있었다!!!
디버깅시에는 모든 것을 의심하자

timestamp 배열 연습으로 한번 더 풀어보면 좋을 것 같다

"""

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

"""
0:05 문제 읽기 시작
0:09 읽기 완료
0:16 구상 완료
0:48 1차 구현 완료, tc3 오류 발견
0:54 냄새 로직 문제와 똑같이 수정 -> tc3 오류 해결
0:55 tc 5, 6 오류 발견 후 문제 정독
1:02 tc 3으로 예제와 코드 일치 확인
1:10 예제 6 디버거로 확인 + 문제 정독
1:12 방문 체크 로직 분기
1:15 tc 전체 통과 확인
1:17 제출 후 틀렸습니다 확인
1:19 방문 체크 로직 리스트로 수정 후 제출

간 곳을 또 간다는 생각을 못해서 디버깅이 오래 걸렸다.
그 생각을 한 후에도 v 배열을 유지해보려다가 틀렸다. 직감적으로 될 것 같았는데 그러지 않았다.
dfs/백트랙킹에서는 최대한 보수적으로 생각해서 구현하자. 100% 파악하지 못한 로직이 스스로 알아서 잘 돌아갈 것이라고 기대하는 것은 만용이다

"""

import copy
import sys

input = sys.stdin.readline


def move_fish(ocean):
    new_ocean = [[list() for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for fd in ocean[i][j]:
                ni, nj, nfd = choose_fish_d(i, j, fd)
                new_ocean[ni][nj].append(nfd)

    return new_ocean


def choose_fish_d(i, j, first_fd):
    first_cnt = -1
    fd = first_fd
    while True:
        if fd == first_fd:
            first_cnt += 1
            if first_cnt == 1:
                break
        ni, nj = i + di[fd], j + dj[fd]

        if not (0 <= ni < N and 0 <= nj < N):
            fd = (fd - 1) % 8
            continue
        if smell_arr[ni][nj]:
            fd = (fd - 1) % 8
            continue
        if ni == si and nj == sj:
            fd = (fd - 1) % 8
            continue
        break

    if first_cnt == 1:
        return i, j, first_fd
    else:
        return ni, nj, fd


def go(ci, cj, idx, lst):
    if idx >= 100:
        fish_cnt = 0
        for num in set(lst):
            i, j = divmod(num, 4)
            fish_cnt += len(ocean[i][j])

        shark_choices.append((fish_cnt, idx))
        return

    for d in [2, 0, 6, 4]:
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): continue
        go(ni, nj, idx * 10 + dir_to_idx[d], lst + [ni * 4 + nj])

    return


di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_to_idx = {2: 1, 0: 2, 6: 3, 4: 4}
idx_to_dir = {1: 2, 2: 0, 3: 6, 4: 4}
N = 4
ocean = [[list() for _ in range(N)] for _ in range(N)]
fish_cnt, S = map(int, input().split())
for _ in range(fish_cnt):
    x, y, d = map(int, input().split())
    ocean[x - 1][y - 1].append(d - 1)
si, sj = map(int, input().split())
si, sj = si - 1, sj - 1
smell_arr = [[0] * N for _ in range(N)]  # 냄새가 사라지기까지의 시간 배열
smell_time = 2  # 냄새 지속 시간
for _ in range(S):
    # 복제 마법
    copy_ocean = copy.deepcopy(ocean)

    # 물고기 이동
    ocean = move_fish(ocean)

    # 냄새가 옅어진다
    for i in range(N):
        for j in range(N):
            if smell_arr[i][j]:
                smell_arr[i][j] -= 1

    # 상어 이동
    shark_choices = []  # (물고기 수, 경로의 index)
    go(si, sj, 0, [])

    shark_choices.sort(key=lambda x: (-x[0], x[1]))
    _, choice = shark_choices[0]

    for c in str(choice):
        d = idx_to_dir[int(c)]
        si, sj = si + di[d], sj + dj[d]
        if ocean[si][sj]:
            smell_arr[si][sj] = smell_time
        ocean[si][sj] = []

    # 물고기가 복제된다
    for i in range(N):
        for j in range(N):
            ocean[i][j].extend(copy_ocean[i][j])

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(ocean[i][j])

print(ans)
