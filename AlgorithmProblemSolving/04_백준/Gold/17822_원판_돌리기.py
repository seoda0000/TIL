"""
백준 골드3 17822
원판 돌리기
https://www.acmicpc.net/problem/17822

반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다. 각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다. 수의 위치는 다음을 만족한다.

(i, 1)은 (i, 2), (i, M)과 인접하다.
(i, M)은 (i, M-1), (i, 1)과 인접하다.
(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
(1, j)는 (2, j)와 인접하다.
(N, j)는 (N-1, j)와 인접하다.
(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)
아래 그림은 N = 3, M = 4인 경우이다.



원판의 회전은 독립적으로 이루어진다. 2번 원판을 회전했을 때, 나머지 원판은 회전하지 않는다. 원판을 회전시킬 때는 수의 위치를 기준으로 하며, 회전시킨 후의 수의 위치는 회전시키기 전과 일치해야 한다.

다음 그림은 원판을 회전시킨 예시이다.


1번 원판을 시계 방향으로 1칸 회전	2, 3번 원판을 반시계 방향으로 3칸 회전	1, 3번 원판을 시계 방향으로 2칸 회전
원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 xi, di, ki이다.

번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.

"""
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def spin(x, d, k):
    for n in range(N):
        if (n+1) % x == 0:
            for _ in range(k):
                if d:
                    num = numbers[n].popleft()
                    numbers[n].append(num)
                else:
                    num = numbers[n].pop()
                    numbers[n].appendleft(num)

def check(n, m, t):
    st.add((n, m))
    if n+1 < N and v[n+1][m] == 0 and numbers[n+1][m] == t:
        v[n+1][m] = 1
        check(n+1, m, t)
    if n-1 >= 0 and v[n-1][m] == 0 and numbers[n-1][m] == t:
        v[n-1][m] = 1
        check(n-1, m, t)
    if m+1 < M and v[n][m+1] == 0 and numbers[n][m+1] == t:
        v[n][m+1] = 1
        check(n, m+1, t)
    if m == M-1 and v[n][0] == 0 and numbers[n][0] == t:
        v[n][0] = 1
        check(n, 0, t)
    if  v[n][m-1] == 0 and numbers[n][m-1] == t:
        v[n][m-1] = 1
        check(n, m-1, t)

def noSameNumber():
    s = 0
    cnt = 0
    for n in range(N):
        for m in range(M):
            if numbers[n][m] != 0:
                s += numbers[n][m]
                cnt += 1
    if cnt == 0:
        return
    mean = s/cnt
    for n in range(N):
        for m in range(M):
            if numbers[n][m] != 0:
                if numbers[n][m] > mean:
                    numbers[n][m] -= 1
                elif numbers[n][m] < mean:
                    numbers[n][m] += 1


N, M, T = map(int, input().split())
numbers = [deque(list(map(int, input().split()))) for _ in range(N)]
rollings = [deque(list(map(int, input().split()))) for _ in range(T)]

for t in range(T):
    tx, td, tk = rollings[t]
    spin(tx, td, tk)
    visited = [[0] * M for _ in range(N)]
    f = False
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 0 and numbers[n][m]:
                st = set()
                v = [[0] * M for _ in range(N)]
                check(n, m, numbers[n][m])

                if len(st) > 1:
                    for s in list(st):
                        a, b = s
                        numbers[a][b] = 0
                        visited[a][b] = 1
                        f = True
    if not f:
        noSameNumber()

ans = 0
for n in range(N):
    for m in range(M):
        if numbers[n][m] != 0:
            ans += numbers[n][m]

print(ans)