"""
https://www.acmicpc.net/problem/3460
백준 브론즈3 3460 이진수

양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오.
최하위 비트(least significant bit, lsb)의 위치는 0이다.
"""

T = int(input())
for t in range(T):
    n = int(input())
    p = 0
    ans = []
    while n:
        if n % 2:
            ans.append(p)
        n //= 2
        p += 1
    print(*ans)
