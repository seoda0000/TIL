"""
질량 합을 개수로 잘못 봐서 틀렸다.
"""

"""
9:27 시작
9:31 구상 완료
9:45 구현 완료
9:47 dic.items 디버깅
9:51 개수 -> 질량합 디버깅
"""
from collections import defaultdict

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
N, atom_cnt, K = map(int, input().split())
dic = defaultdict(list)  # (질량, 속력, 방향)

for _ in range(atom_cnt):
    x, y, m, s, d = map(int, input().split())
    dic[(x - 1, y - 1)].append((m, s, d))

for _ in range(K):

    # 모든 원자 동시 이동
    moved_dic = defaultdict(list)

    for key, values in dic.items():
        ci, cj = key

        for m, s, d in values:
            ni, nj = (ci + di[d] * s) % N, (cj + dj[d] * s) % N
            moved_dic[(ni, nj)].append((m, s, d))

    dic = moved_dic

    # 쪼개진다...
    dic_item_lst = list(dic.items())
    for key, values in dic_item_lst:
        if len(values) <= 1: continue
        sm_m = sm_s = 0
        d_set = set()

        for m, s, d in values:  # (질량, 속력, 방향)
            sm_m += m
            sm_s += s
            d_set.add(d % 2)
        nm = sm_m // 5  # 질량
        ns = sm_s // len(values)  # 속력

        if not nm:  # 소멸
            dic.pop(key)
            continue

        atom_lst = []
        if len(d_set) == 1:  # 상하좌우
            d_lst = [0, 2, 4, 6]
        else:
            d_lst = [1, 3, 5, 7]

        for d in d_lst:
            atom_lst.append((nm, ns, d))

        dic[key] = atom_lst

ans = 0
for values in dic.values():
    for value in values:
        ans += value[0]

print(ans)