"""
4:03 시작
4:08 구상 완료
4:22~4:29 휴식
4:38 1차 구현 완료
4:41 첫 제출
4:41~4:48 v set 오류 (dfs는 첫 방문에서 최단 거리를 보장하지 않는다)
4:48 두번째 제출
4:48~4:55 출구 조건 오류 (행과 열 모두가 일치해야 출구다)
4:55 세번째 제출
"""
from collections import defaultdict


def solve(nth, ri, rj, bi, bj):
    global ans

    if nth >= ans:
        return

    if ri == oi and rj == oj:
        ans = min(ans, nth)
        return

    if (ri, rj, bi, bj) in v:
        if v_dic[(ri, rj, bi, bj)] <= nth:
            return
    else:
        v.add((ri, rj, bi, bj))
        v_dic[(ri, rj, bi, bj)] = nth

    for k in [1, -1]:
        nri, nrj, nbi, nbj = up_down(k, ri, rj, bi, bj)
        if nbi >= 0:  # 아직 종료되지 않았다면
            solve(nth + 1, nri, nrj, nbi, nbj)

    for k in [1, -1]:
        nri, nrj, nbi, nbj = right_left(k, ri, rj, bi, bj)
        if nbi >= 0:  # 아직 종료되지 않았다면
            solve(nth + 1, nri, nrj, nbi, nbj)
    return


def up_down(k, ri, rj, bi, bj):  # (k:1 위 -1 아래)로 굴린 후 구슬 위치 return
    j_lst = list({rj, bj})

    for j in j_lst:

        for i in range(N)[::k]:
            if arr[i][j] == 1:  # 장애물
                xi = i + k
            elif arr[i][j] == -1:  # 출구
                xi = i
            elif i == ri and j == rj:  # 빨간 구슬 발견
                ri = xi  # 굴러 간다
                if not (ri == oi and rj == oj):  # 출구가 아니면
                    xi += k
            elif i == bi and j == bj:  # 파란 구슬 발견
                bi = xi  # 굴러 간다
                if not (bi == oi and bj == oj):  # 출구가 아니면
                    xi += k

    if bi == oi and bj == oj:
        bi, bj = -1, -1
    return ri, rj, bi, bj


def right_left(k, ri, rj, bi, bj):  # (k:1 왼 -1 오)로 굴린 후 구슬 위치 return
    i_lst = list({ri, bi})

    for i in i_lst:

        for j in range(M)[::k]:
            if arr[i][j] == 1:  # 장애물
                xj = j + k
            elif arr[i][j] == -1:  # 출구
                xj = j
            elif i == ri and j == rj:  # 빨간 구슬 발견
                rj = xj  # 굴러 간다
                if not (ri == oi and rj == oj):  # 출구가 아니면
                    xj += k
            elif i == bi and j == bj:  # 파란 구슬 발견
                bj = xj  # 굴러 간다
                if not (bi == oi and bj == oj):  # 출구가 아니면
                    xj += k

    if bi == oi and bj == oj:
        bi, bj = -1, -1
    return ri, rj, bi, bj


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]  # 0 빈칸, 1 장애물, -1 출구
for i in range(N):
    ipt = input()

    for j in range(M):
        if ipt[j] == '#':  # 장애물
            arr[i][j] = 1
        elif ipt[j] == 'B':  # 파란 사탕
            bi, bj = i, j
        elif ipt[j] == 'R':  # 빨간 사탕
            ri, rj = i, j
        elif ipt[j] == 'O':  # 출구
            oi, oj = i, j
            arr[i][j] = -1

v = set()
v_dic = defaultdict(lambda: 11)
ans = 11
solve(0, ri, rj, bi, bj)

if ans == 11:
    ans = -1
print(ans)
