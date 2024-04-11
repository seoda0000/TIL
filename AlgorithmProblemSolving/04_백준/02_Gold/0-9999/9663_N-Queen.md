# N-Queen

https://www.acmicpc.net/problem/9663
백준 골드4 9663

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

---

```python
def f(i, j, n, N):  # (i, j)에 n번째 퀸을 놓았을 때 n+1번째 퀸의 자리 탐색
    global ans
    if n == N:  # N개의 퀸을 모두 놓은 경우
        ans += 1  # 횟수 세기
        return

    if 0 not in arr[-1]:  # 마지막 줄에 놓을 수 있는 자리가 없으면 바로 중단
        return

    for d in range(-j, N - j):
        ni, nj = i + 1, j + d  # 다음 행 탐색
        if arr[ni][nj] == 0:  # 만약 퀸을 놓을 수 있으면
            note(ni, nj, 0, N, n + 1)  # 퀸이 공격할 수 있는 자리 표시
            f(ni, nj, n + 1, N)  # 퀸을 놓는다
            note(ni, nj, n + 1, N, 0)  # 퀸이 공격할 수 있는 자리 clear


def note(i, j, p, N, k):  # p로 표시된 자리 중 (i, j)의 퀸이 공격할 수 있는 자리를 k로 표시하는 함수
    for a in range(i + 1, N):
        for b in range(N):
            if (b == j or a - i == b - j or a - i == -b + j) and arr[a][b] == p:
                arr[a][b] = k


N = int(input())
arr = [[0] * N for _ in range(N)]
ans = 0

for y in range(0, N):  # 첫 행에서 시작
    note(0, y, 0, N, 1)  # 퀸이 공격할 수 있는 자리 표시
    f(0, y, 1, N)  # 퀸을 놓는다
    note(0, y, 1, N, 0)  # 퀸이 공격할 수 있는 자리 clear
print(ans)
```

### 참고답안

* check 함수 이용. 0, 1로 표시하는 게 아닌 1씩 증가.

```python
def check(si, sj):
    # [1] 위쪽체크
    for i in range(si):
        if arr[i][sj]:  # 해당좌표에 Q있다면 0
            return 0
    # [2] 좌측위쪽 대각선
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if arr[i][j]:
            return 0
        i, j = i - 1, j - 1
    # [3] 우측위쪽 대각선
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if arr[i][j]:
            return 0
        i, j = i - 1, j + 1
    return 1


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if check(n, j):
            arr[n][j] = 1
            dfs(n + 1)
            arr[n][j] = 0


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    ans = 0

    dfs(0)
    print(f'#{test_case} {ans}')
```

* lookup table 이용

```python
def check(si, sj):
    # [1] 위쪽체크
    for i in range(si):
        if arr[i][sj]:  # 해당좌표에 Q있다면 0
            return 0
    # [2] 좌측위쪽 대각선
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if arr[i][j]:
            return 0
        i, j = i - 1, j - 1
    # [3] 우측위쪽 대각선
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if arr[i][j]:
            return 0
        i, j = i - 1, j + 1
    return 1


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if check(n, j):
            arr[n][j] = 1
            dfs(n + 1)
            arr[n][j] = 0


def dfs_tbl(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if j not in v1 and (n + j) not in v2 and (n - j) not in v3:
            v1.append(j), v2.append(n + j), v3.append(n - j)
            dfs_tbl(n + 1)
            v1.pop(), v2.pop(), v3.pop()


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    ans = 0

    # dfs(0)

    v1 = []
    v2 = []
    v3 = []
    dfs_tbl(0)
    print(f'#{test_case} {ans}')
```

* 아래 3방향만 탐색 & 체크

```python
def checkQueensRoad(nth, sj, before, after):  # 퀸 경로 중 before을 after로 체크
    v[nth][sj] = after

    for d in range(3):
        ni, nj = nth, sj
        while True:
            ni += di[d]
            nj += dj[d]
            if not (0 <= ni < N and 0 <= nj < N): break

            if v[ni][nj] == before:
                v[ni][nj] = after
    return


def putQueen(nth):
    global ans
    if nth == N:
        ans += 1
        return

    for j in range(N):
        if v[nth][j] >= 0: continue

        checkQueensRoad(nth, j, -1, nth)
        putQueen(nth + 1)
        checkQueensRoad(nth, j, nth, -1)


N = int(input())
ans = 0
v = [[-1] * N for _ in range(N)]
di = [1, 1, 1]
dj = [0, 1, -1]
putQueen(0)

print(ans)

```

* 열, 대각선 visited 리스트 이용

```python
def putQueen(nth):
    global ans
    if nth == N:
        ans += 1
        return

    for j in range(N):
        if Vj[j]: continue
        
        rdIdx, ldIdx = N + nth - j - 1, nth + j
        if Vrd[rdIdx]: continue
        if Vld[ldIdx]: continue

        Vj[j] = 1
        Vrd[rdIdx] = 1
        Vld[ldIdx] = 1
        putQueen(nth + 1)
        Vj[j] = 0
        Vrd[rdIdx] = 0
        Vld[ldIdx] = 0


N = int(input())
ans = 0
Vj = [0] * N  # n = j
Vrd = [0] * (2 * N - 1)  # n = N+i-j-1
Vld = [0] * (2 * N - 1)  # n = i+j
putQueen(0)

print(ans)

```

* 비트 이용

```python
def putQueen(nth):
    global ans, Vjj, Vrd, Vld
    if nth == N:
        ans += 1
        return

    for j in range(N):
        if Vjj & 1 << j: continue

        rdIdx, ldIdx = N + nth - j - 1, nth + j
        if Vrd & 1 << rdIdx: continue
        if Vld & 1 << ldIdx: continue

        Vjj |= 1 << j
        Vrd |= 1 << rdIdx
        Vld |= 1 << ldIdx
        putQueen(nth + 1)
        Vjj ^= 1 << j
        Vrd ^= 1 << rdIdx
        Vld ^= 1 << ldIdx


N = int(input())
ans = 0
Vjj = 0  # idx = j
Vrd = 0  # idx = N+i-j-1
Vld = 0  # idx = i+j
putQueen(0)

print(ans)

```