'''
4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth D2
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.

3 4 + .

Forth에서는 동작은 다음과 같다.

    숫자는 스택에 넣는다.
    연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
    ‘.’은 스택에서 숫자를 꺼내 출력한다.

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
'''


import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    st = input().split()
    stk = []
    for ch in st:
        if ch.isdigit():        # 숫자일 경우 stk에 push
            stk.append(int(ch))
        elif ch == '.':         # .일 경우 ans로 꺼내고 break
            ans = stk.pop()
            break

        else:
            if len(stk)>=2:     # 스택에 수가 두개 이상 남아 있을 경우
                op2 = stk.pop() # 뒤부터 꺼내기
                op1 = stk.pop()

                if ch == '+':
                        eq = op1 + op2
                elif ch == '*':
                        eq = op1 * op2
                elif ch == '/':
                        eq = op1 // op2
                elif ch == '-':
                        eq = op1 - op2
                stk.append(eq)  # 연산 수행 후 다시 stk에 push

            else:               # 스택에 연산할 수가 없는 경우 error
                ans = 'error'
                break

    if stk:
        ans = 'error'

    print(f'#{tc}', ans)