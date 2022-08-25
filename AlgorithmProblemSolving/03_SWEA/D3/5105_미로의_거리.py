'''
 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3
 https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

 NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.
'''

import sys
sys.stdin = open('s_input.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j
    q = [(si, sj, -1)]          # 지나는 블록 기준이니까 시작 지점에서는 -1로 넣어줘야 한다.

    while q:
        i, j, k = q.pop(0)
        visited[i][j] = 1
        if i == ei and j == ej:
            ans = k
            break
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + a, j + b
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj, k + 1))   # 지나는 블록이 하나 추가된다.

    print(f'#{tc}', ans)

