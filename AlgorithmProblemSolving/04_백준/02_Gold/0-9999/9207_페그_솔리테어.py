import sys

input = sys.stdin.readline


def solve():
    global ans

    if ans == 1:
        return

    can_move = False
    cnt = 0
    for n in range(1, N + 1):
        pi, pj = dic[n]
        if pi == -1:
            continue

        cnt += 1  # 핀 개수 세기
        for d in range(4):
            # 주위 칸에 핀 있는지 확인
            ni, nj = pi + di[d], pj + dj[d]
            if not (0 <= ni < 5 and 0 <= nj < 9): continue
            if arr[ni][nj] <= 0: continue

            # 핀이 있다면, 그 너머로 갈 수 있는지 확인
            nni, nnj = ni + di[d], nj + dj[d]
            if not (0 <= nni < 5 and 0 <= nnj < 9): continue
            if arr[nni][nnj]: continue

            # 갈 수 있다면 가기
            can_move = True
            n_other = arr[ni][nj]  # 상대 정보

            arr[ni][nj] = 0
            arr[nni][nnj] = n
            dic[n] = (nni, nnj)
            dic[n_other] = (-1, -1)
            arr[pi][pj] = 0

            # 다음으로
            solve()

            # 초기화
            arr[pi][pj] = n
            dic[n] = (pi, pj)
            dic[n_other] = (ni, nj)
            arr[nni][nnj] = 0
            arr[ni][nj] = n_other

    if not can_move:  # 더 이상 움직이지 못할 경우 개수 세기
        ans = min(cnt, ans)
        return

    return


T = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for t in range(1, T + 1):
    arr = []
    dic = dict()
    N = 1
    for i in range(5):
        ipt = input()
        row = []
        for j in range(9):
            if ipt[j] == '#':
                row.append(-1)
            elif ipt[j] == '.':
                row.append(0)
            else:
                row.append(N)
                dic[N] = (i, j)
                N += 1
        arr.append(row)

    if t < T:
        input()
    N -= 1
    ans = 9 * 5
    solve()
    print(ans, N - ans)
