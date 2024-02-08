"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT
"""

import sys

sys.stdin = open("input.txt", "r")


def makeBurger(nth, tSm, kSm):
    global ans

    if nth == N:
        if kSm <= L:
            ans = max(ans, tSm)
        return

    if kSm > L:
        return

    makeBurger(nth + 1, tSm, kSm)
    makeBurger(nth + 1, tSm + lst[nth][0], kSm + lst[nth][1])


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    makeBurger(0, 0, 0)
    print(f'#{test_case} {ans}')
