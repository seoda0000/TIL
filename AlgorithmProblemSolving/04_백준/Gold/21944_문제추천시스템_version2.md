import sys
sys.stdin = open('input1.txt', 'r')
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


rank_prob = 1000000
N = int(input())
r1_dic = defaultdict(dict)  # recommend  : 우선순위 G > L > P     dic형식 {G:{LP:bool}}
r2_dic = defaultdict(dict)  # recommend2 : 우선순위 L > P         dic형식 {LP:bool}
r3_dic = defaultdict(dict)  # recommend3 : 우선순위 L > P > -1    dic형식 {L:{P:bool}}
problem_dict = dict()       # 전체 문제 dic : dic형식 {P:[L, G]}

for _ in range(N):
    P, L, G = map(int, input().split())
    calc_num = L * rank_prob + P    # LLLPPPPPP : 난이도와 문제 번호 합치기
    r1_dic[G][calc_num] = 1
    r2_dic[calc_num] = 1
    r3_dic[L][P] = 1
    problem_dict[P] = [L, G]

M = int(input())
for _ in range(M):
    command, *arg = input().split()

    if command == 'recommend':
        G, x = map(int, arg)
        if x > 0:
            calc_num = max(r1_dic[G].keys())    # G에 해당하는 가장 어려운 문제 (G에 해당하는 값중 -> L이 높고 -> P가 높은 것)
        else:
            calc_num = min(r1_dic[G].keys())    # G에 해당하는 가장 쉬운 문제 (G에 해당하는 값중 -> L이 낮고 -> P가 낮은 것)
        L = calc_num // rank_prob
        P = calc_num % rank_prob
        print(P)
    elif command == 'recommend2':
        x = int(arg[0])
        if x > 0:
            calc_num = max(r2_dic.keys())   # 가장 난이도가 높은 문제 중 문제 번호가 높은 것 (L이 크고 -> P가 큰 것)
        else:
            calc_num = min(r2_dic.keys())   # 가장 난이도가 낮은 문제 중 문제 번호가 낮은 것 (L이 낮고 -> P가 낮은 것)
        L = calc_num // rank_prob
        P = calc_num % rank_prob
        print(P)
    elif command == 'recommend3':
        x, target_L = map(int, arg)
        if x < 0:
            target_L = target_L - 1     # x가 -1인 경우 타겟 L보다 작아야 하므로 1을 빼준다.
        result = -1                     # 초기값 설정 (조건을 충족하는 문제가 없을 경우)
        while 0 <= target_L <= 100:
            if r3_dic.get(target_L):    # r3 dic에서 타겟 L 찾기
                if x > 0:
                    result = min(r3_dic[target_L].keys())   # 타겟 L보다 난이도가 같거나 어려운 문제 중 가장 쉬운 문제 (타겟 L보다 L이 같거나 크고 -> L이 작고 -> P가 낮은 것)
                else:
                    result = max(r3_dic[target_L].keys())   # 타겟 L보다 난이도가 쉬운 문제 중 가장 어려운 문제 (타겟 L보다 L이 작고 -> L이 크고 -> P가 높은 것)
                break
            target_L = target_L + x     # x가 양수인 경우 1을 더하고, x가 음수인 경우 1을 줄여야 한다.
        print(result)

    elif command == 'solved':
        P = int(arg[0])
        L, G = problem_dict[P]
        calc_num = L * rank_prob + P
        del r3_dic[L][P]            # 각 dic에서 값 제거
        del r2_dic[calc_num]
        del r1_dic[G][calc_num]
    else:
        P, L, G = map(int, arg)
        calc_num = L * rank_prob + P
        r1_dic[G][calc_num] = 1
        r2_dic[calc_num] = 1
        r3_dic[L][P] = 1
        problem_dict[P] = [L, G]