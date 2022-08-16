'''
1211. [S/W 문제해결 기본] 2일차 - Ladder2
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 최단거리로 바닥에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 모든 출발점을 검사하여 바닥까지 가장 짧은 이동 거리를 갖는 시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드를 작성하라.
(‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다.)

'''

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 양 옆 0으로 감싸기

    mn = 100*100 # 초기 최소거리 설정

    for i in range(1, 102):

        x = i
        if arr[0][x]: # 만약 첫줄이 1이면 시작
            y = r = 0  # 열좌표, 이동거리
            while y <= 99: # 인덱스 99까지 진행
                if arr[y][x-1]: # 왼쪽에 길이 있으면 진입
                    x -= 1 # 왼쪽으로 이동
                    r += 1 # 이동거리 증가
                    while arr[y][x-1]: # 더이상 왼쪽에 길이 없을 때까지
                        x -= 1 # 왼쪽으로 이동
                        r += 1 # 이동거리 증가

                elif arr[y][x+1]: # 오른쪽에 길이 있으면 진입
                    x += 1 # 오른쪽으로 이동
                    r += 1 # 이동거리 증가
                    while arr[y][x+1]: # 더이상 오른쪽에 길이 없을 때까지
                        x += 1 # 오른쪽으로 이동
                        r += 1 # 이동거리 증가
                y += 1 # 양옆에 길이 없다면 아래로 이동
                r += 1 # 이동거리 증가
            if mn > r > 0: # 최소거리 갱신
                mn = r
                mnIdx = i # 최소거리 인덱스 갱신
    print(f'#{tc}', mnIdx-1) # 0으로 둘러쌌으니 인덱스에서 1 빼기