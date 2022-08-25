'''
1226. [S/W 문제해결 기본] 7일차 - 미로1 D4
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.
'''


import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    _ = input()
    arr = [list(map(int, list(input()))) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si, sj = i, j   # 출발지점 좌표
            elif arr[i][j] == 3:
                ei, ej = i, j   # 도착지점 좌표
    q = [(si, sj)]              # 출발지점 q에 넣기
    visited = [[0]*16 for _ in range(16)]
    ans = 0

    while q:
        i, j = q.pop(0)         # dequeue
        visited[i][j] = 1       # 방문 기록
        if i == ei and j == ej: # 도착지점이면 break
            ans = 1
            break

        for a, b in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # 상하좌우 탐색
            ni, nj = i+a, j+b
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))   # 범위 내이고, 이동 가능하고, 아직 방문하지 않은 곳일 경우 enqueue
    print(f'#{tc}', ans)
