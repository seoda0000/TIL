import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    str = input()
    ans = 0
    for s in str:
        if ans < 0:
            print('NO')
            break
        if s == '(':
            ans += 1
        else:
            ans -= 1
    else:
        if ans == 0:
            print('YES')
        else:
            print('NO')
