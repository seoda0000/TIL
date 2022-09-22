'''
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

'''


import sys
sys.stdin = open('s_input (1).txt', 'r')


def dfs(n, s, v):
    if v == N-1:
        ans.append(s + arr[n][0])
    for i in range(N):
        if i != n and not visited[i]:
            visited[i] = True
            dfs(i, s + arr[n][i], v+1)
            visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [True] + [False] * (N-1)
    ans = []
    dfs(0, 0, 0)
    answer = min(ans)

    print(f'#{tc}', answer)