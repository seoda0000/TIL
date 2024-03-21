'''
문자열 집합
https://www.acmicpc.net/problem/14425
14425 실버3
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
lst = [input() for _ in range(N)]
ans = 0
for _ in range(M):
    m = input()
    if m in lst:
        ans += 1
print(ans)
