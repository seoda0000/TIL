'''
1224. [S/W 문제해결 기본] 6일차 - 계산기3 D4
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+(4+5)*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"345+6*+7+"

변환된 식을 계산하면 64를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
'''


import sys
sys.stdin = open('input.txt', 'r')

def calc():                     # 연산 함수
    eq = stk.pop()              # 연산자를 stk에서 빼고
    op2 = stknum.pop()          # 숫자 두개를 stknum에서 빼고
    op1 = stknum.pop()
    if eq == '+':               # 연산하고 다시 stknum에 push
        stknum.append(op1 + op2)
    elif eq == '*':
        stknum.append(op1 * op2)

for tc in range(1, 11):
    N = int(input())
    st = input()
    stk = []        # 연산자 스택
    stknum = []     # 숫자 스택
    dic_before = {'+':1, '*':2, '(':3}  # stk에 들어가기 전 연산자 우선순위
    dic_after = {'+':1, '*':2, '(':0}   # stk에 들어간 후 연산자 우선순위

    for ch in st:
        if ch.isdigit():                # 숫자일 경우 stknum에 push
            stknum.append(int(ch))
        else:
            if ch == ')':               # )일 경우 (를 만날 때까지 차례대로 연산
                while stk[-1] != '(':
                    calc()
                stk.pop()               # ( 버리기
            else:
                while stk and dic_after[stk[-1]] > dic_before[ch]:  # 자기보다 높은 우선순위 연산자 빼서 연산
                    calc()
                stk.append(ch)  # 자기보다 높은 우선순위가 없을 경우 push
    ans = stknum[0]
    print(f'#{tc}', ans)


