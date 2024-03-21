"""
9:38 시작
10:02 구상 완료
10:07 입력 구현 완료 + 휴식 시작
10:11 휴식 끝, 방향배열 재구상
10:12 재구상 완료, 구현 시작
10:42 벽 제외 구현 완료, 벽 재구상
10:59 벽 구현 완료
11:00 tc 2 디버깅 시작
11:02 디버깅 완료 (q 반복 누락 오류), tc 4 디버깅 시작
11:05 디버깅 완료 (테두리 0도 제외 오류), 전체 tc 확인 완료
11:12 코드 검토 완료

깡구현 문제라 차근차근 접근했다. 체력과 집중력이 떨어진 상태라 단계별로 구상-구현을 반복했다. 이를 위해 각 요소를 함수로 구현했다.
벽을 확인하는 로직이 까다로웠는데, 그냥 함수에게 시킨 후 나중에 함수를 구현하는 방식으로 접근했다.
깡구현 문제는 세부 규칙만 파악하면 구현은 어렵지 않으니 침착하게 분석해야 한다.
"""

from collections import defaultdict, deque


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < M)


def check_wall(i, j, d):  # d: (1-위, 3:오, 5:아래, 7:왼)
    if d == 1:
        return wall_dic[(i, j)][0]  # 벽이 없으면 0, 벽이 있으면 1
    elif d == 3:
        return wall_dic[(i, j)][1]
    elif d == 5:
        return wall_dic[(i + 1, j)][0]
    else:
        return wall_dic[(i, j - 1)][1]


def heat(ri, rj, rd):
    v = [[0] * M for _ in range(N)]
    si, sj = ri + di[rd], rj + dj[rd]  # 5도 오른 칸
    if OOB(si, sj): return
    v[si][sj] = 5
    room[si][sj] += 5
    q = deque([(si, sj)])

    for _ in range(4):
        nq = len(q)
        for _ in range(nq):
            ci, cj = q.popleft()

            for e in [-1, 0, 1]:
                d = (rd + e) % 8
                ni, nj = ci + di[d], cj + dj[d]

                if OOB(ni, nj): continue
                if v[ni][nj]: continue

                # 영향 받는 칸의 벽 확인
                if check_wall(ni, nj, (rd + 4) % 8): continue

                # 영향 주는 칸의 벽 확인
                if check_wall(ci, cj, (rd + e * 2) % 8): continue

                v[ni][nj] = v[ci][cj] - 1
                room[ni][nj] += v[ni][nj]
                q.append((ni, nj))

    return


di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
N, M, K = map(int, input().split())
robots = []
targets = []
for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(M):
        if ipt[j] == 1:  # 온풍기 -> 방향 재설정 후 좌표, 방향 저장
            robots.append((i, j, 3))
        elif ipt[j] == 2:
            robots.append((i, j, 7))
        elif ipt[j] == 3:
            robots.append((i, j, 1))
        elif ipt[j] == 4:
            robots.append((i, j, 5))
        elif ipt[j] == 5:  # 조사 지점 -> 리스트에 좌표 저장
            targets.append((i, j))

W = int(input())
wall_dic = defaultdict(lambda: [0, 0])
for _ in range(W):
    x, y, t = map(int, input().split())
    wall_dic[(x - 1, y - 1)][t] = 1

choco = 0
room = [[0] * M for _ in range(N)]  # 방 온도 배열

while True:

    # 모든 온풍기에서 바람이 한번 나온다
    for ri, rj, rd in robots:
        heat_arr = heat(ri, rj, rd)

    # 온도가 조절된다
    edit_arr = [[0] * M for _ in range(N)]

    for i in range(N)[::-1]:  # 끝 행부터 확인
        for j in range(M):  # 첫 열부터 확인
            wall = wall_dic[(i, j)]  # 현재 칸의 벽

            if wall[0] == 0 and i != 0:  # 윗벽 없음 -> 공기 조절
                cur = room[i][j]
                nxt = room[i - 1][j]
                edit = abs(cur - nxt) // 4  # 조절될 온도

                if cur > nxt:
                    edit_arr[i][j] -= edit
                    edit_arr[i - 1][j] += edit
                else:
                    edit_arr[i][j] += edit
                    edit_arr[i - 1][j] -= edit

            if wall[1] == 0 and j != M - 1:  # 오른쪽 벽 없음 -> 공기 조절
                cur = room[i][j]
                nxt = room[i][j + 1]
                edit = abs(cur - nxt) // 4  # 조절될 온도

                if cur > nxt:
                    edit_arr[i][j] -= edit
                    edit_arr[i][j + 1] += edit
                else:
                    edit_arr[i][j] += edit
                    edit_arr[i][j + 1] -= edit

    for i in range(N):
        for j in range(M):
            room[i][j] += edit_arr[i][j]

    # 테두리 칸 온도 1씩 감소 (0도 제외)
    for j in range(M):  # 0행, N-1행
        room[0][j] = max(0, room[0][j] - 1)
        room[N - 1][j] = max(0, room[N - 1][j] - 1)
    for i in range(1, N - 1):  # 0열, M-1열
        room[i][0] = max(0, room[i][0] - 1)
        room[i][M - 1] = max(0, room[i][M - 1] - 1)

    # 초콜렛 하나 먹기
    choco += 1
    if choco > 100:
        break

    # 조사대상 조사하기
    is_success = True
    for ti, tj in targets:
        if room[ti][tj] < K:
            is_success = False
            break

    if is_success:
        break

print(choco)
