"""
https://www.acmicpc.net/problem/12015
백준 골드2 12015 가장 긴 증가하는 부분 수열 2

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
"""

from collections import defaultdict
import sys

input = sys.stdin.readline


def find_where(target):
    if not ans: return -1
    s, e = 0, len(ans) - 1
    idx = -1
    while s <= e:
        m = (s + e) // 2

        if ans[m] == target:
            idx = m
            break
        elif ans[m] < target:
            s = m + 1
        else:
            idx = m
            e = m - 1
    return idx


N = int(input())
lst = list(map(int, input().split()))
ans = []

for l in lst:
    idx = find_where(l)
    if idx == -1:
        ans.append(l)
    else:
        ans[idx] = l
print(len(ans))
