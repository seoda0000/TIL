'''
2819. 격자판의 숫자 이어 붙이기 D4
https://swexpertacademy.com/main/code/problem/problemDetail.do

4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.

격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서,
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.

이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.

격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.
'''


import sys
sys.stdin = open('sample_input (2).txt', 'r')


dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def f(ci, cj, s, nth):
    if nth == 7:
        ans.append(s)
        return
    for a, b in dr:
        ni, nj = ci+a, cj+b
        if 0<=ni<N and 0<=nj<N:
            f(ni, nj, s+arr[ci][cj], nth+1)

T = int(input())
N = 4
for tc in range(1, T+1):
    arr = [input().split() for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            f(i, j, arr[i][j], 0)

    print(f'#{tc}', len(set(ans)))