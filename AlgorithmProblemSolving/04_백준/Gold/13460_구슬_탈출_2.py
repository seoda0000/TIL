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
