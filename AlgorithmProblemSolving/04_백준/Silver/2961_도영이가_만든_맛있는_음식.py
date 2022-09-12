'''
도영이가 만든 맛있는 음식
https://www.acmicpc.net/problem/2961
백준 실버2 2961

도영이는 짜파구리 요리사로 명성을 날렸었다. 이번에는 이전에 없었던 새로운 요리에 도전을 해보려고 한다.

지금 도영이의 앞에는 재료가 N개 있다. 도영이는 각 재료의 신맛 S와 쓴맛 B를 알고 있다.
여러 재료를 이용해서 요리할 때, 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.

시거나 쓴 음식을 좋아하는 사람은 많지 않다. 도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다.
또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.

재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.
'''
import sys


def input():
    return sys.stdin.readline().rstrip()


def dfs(n, S, B):
    global ans
    if n == N:              # 종료조건 : 전부 순회했을 때
        if S > 1 or B > 0:      # 만약 물이 아니라면
            if abs(S-B) < ans:  # ans 갱신
                ans = abs(S-B)
        return
    dfs(n+1, S, B)        # 해당 재료를 안 넣었을 때
    nS, nB = arr[n]
    dfs(n+1, S*nS, B+nB)  # 해당 재료를 넣었을 때


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
ans = 1000000000
dfs(0, 1, 0)   # 순서 초기값, 신맛(곱) 초기값, 쓴맛(합) 초기값
print(ans)
