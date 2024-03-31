"""
실행시간: 548(개선: 192) -> 896
풀이시간: 67분 - > 52분

<이전과의 비교>
bfs로 최적화를 했었는데 그 방법을 못 떠올리고 dfs로 풀었다.
그런데? bfs 때의 희미한 기억으로 v 배열은 bfs 처럼 썼다. 그래서 틀렸다!! dfs는 첫 방문에서 최단 거리를 보장하지 않는다!!
애매하게 기억하는 방법으로 적용하지 말고 제대로 된 구상을 해야 한다.
최단거리(횟수)를 구할 때는 꼭 bfs를 쓰자.

이전에 연속으로 같은 방향을 기울이는 경우도 구현했었는데, 필요 없다고 판단하고 구현하지 않았다.
이로 인해 실행시간이 늘어났다.


"""

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

"""
9:10~9:23 구상
9:24~10:01 1차 구현
10:02 동시에 빠져도 실패 발견
10:02~10:09 디버깅 및 코드 점검
10:09~10:15 휴식
10:15~10:17 오류 사항 발견 및 디버깅

89% 틀렸습니다

10:44 N M 실수 잡아냄 실화냐...............

<실수한 부분>

마지막 값인 10을 확인하고 return해야 했는데 확인을 안하고 바로 종료했다.
마지막 값은 꼭 점검하도록 하자

실수 안 하려고 일부러 복붙을 최대한 활용했는데 복붙 때문에 틀렸다... 헐...
N M 오타는 찾기 어려우니 꼭 검색을 통해 제 위치에 있는지 점검하자ㅠㅠ
ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅠㅠㅜㅠㅜㅠㅜ



<잘한 부분>

오류가 날 때 멘탈이 터질 미래가 보여서 오류가 나면 화장실을 가야겠다고 미리 생각하고 바로 실행한 점 덕분에 멘탈을 유지할 수 있었다


"""
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline


def bfs(sri, srj, sbi, sbj):
    v = defaultdict(lambda: 11)
    q = deque([(sri, srj, sbi, sbj)])
    v[(sri, srj, sbi, sbj)] = 0

    k = -1
    while True:
        k += 1
        nq = len(q)

        if k == 11:  # 10번까지 점검 완료 -> 종료
            return -1

        for _ in range(nq):

            ri, rj, bi, bj = q.popleft()

            if bi == oi and bj == oj:  # 구슬이 빠진 경우
                continue
            elif ri == oi and rj == oj:
                return k

            # 위 아래
            for d in [1, -1]:
                nri, nrj, nbi, nbj = up_down(ri, rj, bi, bj, d)  # 구슬 굴린다
                if v[(nri, nrj, nbi, nbj)] <= k + 1: continue  # 이미 적거나 같은 횟수로 이곳에 다다른 경우 skip
                v[(nri, nrj, nbi, nbj)] = k + 1  # 횟수 표기
                q.append((nri, nrj, nbi, nbj))

            # 왼 오
            for d in [1, -1]:
                nri, nrj, nbi, nbj = left_right(ri, rj, bi, bj, d)
                if v[(nri, nrj, nbi, nbj)] <= k + 1: continue
                v[(nri, nrj, nbi, nbj)] = k + 1
                q.append((nri, nrj, nbi, nbj))

    return -1


def up_down(ri, rj, bi, bj, d):  # d가 1이면 위, d가 -1이면 아래
    j_lst = list({rj, bj})
    if d == 1:  # 구슬이 굴러가서 놓일 위치
        start = 1
    else:
        start = N - 2

    for j in j_lst:  # 구슬이 있는 열만 확인
        s = start

        is_exit = False

        for i in range(1, N - 1)[::d]:  # 지구에 가까운 쪽부터 확인하며 구슬이 놓일 위치 갱신

            if arr[i][j] == '#':  # 벽 : 바로 위에 다음 구슬이 놓인다
                is_exit = False
                s = i + d
            elif arr[i][j] == 'O':  # 구멍 : 에 다음 구슬이 놓인다
                is_exit = True
                s = i
            elif i == ri and j == rj:  # 빨간 구슬 : 구멍일 경우 빠지고, 아닐 경우 바로 위에 다음 구슬이 놓인다
                if is_exit:  # 구멍에 빠진다
                    ri = s
                else:  # 굴러간다
                    ri = s
                    s += d
            elif i == bi and j == bj:  # 파란 구슬 : 구멍일 경우 빠지고, 아닐 경우 바로 위에 다음 구슬이 놓인다
                if is_exit:  # 구멍에 빠진다 -> 게임 끝
                    return ri, rj, oi, oj
                else:  # 굴러간다
                    bi = s
                    s += d

    return ri, rj, bi, bj


def left_right(ri, rj, bi, bj, d):  # d가 1이면 왼쪽, d가 -1이면 오른쪽
    i_lst = list({ri, bi})

    if d == 1:  # 구슬이 굴러가서 놓일 위치
        start = 1
    else:
        start = M - 2

    for i in i_lst:
        s = start

        is_exit = False

        for j in range(1, M - 1)[::d]:

            if arr[i][j] == '#':  # 벽
                is_exit = False
                s = j + d
            elif arr[i][j] == 'O':  # 구멍
                is_exit = True
                s = j
            elif i == ri and j == rj:  # 빨간 구슬
                if is_exit:  # 구멍에 빠진다
                    rj = s
                else:  # 굴러간다
                    rj = s
                    s += d
            elif i == bi and j == bj:  # 파란 구슬
                if is_exit:  # 구멍에 빠진다 -> 바로 종료
                    return ri, rj, oi, oj
                else:  # 굴러간다
                    bj = s
                    s += d

    return ri, rj, bi, bj


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v_set = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            oi, oj = i, j

ans = bfs(ri, rj, bi, bj)
print(ans)
