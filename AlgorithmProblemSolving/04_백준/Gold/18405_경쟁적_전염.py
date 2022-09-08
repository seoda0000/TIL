'''
경쟁적 전염
https://www.acmicpc.net/problem/18405
백준 골드5
NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다.
모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

'''




from collections import deque
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
q = []
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            q.append((arr[i][j], i, j, 0))  # 바이러스 번호, 행, 열, 발생한 시각
q.sort()
q = deque(q)
sec = 0
while q:
    bb, bi, bj, bs = q.popleft()
    if bs == S:  # 시각이 S초라면 종료
        break
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0<=bi+a<N and 0<=bj+b<N and arr[bi+a][bj+b] == 0:  # 빈칸이면
            arr[bi+a][bj+b] = bb                              # 바이러스 생성
            q.append((bb, bi+a, bj+b, bs+1))                  # q에 enqueue
print(arr[X-1][Y-1])

