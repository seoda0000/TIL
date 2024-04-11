"""
실행시간: 128(120) -> 124
풀이시간: 48분 -> 15분

이전에는 if elif else를 통해 조건을 복잡하게 분기하고 분기마다 함수를 따로 구현했다. (땜빵 코딩)
이번엔 최대한 간결하게 분기하고, 각각의 분기를 모두 통일할 수 있도록 함수를 설계했다.
상당히 힘든 상황에서 어렵게 푼 문제 중 하나인데 너무나 쉽게 풀려 의아하다...
함수화할 때는 설계를 꼭 하자. 땜빵 코딩 절대 안됨!!

"""

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

"""
15:18 문제 읽기 시작
16:06 구현 완료

심신이 미약한 상태로 풀기 시작해서 상당히 더럽다...
경우를 나눠 각각의 상황마다 구상을 했다.
이전 위치를 돌아보지 않겠다고 생각하고 갔는데, 오르락 내리락거리는 부분 때문에 v 배열을 적용해서 풀었다.
v 배열을 적용하면 이전에 썼던 변수를 상당량 지워도 돌아간다.

transpose를 싫어해서 안 썼는데... 단순 행 열 순회면 적극적으로 쓰도록 해봐야겠다. 훨씬 깔끔해진다!
구상을 조금 더 꼼꼼히 하자
"""


def check(ci, cj):
    global cnt

    if cj >= N - 1:
        cnt += 1
        return

    ck = arr[ci][cj]
    nk = arr[ci][cj + 1]

    if nk > ck + 1:
        return

    elif nk == ck + 1:
        for x in range(cj - L + 1, cj + 1):
            if x < 0: return
            if arr[ci][x] != arr[ci][cj]: return
            if v[x]:
                return
            else:
                v[x] = 1
        check(ci, cj + 1)

    elif nk == ck:
        check(ci, cj + 1)

    elif nk == ck - 1:
        for x in range(cj + 1, cj + 1 + L):
            if x >= N: return
            if arr[ci][x] != arr[ci][cj + 1]: return
            if v[x]:
                return
            else:
                v[x] = 1
        check(ci, cj + L)

    else:
        return

    return


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):  # 행 확인
    v = [0] * N
    check(i, 0)
arr = list(zip(*arr))
for i in range(N):  # 열 확인
    v = [0] * N
    check(i, 0)

print(cnt)
