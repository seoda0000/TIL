"""
실행시간: 2988(340) -> 448
풀이시간: 40분 -> 29분

이전에 배운 인덱스 배열 아이디어를 활용하여 풀었다.
이전에는 id를 이용했는데, 딱히 필요 없어서 (애초에 주어지는 id가 없다) 상어 리스트만으로 풀이를 진행했다.
"""

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

"""
9:50 시작
9:52 문제 읽기 완료
9:59 구상 완료
10:20 구현
10:30 디버깅 후 제출 (ni, nj를 ci, cj로 쓰는 오타 & 상어 한마리만 잡아야 함)

<실수한 부분>
오타가 있었다... 범위 체크할 때 ni, nj가 아닌 ci, cj를 체크하고 있었다. 디버거를 활용해 바로 잡아냈다.
또 상어를 한마리만 잡아야 하는데 모든 상어를 잡아버렸다...!! 설계를 한 후 주석으로 옮기는 습관을 들이자

제출 후 굳이 딕셔너리를 쓰지 않아도 될 것 같아서 배열에 모든 정보를 저장하는 로직으로 리팩토링 했다.
속도는 더 늦지만 딕셔너리 하다가 막히면 시도해봐야겠다.

+ 배열 조차 없앤 풀이
+ 인덱스 배열을 활용하여 이동 로직 단순화 (강사님, 유경 프로님 코드 참고)
"""

"""
딕셔너리와 id를 이용한 풀이
"""


def move_shark(id):  # 상어 이동, dic 수정 ->  상어 위치 반환
    r, c, s, d, z = shark_dic[id]

    mi, mj = (r + di[d] * s) % len(move_i), (c + dj[d] * s) % len(move_j)
    ni, nj = move_i[mi], move_j[mj]

    if not (0 <= mi < R and 0 <= mj < C): d = oppo[d]

    shark_dic[id] = ni, nj, s, d, z

    return ni, nj


di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
oppo = {1: 2, 2: 1, 3: 4, 4: 3}
R, C, M = map(int, input().split())
arr = [[list() for _ in range(C)] for _ in range(R)]
shark_dic = dict()
id = 0

move_i = [n for n in range(R)]  # 0, 1, 2, 3, 2, 1
move_j = [n for n in range(C)]

for i in range(R - 2, 0, -1):
    move_i.append(i)
for i in range(C - 2, 0, -1):
    move_j.append(i)

for _ in range(M):  # 상어 정보 받기
    id += 1
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    shark_dic[id] = (r, c, s, d, z)
    arr[r][c].append(id)

MAX_ID = id
ans = 0

for j in range(C):  # 열마다

    # 땅에서 가장 가까운 상어 잡기
    for i in range(R):
        if arr[i][j]:
            id = arr[i][j].pop()
            ans += shark_dic[id][4]
            shark_dic[id] = ()
            break

    # 상어 이동
    nxt_arr = [[list() for _ in range(C)] for _ in range(R)]

    for id in range(1, MAX_ID + 1):
        if shark_dic[id]:  # 아직 id의 상어가 있다
            r, c = move_shark(id)  # 상어 이동, dic 수정 ->  상어 위치 반환
            nxt_arr[r][c].append(id)

    # 같은 칸 상어 맞짱뜨기
    for i in range(R):
        for j in range(C):
            if len(nxt_arr[i][j]) > 1:
                sharks = []
                for id in nxt_arr[i][j]:
                    sharks.append((id, shark_dic[id][4]))  # id, 크기
                sharks.sort(key=lambda x: -x[1])  # 크기 비교
                winner_shark_id = sharks[0][0]

                nxt_arr[i][j] = [winner_shark_id]

                for x in range(1, len(sharks)):
                    loser_shark_id = sharks[x][0]
                    shark_dic[loser_shark_id] = ()

    arr = nxt_arr

print(ans)

"""
배열만으로 푸는 풀이
"""


def move_shark(r, c, s, d):  # 상어 이동 후 정보 return

    ci, cj = r, c
    for _ in range(s):
        ni, nj = ci + di[d], cj + dj[d]

        if not (0 <= ni < R and 0 <= nj < C):
            d = oppo[d]
            ni, nj = ci + di[d], cj + dj[d]
        ci, cj = ni, nj

    return ci, cj, d


di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
oppo = {1: 2, 2: 1, 3: 4, 4: 3}
R, C, M = map(int, input().split())
arr = [[list() for _ in range(C)] for _ in range(R)]
for _ in range(M):  # 상어 정보 받기
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    arr[r][c].append((s, d, z))  # 해당 위치에 (속력, 이동방향, 크기) 저장

ans = 0
for j in range(C):  # 열마다

    # 땅에서 가장 가까운 상어 잡기
    for i in range(R):
        if arr[i][j]:
            ans += arr[i][j].pop()[-1]
            break

    # 상어 이동
    nxt_arr = [[list() for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            sharks = arr[i][j]
            if not sharks: continue

            for shark in sharks:
                s, d, z = shark
                ni, nj, nd = move_shark(i, j, s, d)
                nxt_arr[ni][nj].append((s, nd, z))
    arr = nxt_arr

    # 같은 칸 상어 맞짱뜨기
    for i in range(R):
        for j in range(C):
            arr[i][j]
            if len(arr[i][j]) > 1:
                arr[i][j].sort(key=lambda x: -x[-1])  # 크기 순 정렬
                arr[i][j] = arr[i][j][:1]  # 제일 큰 상어 빼고 다 처치

print(ans)

"""
배열조차 없이 푸는 풀이

강사님, 유경 프로님 코드 참고
천잰가...
"""


def move_shark(r, c, s, d, z):  # 상어 이동 후 정보 반환

    mi, mj = (r + di[d] * s) % len(move_i), (c + dj[d] * s) % len(move_j)
    ni, nj = move_i[mi], move_j[mj]

    if not (0 <= mi < R and 0 <= mj < C): d = oppo[d]

    return ni, nj, s, d, z


di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
oppo = {1: 2, 2: 1, 3: 4, 4: 3}
R, C, M = map(int, input().split())

move_i = [n for n in range(R)]  # 0, 1, 2, 3, 2, 1
move_j = [n for n in range(C)]

for i in range(R - 2, 0, -1):
    move_i.append(i)
for i in range(C - 2, 0, -1):
    move_j.append(i)

sharks = []
for _ in range(M):  # 상어 정보 받기
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    sharks.append((r, c, s, d, z))

ans = 0
sharks.sort()  # 땅과의 거리 순으로 정렬

for j in range(C):  # 열마다

    # 땅에서 가장 가까운 상어 잡기
    ns = len(sharks)
    for x in range(ns):
        r, c, s, d, z = sharks[x]

        if c == j:  # 해당 열의 가장 가까운 상어 발견
            ans += z
            sharks.pop(x)
            break

    # 상어 이동
    nxt_sharks = []  # 다음 상어 위치
    for x in range(len(sharks)):
        r, c, s, d, z = sharks[x]
        nxt_sharks.append(move_shark(r, c, s, d, z))  # 이동

    sharks = nxt_sharks
    sharks.sort(key=lambda x: (x[0], x[1], -x[-1]))  # 위치 정렬 후 크기가 큰 순서대로 정렬

    ns = len(sharks)
    for x in range(1, ns)[::-1]:  # 뒤에서부터 check (위치가 같은, 더 큰 상어가 있으면 삭제)

        cur = sharks[x]  # 이번 상어
        bef = sharks[x - 1]  # 비교 대상

        if cur[0] == bef[0] and cur[1] == bef[1]:  # 같은 위치일 경우 현재 상어 삭제
            nxt_sharks.pop(x)

print(ans)
