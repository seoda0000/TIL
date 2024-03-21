"""
https://www.acmicpc.net/problem/1629
자연수 A를 B번 곱한 수를 알고 싶다.
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
"""

import sys

a, b, c = map(int, sys.stdin.readline().split())


# 모듈러 정리 : (a*b)%c = (a%c * b%c) % c
def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return ((tmp * tmp) * a) % c


print(multi(a, b))
