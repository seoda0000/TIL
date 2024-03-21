'''
N과 M (12)
https://www.acmicpc.net/problem/15666
백준 실버2 15666

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
'''

N, M = map(int, input().split())
lst = list(set(map(int, input().split())))
lst.sort()
arr = [0] * M
def f(i, M):
    if i == M:
        print(*arr)
        return
    else:
        for n in lst:
            if i == 0 or n >= arr[i-1]:
                arr[i] = n
                f(i+1, M)
                arr[i] = 0
f(0, M)
