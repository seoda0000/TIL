'''
N-Queen
https://www.acmicpc.net/problem/9663
백준 골드4 9663

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''

def f(i, j, n, N):          # (i, j)에 n번째 퀸을 놓았을 때 n+1번째 퀸의 자리 탐색
    global ans
    if n == N:              # N개의 퀸을 모두 놓은 경우
        ans += 1            # 횟수 세기
        return

    if 0 not in arr[-1]:    # 마지막 줄에 놓을 수 있는 자리가 없으면 바로 중단
        return

    for d in range(-j, N-j):
        ni, nj = i+1, j+d       # 다음 행 탐색
        if arr[ni][nj] == 0:    # 만약 퀸을 놓을 수 있으면
            note(ni, nj, 0, N, n+1)    # 퀸이 공격할 수 있는 자리 표시
            f(ni, nj, n+1, N)       # 퀸을 놓는다
            note(ni, nj, n+1, N, 0)    # 퀸이 공격할 수 있는 자리 clear

def note(i, j, p, N, k):           # p로 표시된 자리 중 (i, j)의 퀸이 공격할 수 있는 자리를 k로 표시하는 함수
    for a in range(i+1, N):
        for b in range(N):
            if (b == j or a-i == b-j or a-i == -b+j) and arr[a][b] == p:
                arr[a][b] = k

N = int(input())
arr = [[0]*N for _ in range(N)]
ans = 0

for y in range(0, N):   # 첫 행에서 시작
    note(0, y, 0, N, 1)        # 퀸이 공격할 수 있는 자리 표시
    f(0, y, 1, N)           # 퀸을 놓는다
    note(0, y, 1, N, 0)        # 퀸이 공격할 수 있는 자리 clear
print(ans)

