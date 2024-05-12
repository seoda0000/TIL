"""
20:02~20:11 구상
20:11~20:28 1차 구현

시간 복잡도
testcase*(N*M + K*T + T + N)
= testcase*(15*15 + 50*15*15 + 15*15 + 15)

20:28~20:39 코드 검토
20:39~20:43 1차 디버깅
20:43~20:48 테스트케이스 적용

제출 전에 문제를 다시 읽고 테스트케이스를 생각해보자...
"""
p = 0
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break
    p += 1
    arr = [list(input()) for _ in range(N)]
    keys = input()
    dic = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
    targets = []  # 목표 지점 좌표 리스트
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'w':
                wi, wj = i, j
            elif arr[i][j] == 'W':
                targets.append((i, j))
                wi, wj = i, j
            elif arr[i][j] == 'B':
                targets.append((i, j))
                arr[i][j] = 'b'
            elif arr[i][j] == '+':
                targets.append((i, j))

    ans = 'incomplete'
    for key in keys:
        di, dj = dic[key]

        ni, nj = wi + di, wj + dj

        if arr[ni][nj] == '#':  # 벽 -> 이동 불가
            continue
        elif arr[ni][nj] == 'b':  # 박스
            nni, nnj = ni + di, nj + dj
            if arr[nni][nnj] == '#': continue
            if arr[nni][nnj] == 'b': continue
            arr[nni][nnj] = 'b'
            arr[ni][nj] = 'w'
            arr[wi][wj] = '.'
            wi, wj = ni, nj
        else:  # 빈칸 -> 이동
            arr[ni][nj] = 'w'
            arr[wi][wj] = '.'
            wi, wj = ni, nj

        is_completed = True
        for ti, tj in targets:
            if arr[ti][tj] != 'b':
                is_completed = False
                break
        if is_completed:
            ans = 'complete'
            break

    for ti, tj in targets:
        if arr[ti][tj] == '.':
            arr[ti][tj] = '+'
        elif arr[ti][tj] == 'b':
            arr[ti][tj] = 'B'
        elif arr[ti][tj] == 'w':
            arr[ti][tj] = 'W'

    print(f'Game {p}: {ans}')
    for a in arr:
        print(''.join(a))
