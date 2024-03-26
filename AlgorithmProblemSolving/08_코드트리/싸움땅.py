"""
9:01 시작
9:15 구상 완료
9:41 1차 구현 완료
9:43 tc3 오류 확인
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def check_gun(i, j, gun):  # i, j의 총 확인 후 가장 쎈 총 return + 나머지 총 바닥에 두기
    if not guns[i][j]: return gun
    new_gun = max(guns[i][j])

    if new_gun > gun:
        guns[i][j].remove(new_gun)
        if gun: guns[i][j].append(gun)
        return new_gun
    else:
        return gun


def fight(id1, id2):  # 싸우고 승자, 패자 return + score 계산
    _, _, _, s1, g1 = player_dic[id1]
    _, _, _, s2, g2 = player_dic[id2]
    res = sorted([(s1 + g1, s1, id1), (s2 + g2, s2, id2)], reverse=True)
    winner = res[0][2]
    loser = res[-1][2]
    scores[winner] += res[0][0] - res[-1][0]
    return winner, loser


def make_int_lst(i):
    if i == '0':
        return []
    else:
        return [int(i)]


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, player_cnt, K = map(int, input().split())
guns = [list(map(make_int_lst, input().split())) for _ in range(N)]
field = [[0] * N for _ in range(N)]
player_dic = dict()  # id: (i, j, 방향, 능력치, 총기)
for id in range(1, player_cnt + 1):
    x, y, d, s = map(int, input().split())
    player_dic[id] = (x - 1, y - 1, d, s, 0)
    field[x - 1][y - 1] = id

scores = [0] * (player_cnt + 1)

for _ in range(K):
    for id in range(1, player_cnt + 1):
        ci, cj, cd, cs, cg = player_dic[id]

        # 이동
        ni, nj = ci + di[cd], cj + dj[cd]
        if OOB(ni, nj):
            cd = (cd + 2) % 4
            ni, nj = ci + di[cd], cj + dj[cd]

        field[ci][cj] = 0
        enemy = field[ni][nj]
        if not enemy:  # 이동한 칸에 플레이어가 없다면
            # 총 확인
            cg = check_gun(ni, nj, cg)
            player_dic[id] = (ni, nj, cd, cs, cg)
            field[ni][nj] = id
        else:  # 이동한 칸에 플레이어가 있다면
            player_dic[id] = (ni, nj, cd, cs, cg)

            # 싸운다
            winner, loser = fight(id, enemy)

            # 패배자
            _, _, ld, ls, lg = player_dic[loser]

            # 총 내려두고 한칸 이동
            if lg: guns[ni][nj].append(lg)

            nni, nnj = ni + di[ld], nj + dj[ld]
            while OOB(nni, nnj) or field[nni][nnj]:
                ld = (ld + 1) % 4
                nni, nnj = ni + di[ld], nj + dj[ld]
            lg = check_gun(nni, nnj, 0)
            player_dic[loser] = (nni, nnj, ld, ls, lg)
            field[nni][nnj] = loser

            # 승리자
            _, _, wd, ws, wg = player_dic[winner]
            wg = check_gun(ni, nj, wg)
            player_dic[winner] = (ni, nj, wd, ws, wg)
            field[ni][nj] = winner

print(*scores[1:])
