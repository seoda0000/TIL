"""
https://www.acmicpc.net/problem/11404
백준 골드4 11404 플로이드

n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
"""

N = int(input())
M = int(input())
CEILING = 100001 * M
arr = [[CEILING] * N for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    arr[a][b] = min(arr[a][b], c)

for k in range(N):
    for a in range(N):
        for b in range(N):
            if arr[a][b] > arr[a][k] + arr[k][b]:
                arr[a][b] = arr[a][k] + arr[k][b]

for a in arr:
    p = " ".join(map(str, a))
    print(p.replace(str(CEILING), '0'))
