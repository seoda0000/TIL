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
