"""
https://www.acmicpc.net/problem/2749
백준 골드2 2749 피보나치 수 3

"""

"""
피사노 주기 참고
"""

N = int(input())
if N < 2:
    print(N)
else:

    M = 1000000
    cycle = (M // 10) * 15
    N %= cycle
    lst = [0] * (N + 1)
    lst[1] = 1
    for p in range(2, N + 1):
        lst[p] = (lst[p - 2] + lst[p - 1]) % M
    print(lst[N])
