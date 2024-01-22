"""
https://www.acmicpc.net/problem/11403
백준 실버1 경로찾기
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[i][k] > 0 and arr[k][j] > 0:
                arr[i][j] = 1
for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[i][k] > 0 and arr[k][j] > 0:
                arr[i][j] = 1
for n in range(N):
    print(*arr[n])

# ===============================================

def bfs(start):
    q = [start]
    while q:
        mid = q.pop(0)
        for i in range(N):
            if arr[mid][i] and ans[start][i] == 0:
                q.append(i)
                ans[start][i] = 1


    return
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]

for i in range(N):
    bfs(i)

for n in range(N):
    print(*ans[n])