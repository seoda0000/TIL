"""
실행시간 124(112) -> 112
풀이시간: 22분 -> 30분

구상하기 귀찮아서 바로 풀었더니 오히려 풀이시간이 늘었다!! 구상 빼먹지 말자...!
이동 가능한 칸이 없을 때 후진하는 로직에서 기존엔 while과 함수를 썼다면, 이번엔 다른 프로님들의 코드를 참고하여 그냥 for문 4번을 돌려서 로직을 단순화했다.
훨씬 편했다... 좋은 방법 같다.

"""

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
ci, cj, cd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]
v[ci][cj] = 1

while True:
    can_go = False
    nd = cd
    for _ in range(4):
        nd = (nd - 1) % 4

        ni, nj = ci + di[nd], cj + dj[nd]
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] or v[ni][nj]:
            continue

        v[ni][nj] = 1
        ci, cj = ni, nj
        can_go = True
        break

    if not can_go:
        ni, nj = ci - di[nd], cj - dj[nd]
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj]: break
        ci, cj = ni, nj
    else:
        cd = nd

print(sum([sum(vv) for vv in v]))

"""
15:00~15:11 구상 완료
15:11~15:22 구현 완료

방향을 나타내는 d를 습관적으로 for문에 써서 값이 바뀌는 오류가 있었다.
-> for문의 d를 체크하고 함수로 분리하자
-> 유지되어야 하는 방향 변수는 d 대신 dd로 표현하자
"""


def clean(ci, cj, dd, arr):
    ans = 0

    while True:
        if arr[ci][cj] == 0:
            arr[ci][cj] = 2
            ans += 1

        if is_near_clean(ci, cj):
            ni, nj = ci - di[dd], cj - dj[dd]
            if not (0 <= ni < N and 0 <= nj < M): return ans
            if arr[ni][nj] == 1: return ans
            ci, cj = ni, nj
            continue

        else:
            while True:
                dd = (dd + 3) % 4
                ni, nj = ci + di[dd], cj + dj[dd]
                if not (0 <= ni < N and 0 <= nj < M): continue
                if arr[ni][nj] == 1: continue
                if arr[ni][nj] == 0:
                    ci, cj = ni, nj
                    break
    return ans


def is_near_clean(ci, cj):
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M): continue
        if arr[ni][nj] == 0:
            return False
    return True


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
ci, cj, dd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = clean(ci, cj, dd, arr)

print(ans)
