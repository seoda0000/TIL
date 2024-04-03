import heapq


class Rabit:
    def __init__(self, id, dist, cnt=0, i=0, j=0):
        self.id = id
        self.dist = dist
        self.cnt = cnt
        self.i = i
        self.j = j

    def __lt__(self, other):  # 작다
        return (self.cnt, self.i + self.j, self.i, self.j) < (other.cnt, other.i + other.j, other.i, other.j)


def get_nij(ci, cj, ck):
    ni, nj = ci + di[d] * ck, cj + dj[d] * ck
    if ni < 0:
        ni = 0
        nd = (d + 2) % 4
        ni, nj = ni + di[nd], nj + dj[nd]
    elif ni >= N:
        ni = N - 1
        nd = (d + 2) % 4
        ni, nj = ni + di[nd], nj + dj[nd]
    elif nj < 0:
        nj = 0
        nd = (d + 2) % 4
        ni, nj = ni + di[nd], nj + dj[nd]
    elif nj >= M:
        nj = 0
        nd = (d + 2) % 4
        ni, nj = ni + di[nd], nj + dj[nd]
    return ni, nj


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
Q = int(input())
q = []
second_q = []
basic_score = 0
for _ in range(Q):
    ipt = list(map(int, input().split()))

    if ipt[0] == '100':  # 처음: 경주 시작 준비
        N, M, P = map(int, ipt[1:4])
        score = [0] * (P + 1)
        for x in range(4, 4 + P):
            heapq.heappush(q, Rabit(ipt[x], ipt[x + P]))

    elif ipt[0] == '200':  # 경주 진행
        K, S = map(int, ipt[1:3])

        for _ in range(K):
            rabbit = heapq.heappop(q)

            nij_lst = []
            ci, cj, ck = rabbit.i, rabbit.j, rabbit.dist
            for d in range(4):
                nij_lst.append(get_nij(ci, cj, ck))
            nij_lst.sort(key=lambda x: (-x[0] - x[1], -x[0], -x[1]))
            ni, nj = nij_lst[0]
            basic_score += (ni + nj)
            score[rabbit.id] -= (ni + nj)

            rabbit.cnt += 1
            rabbit.i = ni
            rabbit.j = nj
            second_q.append(rabbit)
            q.append(rabbit)

    elif ipt[0] == '300':  # 이동거리 변경
        pid_t, L = map(int, ipt[1:3])

    else:  # 마지막: 최고의 토끼 선정
        pass
