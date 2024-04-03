import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


class Rabit:
    def __init__(self, id, dist, cnt=0, i=0, j=0):
        self.id = id
        self.dist = dist
        self.cnt = cnt
        self.i = i
        self.j = j

    def __str__(self):
        return f'id: {self.id} dist:{self.dist} ij: {self.i, self.j} cnt: {self.cnt}'

    def __lt__(self, other):

        if self.cnt != other.cnt:
            return self.cnt < other.cnt

        if (self.i + self.j) != (other.i + other.j):
            return (self.i + self.j) < (other.i + other.j)

        if self.i != other.i:
            return self.i < other.i

        if self.j != other.j:
            return self.j < other.j

        return self.id < other.id

    def jump(self, ni, nj):
        self.i = ni
        self.j = nj
        self.cnt += 1


def get_nij(ci, cj, ck, d):
    idx_i, idx_j = (ci + di[d] * ck) % (N * 2 - 2), (cj + dj[d] * ck) % (M * 2 - 2)
    ai, bi = divmod(idx_i, N)
    aj, bj = divmod(idx_j, M)
    ni, nj = bi, bj
    if ai: ni = N - 2 - bi
    if aj: nj = M - 2 - bj
    return ni, nj


# def pprint():
#     arr = [[0] * M for _ in range(N)]
#     for rb in q:
#         arr[rb.i][rb.j] = (rb.id, score[rb.id] + basic_score)
# 
#     for a in arr:
#         print(a)
#     print()
#     return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
Q = int(input())
q = []
l_dic = dict()  # id: L배 해주기
score = dict()  # id: 점수
basic_score = 0
for _ in range(Q):
    ipt = list(input().split())

    if ipt[0] == '100':  # 처음: 경주 시작 준비
        N, M, P = map(int, ipt[1:4])

        for x in range(4, len(ipt), 2):
            heapq.heappush(q, Rabit(int(ipt[x]), int(ipt[x + 1])))
            score[int(ipt[x])] = 0
            l_dic[int(ipt[x])] = 1

    elif ipt[0] == '200':  # 경주 진행
        K, S = map(int, ipt[1:3])

        candi = dict()
        for _ in range(K):
            rb = heapq.heappop(q)

            nij_lst = []

            rb.dist *= l_dic[rb.id]
            l_dic[rb.id] = 1

            ci, cj, ck = rb.i, rb.j, rb.dist
            for d in range(4):
                nij_lst.append(get_nij(ci, cj, ck, d))
            nij_lst.sort(key=lambda x: (-x[0] - x[1], -x[0], -x[1]))
            ni, nj = nij_lst[0]
            basic_score += (ni + nj + 2)
            score[rb.id] -= (ni + nj + 2)
            candi[rb.id] = (ni, nj)
            rb.jump(ni, nj)
            heapq.heappush(q, rb)

        sid = -1
        si, sj = -1, -1
        for rid, value in candi.items():
            ri, rj = value

            if ri + rj > si + sj:
                si, sj, sid = ri, rj, rid
            elif ri + rj == si + sj:
                if ri > si:
                    si, sj, sid = ri, rj, rid
                elif ri == si:
                    if rj > sj:
                        si, sj, sid = ri, rj, rid
                    elif rj == sj:
                        if rid > sid:
                            si, sj, sid = ri, rj, rid

        score[sid] += S

    elif ipt[0] == '300':  # 이동거리 변경
        pid_t, L = map(int, ipt[1:3])
        if L > 1:
            l_dic[pid_t] *= L

    else:  # 마지막: 최고의 토끼 선정
        print(max(score.values()) + basic_score)
