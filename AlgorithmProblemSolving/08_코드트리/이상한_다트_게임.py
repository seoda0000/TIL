"""
실행시간: 1624(340) -> 616
풀이시간: 25분 -> 35분

문제를 안 읽었다!!!!!!!!!!!!!!!!!!!!!!!
문제 좀 읽자!!!!!!!!
석의 프로님 코드를 참고하여 회전 로직을 구현했다
"""

"""
11:16 시작
11:21 구상 완료
11:29 구현 완료
11:32 회전 인덱스 디버깅
11:51 정규화 로직 추가


"""
from collections import deque


def turn(x, d, k, arr):
    for i in range(N):
        if (i + 1) % x == 0:  # 배수
            if d:  # 반시계 방향
                arr[i] = arr[i][k:] + arr[i][:k]
            else:  # 시계 방향
                arr[i] = arr[i][-k:] + arr[i][:-k]
    return


def pop(si, sj):
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    num = arr[si][sj]
    q = deque([(si, sj)])
    is_pop = False

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], (cj + dj[d]) % M
            if not (0 <= ni < N): continue
            if v[ni][nj]: continue
            if arr[ni][nj] != num: continue

            v[ni][nj] = 1
            arr[ni][nj] = 0
            q.append((ni, nj))
            is_pop = True

    if is_pop:
        arr[si][sj] = 0

    return is_pop


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(Q):
    x, d, k = map(int, input().split())
    turn(x, d, k, arr)

    is_pop = False
    sm = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not arr[i][j]: continue
            if pop(i, j):
                is_pop = True
            else:
                sm += arr[i][j]
                cnt += 1

    if not is_pop:
        mean = sm // cnt

        for i in range(N):
            for j in range(M):
                if arr[i][j] > mean:
                    arr[i][j] -= 1
                elif 0 < arr[i][j] < mean:
                    arr[i][j] += 1

print(sum([sum(a) for a in arr]))

"""
2:18 구상 완료
2:43 구현 완료

원판을 2차원 배열로 펴서 케이스를 체크했고 어렵지 않게 구상할 수 있었다.

석의 프로님 코드 참고: 리스트 슬라이싱 이용
"""
from collections import deque


def turn(x, d, k, arr):  # x의 배수 원판을 d(0: 시계, 1: 반시계) 방향으로 k번 회전
    for i in range(x, N + 1, x):
        if d:  # 반시계
            arr[i] = arr[i][k % M:] + arr[i][:k % M]
        else:  # 시계
            arr[i] = arr[i][(-k) % M:] + arr[i][:(-k) % M]
    return


def bfs(si, sj):
    q = deque([(si, sj)])
    v[si][sj] = 1
    target = arr[si][sj]  # 목표 숫자
    cnt = 1  # 목표 숫자와 같은 숫자 개수

    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], (cj + dj[d]) % M  # 열 -> 넘어갈 수 있다: 나머지 처리

            if not (1 <= ni < N + 1): continue  # 행 -> 넘어갈 수 없다: 범위 체크
            if v[ni][nj]: continue
            if arr[ni][nj] != target: continue

            q.append((ni, nj))
            v[ni][nj] = 1
            cnt += 1

    if cnt == 1:  # 같은 숫자가 없으면 v 초기화
        v[si][sj] = 0

    return


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N, M, Q = map(int, input().split())
arr = [[0] * M] + [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(Q)]

for order in orders:
    x, d, k = order
    # 원판 돌리기
    turn(x, d, k, arr)

    v = [[0] * M for _ in range(N + 1)]  # 지워질 숫자 표기
    for i in range(1, N + 1):
        for j in range(M):
            if arr[i][j] == 0: continue
            if v[i][j]: continue
            bfs(i, j)  # 같은 숫자 찾기

    is_changed = False  # 지워지는 숫자 존재 여부
    sm = 0  # 남아있는 수의 총합
    cnt = 0  # 남아있는 수의 총 개수
    for i in range(1, N + 1):
        for j in range(M):
            if arr[i][j] == 0: continue  # 이미 지워진 수
            if v[i][j]:  # 지워지는 수
                arr[i][j] = 0
                is_changed = True
            else:  # 남아있는 수
                sm += arr[i][j]
                cnt += 1

    if is_changed: continue  # 지워지는 수가 있으면 넘어간다
    if cnt == 0: continue  # 남아있는 수가 없으면 넘어간다

    avg = sm / cnt
    for i in range(1, N + 1):  # 정규화
        for j in range(M):
            if 0 < arr[i][j] < avg:
                arr[i][j] += 1
            elif arr[i][j] > avg:
                arr[i][j] -= 1

# 남아있는 수 더하기
ans = 0
for a in arr:
    ans += sum(a)
print(ans)
