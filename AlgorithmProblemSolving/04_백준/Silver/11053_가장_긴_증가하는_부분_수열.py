"""
https://www.acmicpc.net/problem/11053

백준 실버2 11053 가장 긴 증가하는 부분 수열

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
"""


N = int(input())
numbers = list(map(int, input().split()))
cnts = [1] * N

for n in range(1, N):
    cnt = 1
    for m in range(n):
        if numbers[m] < numbers[n]:
            cnt = max(cnts[m] + 1, cnt)
    cnts[n] = cnt
print(max(cnts))
