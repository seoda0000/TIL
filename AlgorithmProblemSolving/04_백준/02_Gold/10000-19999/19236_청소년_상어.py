"""
실행시간: 116 -> 128
풀이시간: 94분 -> 104분

함수에서 si, sj를 참조하는데 매개변수를 주지 않아서, main 함수 단까지 가서 si, sj를 찾았다.
그래서 오류가 났다... 엄청 찾기 어려웠다!!
자동 참조에 기대지 말고 함수에 필요한 매개변수를 다 주자.

그리고 틀린 테케로 디버깅한다고 생각했는데 맞은 테케로 디버깅하면서 왜 안되지 싶었다.
도저히 찾기 어려워서 중간에 한시간 정도 자고 일어나서 다시 풀었다.
피곤하면 별별 일을 다 저지르므로 상태가 최악이라고 가정하고 침착하게 살펴야 할 것이다.

이건 한번 더 풀어야 할듯...
"""

"""
3:18 시작
3:25 구상 완료
3:45 구현 완료
5:01 디버깅 완료
"""


def solve(arr, si, sj, sd, score):
    global ans

    ans = max(ans, score)  # 정답 갱신

    # 도둑말 이동
    for id in range(1, 17):
        move(arr, si, sj, id)

    # 술래말 이동
    ci, cj = si, sj
    while True:
        ci, cj = ci + di[sd], cj + dj[sd]

        if OOB(ci, cj): return
        if arr[ci][cj][0] == 0: continue  # 먹을 물고기 없음
        fid, fd = arr[ci][cj]  # 먹을 물고기
        arr[ci][cj] = (0, 0)  # 꿀꺽
        solve([a[:] for a in arr], ci, cj, fd, score + fid)
        arr[ci][cj] = (fid, fd)  # 꿀꺽 초기화

    return


def move(arr, si, sj, id):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] != id: continue  # 이동할 도둑말 찾기

            d = arr[i][j][1]
            for _ in range(8):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj) or (ni == si and nj == sj):  # 이동불가
                    d = (d + 1) % 8
                else:  # 이동 가능
                    arr[i][j] = (id, d)  # 방향 갱신
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                    return

            return


def OOB(i, j):
    return not (0 <= i < 4 and 0 <= j < 4)


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
arr = [[(0, 0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    ipt = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = (ipt[j * 2], ipt[j * 2 + 1] - 1)

# 0, 0 먹기
si, sj = 0, 0
sid, sd = arr[0][0]
arr[0][0] = (0, 0)

ans = 0
solve(arr, si, sj, sd, sid)
print(ans)

"""
2:05 시작
2:10 문제 읽기 완료
2:15 구상 완료
2:40 1차 구현 완료
2:52 디버깅 완료(%4 오류)
3:01 휴식
3:05 휴식 끝
3:06 배열 복사 이슈 해결
3:26 디버깅 포기
3:39 딕셔너리 디버깅

딕셔너리도 복사를 해야 한다는 걸 늦게 깨달아서 디버깅이 오래 걸렸다.
원래 배열 복사를 즐겨 사용하지 않아서 더더욱 구현하기 어려웠던 것 같다...
배열이나 자료구조 복사는 dfs 보내기 직전에 복사하는 쪽으로 스타일을 만들 것 같다.

디버깅을 엄청 오래 한 기분이었는데 사실 아니었다.
디버깅이 길어져도 포기하지 말고 환기하고 다시 시도하자
"""


def dfs(arr, fish_dic, sm, si, sj):  # 바다 지도, 물고기 좌표 딕셔너리, 상어가 여태 먹은 물고기 수, 곧 먹을 위치
    global ans

    # 먹기
    fish_num, fish_dir = arr[si][sj]
    fish_dic[fish_num] = -1, -1

    # 상어 넣기
    arr[si][sj] = (-1, fish_dir)

    # 물고기 이동
    arr, fish_dic = move_fish(arr, fish_dic)

    is_move = False

    ci, cj = si, sj
    arr[si][sj] = (0, 0)  # 상어가 떠난다
    while True:  # 물고기가 있으면 이동
        ci, cj = ci + di[fish_dir], cj + dj[fish_dir]
        if not (0 <= ci < 4 and 0 <= cj < 4): break
        if arr[ci][cj][0] <= 0: continue  # 물고기가 없다

        # 다음 단계에서 사용할 배열, 딕셔너리 만들기
        n_arr = [row[::] for row in arr]
        n_dic = {key: value for key, value in fish_dic.items()}

        dfs(n_arr, n_dic, sm + fish_num, ci, cj)  # 다음 물고기 먹으러 간다
        is_move = True

    if is_move is False:  # 이동 불가 시 ans 갱신
        ans = max(ans, sm + fish_num)

    return


def move_fish(arr, fish_dic):
    for num in range(1, 17):
        fi, fj = fish_dic[num]
        if fi < 0:  # 먹힌 물고기
            continue
        fish_dir = arr[fi][fj][1]
        fd = fish_dir
        cnt = 0
        while True:
            if fd == fish_dir:  # 한바퀴 돌았으면 정지
                cnt += 1
                if cnt == 2:
                    break

            ni, nj = fi + di[fd], fj + dj[fd]

            if not (0 <= ni < 4 and 0 <= nj < 4):
                fd = (fd + 1) % 8
                continue

            nfish_num, nfish_dir = arr[ni][nj]
            if nfish_num < 0:  # 상어
                fd = (fd + 1) % 8
                continue

            # 이동
            if nfish_num == 0:  # 빈칸
                arr[ni][nj], arr[fi][fj] = (num, fd), (0, 0)
                fish_dic[num] = (ni, nj)
            else:  # 다른 물고기와 교체
                arr[ni][nj], arr[fi][fj] = (num, fd), (nfish_num, nfish_dir)
                fish_dic[num] = (ni, nj)
                fish_dic[nfish_num] = (fi, fj)
            break

    return arr, fish_dic


di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dic = {0: (-1, -1)}  # 물고기 번호: [현재 좌표 i, j]
arr = [list() for _ in range(4)]
for i in range(4):
    ipt = list(map(int, input().split()))
    for j in range(0, 8, 2):
        arr[i].append((ipt[j], ipt[j + 1] - 1))  # 번호, 방향
        fish_dic[ipt[j]] = (i, j // 2)

ans = 0
# 상어 0, 0 먹기 + 물고기 이동
dfs(arr, fish_dic, 0, 0, 0)
print(ans)
