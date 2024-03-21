'''
N과 M(4)
백준 실버3 15652
https://www.acmicpc.net/problem/15652
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

'''

N, M = map(int, input().split())
arr = [0] * M

def f(i, M):
    if i == M:
        print(*arr)
        return
    else:
        for n in range(1, N+1):
            if i == 0 or arr[i-1] <= n:
                arr[i] = n
                f(i+1, M)
                arr[i] = 0
f(0, M)