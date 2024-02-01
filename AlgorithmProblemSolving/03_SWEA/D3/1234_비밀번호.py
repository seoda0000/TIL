"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD
SWEA D3 1234 비밀번호
"""
T = 10
for test_case in range(1, T + 1):
    _, st = input().split()
    N = len(st)
    stk = []
    for n in range(N):
        if stk and stk[-1] == st[n]:
            stk.pop()
        else:
            stk.append(st[n])


    print(f'#{test_case} {"".join(stk)}')
