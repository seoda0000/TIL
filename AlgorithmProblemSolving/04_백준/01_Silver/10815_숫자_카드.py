"""
https://www.acmicpc.net/problem/10815
백준 실버5 10815 숫자 카드

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
"""
import sys

input = sys.stdin.readline

_ = int(input())
s = set(map(int, input().split()))
_ = int(input())
questions = list(map(int, input().split()))
ans = []

for q in questions:
    if q in s:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)

"""
이분 탐색
"""

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
_ = int(input())
questions = list(map(int, input().split()))
ans_lst = []

for q in questions:
    s, e = 0, N - 1
    ans = 0

    while s <= e:
        m = (s + e) // 2

        if lst[m] == q:
            ans = 1
            break
        elif lst[m] > q:
            e = m - 1
        else:
            s = m + 1
    ans_lst.append(ans)

print(*ans_lst)
