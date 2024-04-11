"""
가장자리 padding 했으면 인덱스에 유의
문제 잘 읽기!!!!!!! 출력 조건 확인하자
4방향으로 분기하기보다 언제나 번거롭게 구현하는 게 오히려 빠르고 실수할 일도 없다. 머리 쓰지 말자.
"""
"""
3:35 시작
3:43 구상 완료
4:04 1차 구현 완료
4:14 디버깅 완료
4:17 검토 및 제출
"""


def mark(ki, kj, kh, kw, num):
    cnt = 0

    if num == 0:  # 지우기만 함
        for i in range(ki, ki + kh):
            for j in range(kj, kj + kw):
                knight_arr[i][j] = num
    else:  # 함정 세기도 필요
        for i in range(ki, ki + kh):
            for j in range(kj, kj + kw):
                if field[i][j] == 1: cnt += 1
                knight_arr[i][j] = num
    return cnt


def move(kid, is_ordered):
    ki, kj, kh, kw, kk = knight_dic[kid]

    mark(ki, kj, kh, kw, 0)  # 일단 지운다

    nki, nkj = ki + di[cd], kj + dj[cd]  # 다음 위치 찾기
    kcnt = mark(nki, nkj, kh, kw, kid)  # 표기하며 함정 세기

    if not is_ordered:
        damage[kid] += kcnt
        kk -= kcnt

        if kk <= 0:  # 사라져야 한다
            kk = 0
            mark(nki, nkj, kh, kw, 0)

    knight_dic[kid] = nki, nkj, kh, kw, kk

    return


def check_move(id, d):
    ki, kj, kh, kw, _ = knight_dic[id]
    ni, nj = ki + di[d], kj + dj[d]

    for i in range(ni, ni + kh):
        for j in range(nj, nj + kw):
            if field[i][j] == 2:
                return False
            elif knight_arr[i][j] == id:
                continue  # 자기 영역
            elif knight_arr[i][j]:  # 다른 기사 존재
                if knight_arr[i][j] in pushed_knights: continue
                if not check_move(knight_arr[i][j], d):
                    return False
    # 무사히 확인 완료
    pushed_knights.append(id)
    return True


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, P, Q = map(int, input().split())
N += 2
field = [[2] * N] \
        + [[2] + list(map(int, input().split())) + [2] for _ in range(N - 2)] \
        + [[2] * N]  # 0 빈칸 1 함정 2 벽
knight_dic = dict()
knight_arr = [[0] * N for _ in range(N)]
damage = [0] * (P + 1)
for id in range(1, P + 1):
    r, c, h, w, k = map(int, input().split())
    knight_dic[id] = r, c, h, w, k
    for i in range(r, r + h):  # 판에 표기
        for j in range(c, c + w):
            knight_arr[i][j] = id
orders = [list(map(int, input().split())) for _ in range(Q)]
for cid, cd in orders:
    if knight_dic[cid][-1] <= 0: continue  # 사라진 기사

    pushed_knights = []
    if not check_move(cid, cd): continue  # 이동 불가

    for kid in pushed_knights[:-1]:
        move(kid, False)
    move(cid, True)

ans = 0

for id, values in knight_dic.items():
    if values[-1] <= 0: continue
    ans += damage[id]
print(ans)

"""
9:00 시작
9:12 구상 완료
9:45 구현 완료
9:55 디버깅(return 시점 오류) 및 tc 확인
10:00 코드 점검 및 출력 중 이동 로직 오류 확인
10:13 틀렸습니다 확인 후 휴식
10:15 휴식 끝, 확인 로직 중복 제거(상하)
10:18 확인 로직 중복 제거(좌우)
"""


def OOB(i, j):
    return not (0 <= i < L and 0 <= j < L)


def check_order(id, d):  # id 기사가 d 방향으로 움직일 수 있는지 여부 return + 움직일 수 있는 기사 리스트 추가
    si, sj, h, w, _, _ = knight_dic[id]

    if d % 2 == 0:  # 상하
        if d == 0:
            ci = si - 1  # 체크할 행
        else:
            ci = si + h

        for j in range(sj, sj + w):
            if OOB(ci, j): return False  # 범위 밖
            if board[ci][j] == 2: return False  # 벽
            if knight_arr[ci][j]:  # 다른 기사
                other_id = knight_arr[ci][j]
                if other_id not in cur_knights and not check_order(other_id, d):  # 다른 기사가 이동 가능한지 확인
                    return False

    else:  # 좌우
        if d == 3:
            cj = sj - 1  # 체크할 열
        else:
            cj = sj + w

        for i in range(si, si + h):
            if OOB(i, cj): return False  # 범위 밖
            if board[i][cj] == 2: return False  # 벽
            if knight_arr[i][cj]:  # 다른 기사
                other_id = knight_arr[i][cj]
                if other_id not in cur_knights and not check_order(other_id, d):
                    return False

    cur_knights.append(id)
    return True


def move_knights(cur_knights: list, d: int):  # 기사들을 d 방향으로 이동

    for id in cur_knights:
        si, sj, h, w, k, p = knight_dic[id]

        if d % 2 == 0:  # 상하
            if d == 0:
                new_si = si - 1  # 새로운 첫 행
                ni = si - 1  # 새로 그릴 행
                xi = si + h - 1  # 지워질 행
            else:
                new_si = si + 1
                ni = si + h
                xi = si

            for j in range(sj, sj + w):
                knight_arr[ni][j] = id
                knight_arr[xi][j] = 0

            si = new_si

        else:  # 좌우
            if d == 3:
                new_sj = sj - 1  # 새로운 첫 열
                nj = sj - 1  # 새로 그릴 열
                xj = sj + w - 1  # 지워질 열
            else:
                new_sj = sj + 1  # 새로운 첫 열
                nj = sj + w
                xj = sj

            for i in range(si, si + h):
                knight_arr[i][nj] = id
                knight_arr[i][xj] = 0

            sj = new_sj

        knight_dic[id] = si, sj, h, w, k, p

    return


def calc_damage(damaged_knights):  # 기사들이 입은 대미지 계산
    global ans

    for id in damaged_knights:
        si, sj, h, w, k, p = knight_dic[id]

        damage = 0
        for i in range(si, si + h):  # 함정 세기
            for j in range(sj, sj + w):
                if board[i][j] == 1:
                    damage += 1

        k -= damage
        p += damage

        if k <= 0:  # 기사 사라짐
            for i in range(si, si + h):
                for j in range(sj, sj + w):
                    knight_arr[i][j] = 0
            k = 0

        knight_dic[id] = si, sj, h, w, k, p

    return


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
L, knight_cnt, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]  # 0 빈칸 1 함정 2 벽
knight_dic = dict()
knight_arr = [[0] * L for _ in range(L)]  # 기사 위치 id로 표시
for id in range(1, knight_cnt + 1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    knight_dic[id] = (r, c, h, w, k, 0)  # 좌표 i, j, 높이, 너비, 체력, 받은 데미지
    for i in range(r, r + h):
        for j in range(c, c + w):
            knight_arr[i][j] = id
orders = [list(map(int, input().split())) for _ in range(Q)]

for id, d in orders:

    if knight_dic[id][-2] == 0: continue  # 사라진 기사

    cur_knights = []  # 움직일 기사
    if check_order(id, d):  # 명령 수행 가능
        move_knights(cur_knights, d)
        cur_knights.remove(id)  # 공격자: 피해 안 입음
        calc_damage(cur_knights)

ans = 0
for _, _, _, _, k, p in knight_dic.values():
    if k > 0: ans += p
print(ans)
