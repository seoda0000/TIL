"""
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

SWEA D2 4873 반복문자 지우기
"""

T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []

    for s in st:
        if stk and stk[-1] == s:
            stk.pop()
        else:
            stk.append(s)
    print(f'#{test_case} {len(stk)}')
