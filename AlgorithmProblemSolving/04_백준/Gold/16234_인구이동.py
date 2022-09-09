'''
인구 이동
https://www.acmicpc.net/problem/16234
백준 골드5 16234

N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

'''

from collections import deque
import sys
sys.setrecursionlimit(10**5)  # 10**9는 Pypy는 메모리초과
def input():
    return sys.stdin.readline().rstrip()


def f(wi, wj, nsum, s, q):  # 현재 위치, 인구합, 국경 연 국가 set, 다음 후보 q
    global change_flag      # 변동이 생겼는지 확인하는 flag
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:  # 네 방향 탐색
        if 0<=wi+a<N and 0<=wj+b<N and L <= abs(arr[wi][wj]-arr[wi+a][wj+b]) <= R:
            if visited[wi+a][wj+b] == False:  # 아직 방문 안한 곳이라면 enqueue
                w = (wi+a, wj+b)
                q.append(w)
                s.add(w)
                nsum += arr[wi+a][wj+b]
                visited[wi+a][wj+b] = True
    if q:                      # 만약 q에 내용물이 있다면
        ni, nj = q.popleft()
        f(ni, nj, nsum, s, q)      # 다음 후보지로 이동
    else:                      # 없다면 탐색 종료
        newpop = nsum // len(s)    # 인구 이동
        for n in s:
            nx, ny = n
            if arr[nx][ny] != newpop:
                arr[nx][ny] = newpop
                change_flag = True  # 변동 체크


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


day = 0  # 지난 날짜
while True:
    change_flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                f(i, j, arr[i][j], {(i, j)}, deque([]))
    if change_flag == False:   # 만약 변동이 없다면 중지
        break
    day += 1

print(day)