"""
10:45 시작
10:50 구상 완료
11:01 구현 완료
11:10 변수 중복 오류 디버깅
"""


def solve(board, arr, horse_dic):
    for turn in range(1, 1001):
        for k in range(1, K + 1):
            i, j, d = horse_dic[k]
            f = arr[i][j].index(k)  # 몇층인지

            ni, nj = i + di[d], j + dj[d]

            if board[ni][nj] == 2:  # 파
                d ^= 1
                ni, nj = i + di[d], j + dj[d]
                if board[ni][nj] == 2:  # 방향 전환만
                    ni, nj = i, j

            if not (ni == i and nj == j):  # 이동
                arr[i][j], moving_horses = arr[i][j][:f], arr[i][j][f:]
                if board[ni][nj] == 1:  # 빨
                    moving_horses = moving_horses[::-1]
                arr[ni][nj].extend(moving_horses)

                if len(arr[ni][nj]) >= 4:
                    return turn

                for hk in moving_horses:
                    hi, hj, hd = horse_dic[hk]
                    horse_dic[hk] = ni, nj, hd

            horse_dic[k] = ni, nj, d  # 정보 갱신
    return -1


di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

N, K = map(int, input().split())
board = [[2] * (N + 2)] \
        + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] \
        + [[2] * (N + 2)]
N += 2
arr = [[list() for _ in range(N)] for _ in range(N)]
horse_dic = dict()  # id: (좌표 i, j, 방향)
for k in range(1, K + 1):
    x, y, d = map(int, input().split())
    horse_dic[k] = (x, y, d - 1)
    arr[x][y].append(k)

print(solve(board, arr, horse_dic))
