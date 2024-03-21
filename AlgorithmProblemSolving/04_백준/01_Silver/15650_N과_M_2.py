'''
N과 M (2)
https://www.acmicpc.net/problem/15650
백준 실버3 15650

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
'''

N, M = map(int, input().split())
arr = [0] * M


def f(i, M):
    if i == M:
        print(*arr)
        return
    for m in range(1, N + 1):
        if m not in arr and (i == 0 or arr[i - 1] < m):
            arr[i] = m
            f(i + 1, M)
            arr[i] = 0


f(0, M)

"""
다른 풀이
"""


def printNums(nth, lst):
    if nth == M:
        print(*lst[1:])
        return
    for n in range(lst[-1] + 1, N + 1):
        printNums(nth + 1, lst + [n])


N, M = map(int, input().split())
printNums(0, [0])
