"""
9:15 시작
9:18 구상 완료
9:30 구현 완료
"""


def build(row: list):
    v = [0] * N
    for n in range(N):
        if n == 0 or row[n] == row[n - 1]: continue
        if abs(row[n] - row[n - 1]) >= 2: return False

        # 1 차이 나는 경우
        if row[n] < row[n - 1]:
            if not check(row, v, n, 1):
                return False
        if row[n] > row[n - 1]:
            if not check(row, v, n - 1, -1):
                return False

    return True


def check(row, v, start, k):  # start에서 X개의 칸을 k 방향으로 점검

    h = row[start]
    c = start
    for _ in range(X):
        if not (0 <= c < N): return False
        if v[c]: return False
        if row[c] != h: return False
        v[c] = 1
        c += k
    return True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for n in range(N):
        if build(arr[n]):
            ans += 1
    arr = list(zip(*arr))
    for n in range(N):
        if build(arr[n]):
            ans += 1
    print(f'#{test_case} {ans}')
