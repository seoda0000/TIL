'''
4615. 재미있는 오셀로 게임 D3
https://swexpertacademy.com/main/code/problem/problemDetail.do

오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.

보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).

4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.

그리고 흑, 백이 번갈아가며 돌을 놓는다.

플레이어는 빈공간에 돌을 놓을 수 있다.

단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
(여기에서 "사이"란 가로/세로/대각선을 의미한다.)

이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.

만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.

보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.
'''

import sys
sys.stdin = open('sample_input(1).txt', 'r')


def f1(ii, jj, cc):
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        ni = ii + a
        nj = jj + b
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == cc%2+1:
            f2(ii, jj, cc, a, b)

def f2(ii, jj, cc, a, b):
    na, nb = a, b
    while 0<=ii+na<N and 0<=jj+nb<N and arr[ii+na][jj+nb] == cc%2+1:
        na += a
        nb += b
    if not (0<=ii+na<N and 0<=jj+nb<N) or arr[ii+na][jj+nb] == 0:
        return
    elif arr[ii+na][jj+nb] == cc:
        ta, tb = a, b
        while ta != na+a or tb != nb+b:
            arr[ii+ta][jj+tb] = cc
            ta += a
            tb += b



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] =1
    arr[N//2][N//2] =2

    for _ in range(M):
        j, i, c = map(int, input().split())
        arr[i-1][j-1] = c
        f1(i-1, j-1, c)
    tmp1 = tmp2 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                tmp1 += 1
            elif arr[i][j] == 2:
                tmp2 += 1
    print(f'#{tc}', tmp1, tmp2)

