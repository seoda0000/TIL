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
    if ci == si + 1 and cj == sj - 1 and len(lst) > 1 and d == 3:
        if ans < len(lst):
            ans = len(lst)
        return

    a, b = dr[d]
    if 0 <= ci + a < N and 0 <= cj + b < N and arr[ci + a][cj + b] not in lst:
        f(si, sj, ci + a, cj + b, lst + [arr[ci + a][cj + b]], (d + 1) % 4)
        if cj + b != N - 1 and ci + a != N - 1:
            f(si, sj, ci + a, cj + b, lst + [arr[ci + a][cj + b]], d)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            f(i, j, i, j, [arr[i][j]], 0)

    print(f'#{tc}', ans)

"""
1년 후 풀이
"""

"""
9:14 시작
9:22 구상 완료
9:43 구현 완료

직사각형이 되려면 마주보는 면의 길이가 같아야 한다는 점,
그리고 어느 방향으로 돌아도 같은 직사각형인 점을 이용하여 각 변의 경우에 따라 분기하여 dfs로 풀었다.

다음 단계로 넘겨줄 때 모든 변이 아닌 직전의 꼭짓점만을 넘겨줘서 디버깅을 했다.

1년 전에는 직사각형이 만들어지든 말든 일단 현재 방향, 다음 방향으로 모두 보내버리고 마지막에 돌아왔는지만을 체크했다.
조건이 없어서 코드가 훨씬 짧다.
참고할만한 방법인 것 같다
"""

import sys

sys.stdin = open("input.txt", "r")


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


def draw(si, sj, num_lst, d, line_lst):  # 시작 좌표, 여태까집 방문한 디저트 가게의 종류 리스트, 현재 그릴 변의 방향, 변의 길이 리스트
    global ans
    ci, cj = si, sj

    if d == 0 or d == 1:  # 첫 두 변
        k = 0
        nums = []
        while True:
            k += 1
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj): return
            if arr[ni][nj] in num_lst or arr[ni][nj] in nums: return
            nums.append(arr[ni][nj])
            draw(ni, nj, num_lst + nums, d + 1, line_lst + [k])
            ci, cj = ni, nj
    elif d == 2 or d == 3:  # 다음 두 변
        k = line_lst[d - 2]
        if d == 3:
            k -= 1
        nums = []
        for _ in range(k):
            ni, nj = ci + di[d], cj + dj[d]
            if OOB(ni, nj): return
            if arr[ni][nj] in num_lst or arr[ni][nj] in nums: return
            nums.append(arr[ni][nj])
            ci, cj = ni, nj
        draw(ci, cj, num_lst + nums, d + 1, line_lst)
    else:  # 다 그림

        ans = max(ans, len(num_lst))
        return

    return


di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ans = -1

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for si in range(N - 2):
        for sj in range(1, N - 1):
            draw(si, sj, [arr[si][sj]], 0, [])
    print(f'#{test_case} {ans}')
