"""
구간합

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
"""

import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mn = 10000*100
    mx = 0
    for i in range(N-M+1):
        sumnum = 0
        for j in range(M):
            sumnum += lst[i+j]
        if sumnum > mx :
            mx = sumnum
        if sumnum < mn:
            mn = sumnum
    ans = mx - mn
    print(f"#{case} {ans}")

