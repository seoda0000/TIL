"""
실행시간: 195 -> 193
풀이시간: 58분 -> 53분

클래스 구현을 한번 해보고 싶어서 구현해보았다.
코딩은 훨씬 재밌지만, 구현이 오래 걸린다... (빨리 하려고 해도 괜히 멋있게 짜고 싶어서 이것저것 추가된다. lt처럼)
알고리즘은 4시간동안만 쓸 코드니까 굳이 객체 지향 할 필요 없다.
게다가 내장 메서드와 변수, 메인 변수를 어떻게 다룰지 컨벤션이 없어서 혼자 망설이게 된다....!!
실전에서는 그냥 딕셔너리로 승부 보자...개발이 아니라 문제를 풀자.
"""

"""
3:02 시작
3:07 구상 완료
3:55 1차 구현 및 디버깅 완료
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


class Player:
    def __init__(self, id, i, j, d, ability, gun=0):
        self.id = id
        self.i = i
        self.j = j
        self.d = d
        self.ability = ability
        self.gun = gun

    def __lt__(self, other):
        if self.ability + self.gun != other.ability + other.gun:
            return self.ability + self.gun < other.ability + other.gun
        return self.ability < other.ability

    def __str__(self):
        return f'능력치 {self.ability, self.gun} 위치 {self.i, self.j}'

    def swap_gun(self):
        i, j, gun = self.i, self.j, self.gun
        if not guns[i][j]: return
        mx = max(guns[i][j])
        if mx > gun:
            guns[i][j].remove(mx)
            if gun != 0:
                guns[i][j].append(gun)
            self.gun = mx
        return

    def drop_gun(self):
        if self.gun != 0:
            guns[self.i][self.j].append(self.gun)
        self.gun = 0
        return

    def move(self):
        ci, cj, d = self.i, self.j, self.d
        field[ci][cj] = 0
        ni, nj = ci + di[d], cj + dj[d]
        if OOB(ni, nj):
            d = (d + 2) % 4
            ni, nj = ci + di[d], cj + dj[d]
        self.i, self.j, self.d = ni, nj, d
        return ni, nj

    def run(self):
        self.drop_gun()
        ci, cj, d = self.i, self.j, self.d
        for _ in range(8):
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj) or field[ni][nj]:
                d = (d + 1) % 4
                continue
            self.i, self.j, self.d = ni, nj, d
            field[ni][nj] = self.id
            self.swap_gun()
            return


def fight(p1: Player, p2: Player):
    if p1 > p2: return p1, p2
    return p2, p1


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, player_cnt, round_cnt = map(int, input().split())
guns = [[list() for _ in range(N)] for _ in range(N)]
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(N):
        if ipt[j] > 0:  # 총이 있다
            guns[i][j].append(ipt[j])
field = [[0] * N for _ in range(N)]
players = [Player(0, -1, -1, -1, -1)]
for id in range(1, player_cnt + 1):
    x, y, d, s = map(int, input().split())
    players.append(Player(id, x - 1, y - 1, d, s))
    field[x - 1][y - 1] = id
points = [0] * (1 + player_cnt)
for _ in range(round_cnt):
    for id in range(1, player_cnt + 1):
        player = players[id]
        ni, nj = player.move()

        if field[ni][nj]:  # 플레이어가 있다
            other = players[field[ni][nj]]
            winner, loser = fight(player, other)

            points[winner.id] += abs(winner.ability + winner.gun - loser.ability - loser.gun)
            loser.run()
            winner.swap_gun()

            field[ni][nj] = winner.id

        else:
            player.swap_gun()
            field[ni][nj] = id

print(*points[1:])

"""
9:01 시작
9:15 구상 완료
9:41 1차 구현 완료
9:43 tc3 오류 확인
9:57 코드 정리 후 오류 발견
9:59 제출


<실수한 부분>
총들이라고 적혀 있는 게 수상했지만 먼저 생각해둔 논리상 한 칸에 총 하나만 있어서 무시했다.
그러나 총이 두개 있을 수도 있다... (tc에도 있었는데! 구현 전에 tc를 한번 쭉 확인하자)

코드를 깔끔하게 한답시고 중복 로직을 합쳤는데, 순서대로 이루어져야 하는 로직이라 갑자기 오류가 나기 시작했다.
코드 정리 시에는 로직에 유의하자! 숏코딩은 의미 없다. 무조건 직관적으로 짜자
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
