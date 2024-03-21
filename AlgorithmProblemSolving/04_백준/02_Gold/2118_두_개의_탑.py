"""
https://www.acmicpc.net/problem/2118
백준 골드5 2118 두 개의 탑

1번부터 N번까지의 지점이 있다. 각각의 지점들은 차례로, 그리고 원형으로 연결되어 있다.
이 지점들 중 두 곳에 두 개의 탑을 세우려고 하는데, 두 탑의 거리가 최대가 되도록 만들려고 한다.

지점들이 원형으로 연결되어 있기 때문에, 두 지점 사이에는 시계방향과 반시계방향의 두 경로가 존재한다.
두 지점 사이의 거리를 잴 때에는, 이러한 값들 중에서 더 작은 값을 거리로 한다.

연결되어 있는 두 지점 사이의 거리가 주어졌을 때, 두 탑의 거리의 최댓값을 계산하는 프로그램을 작성하시오.
"""
import sys

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
all_sm = sum(lst)
target = all_sm // 2
s, e = 0, 1
ans = 0
sm = lst[s]
while s < e:
    ans = max(ans, min(sm, all_sm - sm))
    if e >= N:
        break
    if sm < target:
        sm += lst[e]
        e += 1
    elif sm > target:
        sm -= lst[s]
        s += 1
    else:
        ans = target
        break

print(ans)
