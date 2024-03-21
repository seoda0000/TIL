"""
https://www.acmicpc.net/problem/1018
백준 실버4 1018 체스판 다시 칠하기

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""

N, M = map(int, input().split())
board = [input() for _ in range(N)]
check = [[0] * (M - 7) for _ in range(N)]
row = 'BWBWBWBW'
ans = 64

for i in range(N):
    for j in range(M - 7):
        rowCnt = 0  # 시작점 (i, j)로부터 가로 8개의 새로 칠해야 할 수
        for n in range(8):
            if board[i][j + n] == row[n]:
                rowCnt += 1
        check[i][j] = rowCnt

for i in range(N - 7):
    for j in range(M - 7):
        allCnt = 32  # 시작점 (i, j)로부터 가로세로 64개의 새로 칠해야 할 수
        for n in range(0, 8, 2):
            allCnt += check[i + n][j] - check[i + n + 1][j]
        ans = min(ans, 64 - allCnt, allCnt)

print(ans)
