"""
https://www.acmicpc.net/problem/2615
백준 실버1 2615 오목

오목은 바둑판에 검은 바둑알과 흰 바둑알을 교대로 놓아서 겨루는 게임이다.
바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데 가로줄은 위에서부터 아래로 1번, 2번, ... ,19번의 번호가 붙고
세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ... 19번의 번호가 붙는다.

위의 그림에서와 같이 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이기게 된다.
여기서 연속적이란 가로, 세로 또는 대각선 방향 모두를 뜻한다.
즉, 위의 그림은 검은색이 이긴 경우이다. 하지만 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.

입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지, 흰색이 이겼는지 또는 아직 승부가 결정되지 않았는지를 판단하는 프로그램을 작성하시오.
단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.

"""


def f(i, j, c):
    for d in range(4):

        cnt = 1
        h = 1

        while True:
            ni, nj = i + di[d] * h, j + dj[d] * h

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == c:
                cnt += 1
                h += 1
            else:
                break

        if cnt == 5:

            ni, nj = i - di[d], j - dj[d] # 육목 체크
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == c:
                return False

            return i, j

    return False


def omok():
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                where = f(i, j, arr[i][j])
                if where:
                    print(arr[i][j])
                    print(where[0] + 1, where[1] + 1)
                    return True
    return False


N = 19
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

if not omok():
    print(0)
