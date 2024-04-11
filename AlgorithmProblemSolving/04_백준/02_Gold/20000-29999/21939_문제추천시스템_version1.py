'''
문제 추천 시스템 Version 1
https://www.acmicpc.net/problem/21939
백준 골드4 21939

tony9402는 최근 깃헙에 코딩테스트 대비 문제를 직접 뽑아서 "문제 번호, 난이도"로 정리해놨다.

깃헙을 이용하여 공부하시는 분들을 위해 새로운 기능을 추가해보려고 한다.

만들려고 하는 명령어는 총 3가지가 있다. 아래 표는 각 명령어에 대한 설명이다.

recommend $x$ 
 $x$가 1인 경우 추천 문제 리스트에서 가장 어려운 문제의 번호를 출력한다.

만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것으로 출력한다.

 $x$가 -1인 경우 추천 문제 리스트에서 가장 쉬운 문제의 번호를 출력한다.

만약 가장 쉬운 문제가 여러 개라면 문제 번호가 작은 것으로 출력한다.

add $P$ $L$ 	추천 문제 리스트에 난이도가 $L$인 문제 번호 $P$를 추가한다.
(추천 문제 리스트에 없는 문제 번호 $P$만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어 올 수 있다.)
solved $P$ 	추천 문제 리스트에서 문제 번호 $P$를 제거한다. (추천 문제 리스트에 있는 문제 번호 $P$만 입력으로 주어진다.)
명령어 recommend는 추천 문제 리스트에 문제가 하나 이상 있을 때만 주어진다.

명령어 solved는 추천 문제 리스트에 문제 번호가 하나 이상 있을 때만 주어진다.

위 명령어들을 수행하는 추천 시스템을 만들어보자.

'''

import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
prob_level = 1000000
pdic = {}
for _ in range(N):
    P, L = map(int, input().split())
    lpnum = L * prob_level + P
    pdic[P] = lpnum
M = int(input())
for _ in range(M):
    order_and_num = input().split()
    order = order_and_num[0]
    if order == 'add':
        P, L = int(order_and_num[1]), int(order_and_num[2])
        lpnum = L * prob_level + P
        pdic[P] = lpnum
    elif order == 'solved':
        P = int(order_and_num[1])
        solvedlst.append(pdic[P])
        del pdic[P]
    elif order == 'recommend':
        flag = int(order_and_num[1])
        if flag == 1:
            print(max(pdic.values()) % prob_level)
        else:
            print(min(pdic.values()) % prob_level)

