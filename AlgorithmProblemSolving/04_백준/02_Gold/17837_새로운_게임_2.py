"""
0:06~0:10 문제읽기
0:10~0:20 구상
0:21~0:46 1차 구현
0:46~0:48 tc 1 입력 -> 1차 디버깅 - group 배열 인덱스 오류 해결
0:48~0:50 tc 3 입력 -> 2차 디버깅 - d 변수 공유 오류 해결
0:51~0:57 tc 5 입력 -> 디버거 이용하여 로직 체크
0:57~0:59 문제 재확인
0:59~01:06 3차 디버깅 - 공유 변수 분리 및 중복 코드 제거
01:06~01:07 4차 디버깅 - 파란 칸 케이스 방향 전환
1:09~1:12 휴식
1:12~1:28 시뮬레이션 시점마다 보드, 말 위치 등 print하여 확인
1:28~1:30 5차 디버깅 - 종료 조건 수정
1:30~1:35 문제 다시 읽은 후 코드 상세 검토 -> 6차 디버깅 - 튜플 오타 수정
1:35~1:36 tc 재점검 및 제출 (18줄)


설계를 꼼꼼하게 하려 했는데도 사용하는 자료구조가 많다보니 디버깅거리가 많았다.
다양한 자료구조를 쓴다면 check나 clear 시 수정사항이 모든 자료구조에 반영 되었는지 확인해야 한다
또한 종료조건........문제에서 시키는 그대로 섬세하게 다뤄야 한다


디버거를 연결했다 끊었다하니까 캐시 문제인지 이상하게 수정한 코드가 반영되지 않았는데, 이 때문에 5분 더 디버깅 했다...
디버거를 돌릴 때 혹시 모르니 두번씩 점검해보자
"""


def go_white(idx, ci, cj, ni, nj):
    ck = board[ci][cj].index(idx)  # 몇층에 위치하고 있는지

    nb = len(board[ci][cj])
    if ck == 0:  # 0층이 이동 (전체 이동)
        for x in range(nb):
            gdx = board[ci][cj][x]
            xi, xj, xd = cur_horses[gdx]
            cur_horses[gdx] = (ni, nj, xd)
            board[ni][nj].append(gdx)
        board[ci][cj] = []
    else:  # 부분 이동
        group = []  # 옮길 말들
        for _ in range(ck, nb):
            group.append(board[ci][cj].pop())
        ng = len(group)
        for _ in range(ng):
            gdx = group.pop()
            board[ni][nj].append(gdx)
            xi, xj, xd = cur_horses[gdx]
            cur_horses[gdx] = (ni, nj, xd)
    return


def go_red(idx, ci, cj, ni, nj):
    ck = board[ci][cj].index(idx)  # 몇층에 위치하고 있는지

    nb = len(board[ci][cj])

    for x in range(ck, nb):
        gdx = board[ci][cj].pop()
        xi, xj, xd = cur_horses[gdx]
        cur_horses[gdx] = (ni, nj, xd)
        board[ni][nj].append(gdx)

    return


di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
N, K = map(int, input().split())
# 0: 흰색, 1: 빨간색, 2: 파란색
arr = [list(map(int, input().split())) for _ in range(N)]
board = [[list() for _ in range(N)] for _ in range(N)]
oppo_dic = {1: 2, 2: 1, 3: 4, 4: 3}
cur_horses = dict()
for idx in range(1, K + 1):
    i, j, d = map(int, input().split())
    i, j = i - 1, j - 1
    board[i][j].append(idx)
    cur_horses[idx] = (i, j, d)

for turn in range(1, 1001):

    # if turn <= 8:
    #     print(f'{turn}번째 이동 전')
    #     for b in board:
    #         print(b)
    #     print()
    #
    #     for idx in range(1, K + 1):
    #         ci, cj, cd = cur_horses[idx]
    #         st = ''
    #         if cd == 1:
    #             st = '오른쪽'
    #         elif cd == 2:
    #             st = '왼쪽'
    #         elif cd == 3:
    #             st = ' 위쪽'
    #         elif cd == 4:
    #             st = '아래쪽'
    #
    #         print(f'{idx} 말은 {st}로 이동해야 한다.')

    # =========================================================================
    # 순서대로 말 이동시키기
    end = False

    for idx in range(1, K + 1):
        ci, cj, cd = cur_horses[idx]  # 위치, 방향

        ni, nj = ci + di[cd], cj + dj[cd]

        if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == 2:  # 범위 밖이거나 파란색
            nd = oppo_dic[cd]  # 반대 방향 1칸 이동
            ni, nj = ci + di[nd], cj + dj[nd]

            if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == 2:  # 범위 밖이거나 파란색 (이동 X)
                cur_horses[idx] = (ci, cj, nd)

            elif arr[ni][nj] == 0:  # 흰색
                go_white(idx, ci, cj, ni, nj)
                cur_horses[idx] = (ni, nj, nd)

            else:  # 빨간색
                go_red(idx, ci, cj, ni, nj)
                cur_horses[idx] = (ni, nj, nd)


        elif arr[ni][nj] == 0:  # 흰색
            go_white(idx, ci, cj, ni, nj)

        else:  # 빨간색
            go_red(idx, ci, cj, ni, nj)

        # 조건 충족시
        for i in range(N):
            for j in range(N):
                if len(board[i][j]) >= 4:
                    end = True
                    break

    if end:
        print(turn)
        break
else:
    print(-1)
