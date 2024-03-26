import sys

input = sys.stdin.readline


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < M)


def get_n(v, si, sj):  # si, sj에서 시작하는 가장 큰 정사각형의 한 변 길이 return + v 표시
    n = 1
    while True:
        for i in range(si, si + n):
            if OOB(i, sj + n - 1): return n - 1
            if arr[i][sj + n - 1] != 'x': return n - 1
            v[i][sj + n - 1] = 1

        for j in range(sj, sj + n):
            if OOB(si + n - 1, j): return n - 1
            if arr[si + n - 1][j] != 'x': return n - 1
            v[si + n - 1][j] = 1
        n += 1


def find_2nd_square(v1, need_cnt):  # 첫번째 사각형 표시 + 더 필요한 숫자 -> 두번째 사각형의 좌표와 크기 return
    for ni in range(N):
        for nj in range(M):
            if arr[ni][nj] != 'x': continue

            v2 = [[0] * M for _ in range(N)]
            n = get_n(v2, ni, nj)

            cnt = 0  # 두번째 사각형만의 영역 크기 구하기
            for i in range(ni, ni + n):
                for j in range(nj, nj + n):
                    if not v1[i][j] and v2[i][j]:
                        cnt += 1

            if cnt == need_cnt:
                return ni, nj, n

    return -1, -1, -1


def find_squares(si, sj):  # 두 사각형의 좌표와 크기 return
    v = [[0] * M for _ in range(N)]
    n = get_n(v, si, sj)  # 첫 사각형 크기 찾기
    i2, j2, n2 = find_2nd_square(v, x_cnt - n ** 2)  # 두번째 사각형 찾기
    return [(si, sj, n), (i2, j2, n2)]


def solve():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'x': continue
            lst = find_squares(i, j)
            for i, j, n in lst:
                print(i + 1, j + 1, n)
            return


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
x_cnt = sum([a.count('x') for a in arr])
solve()
