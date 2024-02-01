"""
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
SWEA D2 4866 괄호검사
"""

T = int(input())
for test_case in range(1, T + 1):
    code = input()
    stk = []
    ans = 1

    for c in code:
        if c == '(' or c == '{':
            stk.append(c)
        elif c == ')':
            if stk:
                if stk.pop() != '(':
                    ans = 0
            else:
                ans = 0
        elif c == '}':
            if stk:
                if stk.pop() != '{':
                    ans = 0
            else:
                ans = 0
    if stk:
        ans = 0
    print(f'#{test_case} {ans}')
