'''
4008. [모의 SW 역량테스트] 숫자 만들기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH

선표는 게임을 통해 사칙 연산을 공부하고 있다.

N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기로 했다.

수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다.

예를 들어 1, 2, 3 이 적힌 게임 판에 +와 x를 넣어 1 + 2 * 3을 만들면 1 + 2를 먼저 계산하고 그 뒤에 * 를 계산한다.

즉 1+2*3의 결과는 9이다.



주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오.
'''


import sys
sys.stdin = open('s_input (3).txt', 'r')


def dfs(n, s):
    global mn, mx
    if n == N:
        mx = max(s, mx)
        mn = min(s, mn)
        return
    for i in range(4):
        if v[i] < eq[i]:
            v[i] += 1
            if i == 0:
                tmp = s + lst[n]
            elif i == 1:
                tmp = s - lst[n]
            elif i == 2:
                tmp = s * lst[n]
            elif i == 3:
                tmp = int(s/lst[n])
            dfs(n+1, tmp)
            v[i] -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    eq = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    v = [0] * 4
    mx = -100000000
    mn = 100000000
    dfs(1, lst[0])
    print(f'#{tc}', mx - mn)
