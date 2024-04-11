"""
복수 자료구조 유의
v배열 체크 유의
tc 하나하나 체크
"""
"""
4:43 시작
4:52 구상 완료
5:21 1차 구현 완료
5:44 디버깅 후 제출
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_close_santa(ri, rj):  # 가장 가까운 산타 찾기
    santas = []
    for id, values in santa_dic.items():
        si, sj, status = values
        if status == 0: continue
        h = (si - ri) ** 2 + (sj - rj) ** 2
        santas.append((h, si, sj))
    santas.sort(key=lambda x: (x[0], -x[1], -x[2]))
    _, si, sj = santas[0]
    return si, sj


def find_close_dir(si, sj, ei, ej, is_s):
    if is_s:
        dlst = [0, 2, 4, 6]
    else:
        dlst = list(range(8))
    ch = (si - ei) ** 2 + (sj - ej) ** 2

    lst = []
    for d in dlst:
        ni, nj = si + di[d], sj + dj[d]
        if OOB(ni, nj): continue
        if is_s and santa_arr[ni][nj]: continue  # 산타 조건
        nh = (ni - ei) ** 2 + (nj - ej) ** 2
        if nh >= ch: continue
        lst.append((nh, d))

    if not lst:
        return -1

    lst.sort()
    _, d = lst[0]

    return d


def throw_santa(id, d, k, turn):
    si, sj, status = santa_dic[id]
    santa_arr[si][sj] = 0
    ni, nj = si + di[d] * k, sj + dj[d] * k
    if OOB(ni, nj):  # 탈락
        santa_dic[id] = -1, -1, 0
        return
    elif santa_arr[ni][nj]:  # 다른 산타 있음
        push_santa(santa_arr[ni][nj], d)
    santa_dic[id] = ni, nj, -turn
    santa_arr[ni][nj] = id
    return


def push_santa(id, d):
    si, sj, status = santa_dic[id]
    santa_arr[si][sj] = 0
    ni, nj = si + di[d], sj + dj[d]
    if OOB(ni, nj):  # 탈락
        santa_dic[id] = -1, -1, 0
        return
    elif santa_arr[ni][nj]:  # 다른 산타 있음
        push_santa(santa_arr[ni][nj], d)
    santa_dic[id] = ni, nj, status
    santa_arr[ni][nj] = id
    return


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, T, P, C, D = map(int, input().split())
ri, rj = map(int, input().split())
ri, rj = ri - 1, rj - 1
santa_dic = dict()  # id: (i, j, status: 음수-기절 시점 0-탈락 1-정상)
santa_arr = [[0] * N for _ in range(N)]
for _ in range(P):
    id, si, sj = map(int, input().split())
    si, sj = si - 1, sj - 1
    santa_dic[id] = (si, sj, 1)
    santa_arr[si][sj] = id

scores = [0] * (P + 1)
for turn in range(1, T + 1):

    # 기절한 산타가 깨어난다
    remain_cnt = P
    for id in range(1, P + 1):
        si, sj, status = santa_dic[id]
        if status == 0:
            remain_cnt -= 1
            continue
        elif status == -(turn - 2):
            santa_dic[id] = si, sj, 1

    if not remain_cnt: break

    # 루돌프 이동
    si, sj = find_close_santa(ri, rj)
    rd = find_close_dir(ri, rj, si, sj, False)
    ri, rj = ri + di[rd], rj + dj[rd]
    if santa_arr[ri][rj]:  # 루 -> 산
        id = santa_arr[ri][rj]
        scores[id] += C
        throw_santa(id, rd, C, turn)

    # 산타 이동

    for id in range(1, P + 1):
        si, sj, status = santa_dic[id]
        if status <= 0:  # 기절, 탈락
            continue

        sd = find_close_dir(si, sj, ri, rj, True)
        if sd < 0: continue  # 이동 불가

        santa_arr[si][sj] = 0  # 이동 가능
        nsi, nsj = si + di[sd], sj + dj[sd]
        santa_dic[id] = nsi, nsj, status

        if nsi == ri and nsj == rj:  # 산 -> 루
            scores[id] += D
            throw_santa(id, (sd + 4) % 8, D, turn)

        else:
            santa_arr[nsi][nsj] = id

    for id in range(1, P + 1):
        si, sj, status = santa_dic[id]
        if status == 0: continue
        scores[id] += 1

print(*scores[1:])


"""
3:00 시작
3:12 구상 완료
3:44 메인 로직 구현 완료
3:56 휴식 시작
3:59 휴식 끝
4:04 1차 구현 완료
4:13 디버깅(배열 초기화 누락 해결) 후 tc 확인 완료
4:17 코드 점검 완료
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def find_nearest_santa(santa_dic):  # 가장 가깝고, 탈락하지 않은 산타 좌표 return

    dist_lst = []  # (거리, 행, 열)

    for id in range(1, santa_cnt + 1):
        si, sj, status, score = santa_dic[id]
        if not status: continue  # 탈락한 산타 -> skip

        dist = (si - ri) ** 2 + (sj - rj) ** 2  # 거리
        dist_lst.append((dist, si, sj))

    dist_lst.sort(key=lambda x: (x[0], -x[1], -x[2]))

    return dist_lst[0][1:]


def throw_santa(id, d, s, k):  # k턴에 id 산타를 d 방향으로 s만큼 던짐 (산타: s점 획득 후 기절)
    si, sj, status, score = santa_dic[id]
    santa_arr[si][sj] = 0
    score += s  # 점수 획득
    ni, nj = si + di[d] * s, sj + dj[d] * s  # 날아간 곳

    if OOB(ni, nj):  # 탈락
        ni, nj, status = -1, -1, 0
    else:
        if santa_arr[ni][nj]:  # 이동 칸에 산타 -> 상호작용!!!
            move_santa(santa_arr[ni][nj], d)
        santa_arr[ni][nj] = id
        status = -k  # k턴에 기절 표시

    santa_dic[id] = ni, nj, status, score

    return


def move_santa(id, d):  # id 산타를 d 방향으로 1칸 이동
    si, sj, status, score = santa_dic[id]
    santa_arr[si][sj] = 0
    ni, nj = si + di[d], sj + dj[d]

    if OOB(ni, nj):  # 탈락
        ni, nj, status = -1, -1, 0
    else:
        if santa_arr[ni][nj]:  # 이동 칸에 산타 -> 상호작용!!!
            move_santa(santa_arr[ni][nj], d)
        santa_arr[ni][nj] = id

    santa_dic[id] = ni, nj, status, score

    return


def find_shortcut(si, sj, ei, ej, is_s):  # si, sj 에서 ei, ej로 가장 가까워지는 방향 return / is_s: True 산타 False 루돌프
    if is_s:  # 산타 4방향
        dlst = [0, 2, 4, 6]
    else:  # 루돌프 8방향
        dlst = list(range(8))

    nd = -1  # 다음 방향
    mn_dist = (ei - si) ** 2 + (ej - sj) ** 2  # 최소 거리

    for d in dlst:  # 가장 가까워지는 방향 찾기
        ni, nj = si + di[d], sj + dj[d]
        if is_s and (OOB(ni, nj) or santa_arr[ni][nj]): continue  # 산타 조건

        dist = (ei - ni) ** 2 + (ej - nj) ** 2

        if dist < mn_dist:
            nd = d
            mn_dist = dist

    return nd


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, K, santa_cnt, C, D = map(int, input().split())
ri, rj = map(int, input().split())
ri, rj = ri - 1, rj - 1
santa_dic = dict()
santa_arr = [[0] * N for _ in range(N)]
for _ in range(santa_cnt):
    id, i, j = map(int, input().split())
    i, j = i - 1, j - 1
    santa_dic[id] = (i, j, 1, 0)  # 좌표, 상태(-k: -기절 시점, 0: 탈락, 1: 정상), 점수
    santa_arr[i][j] = id

for k in range(1, K + 1):

    # 루돌프 이동
    si, sj = find_nearest_santa(santa_dic)  # 가장 가까운 산타 찾기

    nd = find_shortcut(ri, rj, si, sj, False)  # 다음 방향

    ri, rj = ri + di[nd], rj + dj[nd]  # 이동

    # 이동 칸에 산타 있으면 -> 충돌!!!
    if santa_arr[ri][rj]:
        throw_santa(santa_arr[ri][rj], nd, C, k)

    # 산타 이동
    for id in range(1, santa_cnt + 1):
        si, sj, status, score = santa_dic[id]
        if status <= 0: continue  # 기절, 탈락 -> skip

        nd = find_shortcut(si, sj, ri, rj, True)
        if nd < 0: continue  # 이동 불가

        santa_arr[si][sj] = 0
        si, sj = si + di[nd], sj + dj[nd]  # 이동
        santa_arr[si][sj] = id
        santa_dic[id] = si, sj, status, score

        # 이동 칸에 루돌프 있으면 -> 충돌!!!
        if si == ri and sj == rj:
            throw_santa(id, (nd + 4) % 8, D, k)

    cnt = 0  # 남은 산타의 수

    # 탈락하지 않은 산타 점수 획득 + 2턴 전 기절 깨어남
    for id in range(1, santa_cnt + 1):
        si, sj, status, score = santa_dic[id]
        if not status: continue  # 탈락한 산타 -> skip

        if status == -(k - 1):  # 이전 턴 기절 풀림
            status = 1
        cnt += 1
        santa_dic[id] = si, sj, status, score + 1

    if not cnt: break  # 모든 산타 탈락

ans = [santa_dic[id][-1] for id in range(1, santa_cnt + 1)]
print(*ans)
