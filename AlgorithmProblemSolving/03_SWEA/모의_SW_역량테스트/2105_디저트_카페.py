'''
2105. [모의 SW 역량테스트] 디저트 카페
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu


친구들과 디저트 카페 투어를 할 계획이다.

한 변의 길이가 N인 정사각형 모양을 가진 지역에 디저트 카페가 모여 있다.

원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트의 종류를 의미하고

카페들 사이에는 대각선 방향으로 움직일 수 있는 길들이 있다.

디저트 카페 투어는 어느 한 카페에서 출발하여

대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.

디저트 카페 투어를 하는 도중 해당 지역을 벗어나면 안 된다.

또한, 친구들은 같은 종류의 디저트를 다시 먹는 것을 싫어한다.

즉, 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 된다.

친구들과 디저트를 되도록 많이 먹으려고 한다.

디저트 가게가 모여있는 지역의 한 변의 길이 N과 디저트 카페의 디저트 종류가 입력으로 주어질 때,

임의의 한 카페에서 출발하여 대각선 방향으로 움직이고

서로 다른 디저트를 먹으면서 사각형 모양을 그리며 다시 출발점으로 돌아오는 경우,

디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 정답으로 출력하는 프로그램을 작성하라.

만약, 디저트를 먹을 수 없는 경우 -1을 출력한다.
'''


import sys
sys.stdin = open('s.txt', 'r')

dr = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
def f(si, sj, ci, cj, lst, d):
    global ans
    if ci == si+1 and cj == sj-1 and len(lst) > 1 and d == 3:
        if ans < len(lst):
            ans = len(lst)
        return

    a, b = dr[d]
    if 0<=ci+a<N and 0<=cj+b<N and arr[ci+a][cj+b] not in lst:
        f(si, sj, ci + a, cj + b, lst+[arr[ci+a][cj+b]], (d + 1) % 4)
        if cj + b != N - 1 and ci + a != N - 1:
            f(si, sj, ci+a, cj+b, lst+[arr[ci+a][cj+b]], d)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N-2):
        for j in range(1, N-1):
            f(i, j, i, j, [arr[i][j]], 0)

    print(f'#{tc}', ans)