'''
5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 D2
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
'''

import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = []
    for _ in range(E):
        a, b = map(int, input().split())    # 간선 각각 저장
        arr.append((a, b))
        arr.append((b, a))
    S, G = map(int, input().split())
    q = [(S, 0)]                            # (시작 도시, 지난 간선 수) q에 저장
    visited = [0] * (V+1)
    ans = 0

    while q:
        i, n = q.pop(0)                     # q에서 pop
        if i == G:                          # 만약 목표지점이면 n을 저장하고 break
            ans = n
            break
        if visited[i] == 1:                 # 만약 이미 간 곳이면 건너뜀
            continue
        visited[i] = 1
        n += 1
        for a in arr:                       # 간선 중 아직 가지 않은 도시 q에 넣기
            if a[0] == i and visited[a[1]] == 0:
                q.append((a[1], n))
    print(f'#{tc}', ans)
