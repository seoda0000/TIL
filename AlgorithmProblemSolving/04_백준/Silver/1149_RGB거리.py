"""
https://www.acmicpc.net/problem/1149
백준 1149 RGB거리
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for n in range(1, N):
    for i in range(3):
        if i == 0:
            arr[n][i] += min(arr[n - 1][1], arr[n - 1][2])
        elif i == 1:
            arr[n][i] += min(arr[n - 1][0], arr[n - 1][2])
        else:
            arr[n][i] += min(arr[n - 1][0], arr[n - 1][1])
print(min(arr[N - 1]))
