'''
N과 M (6)
https://www.acmicpc.net/problem/15655
백준 실버3 15655

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
'''

N, M = map(int, input().split())
nlst = list(map(int, input().split()))
nlst.sort()
arr = [0] * M
def f(i, M):
    if i == M:
        print(*arr)
        return
    else:
        for n in nlst:
            if n not in arr and (i == 0 or arr[i-1] < n):
                arr[i] = n
                f(i+1, M)
                arr[i] = 0
f(0, M)