"""
실행시간: 168 -> 288
풀이시간: 54분 -> 23분

이전에 푼 풀이가 복잡하다고 느껴져서, 이번엔 다른 프로님들의 방식대로 풀어보았다.
실행시간이 오래 걸리지만 훨씬 깔끔한 방식이라고 느껴진다.
이전에는 포인터를 활용하여 한번에 이동과 계산을 처리했는데,
이번엔 q를 이용하여 이동한 후에 계산을 해주었다.

이때 방향에 따라 배열을 반대로 뒤집는 디테일을 놓치지 말아야 한다.
새로운 배열을 만들 때는 4방향대로 검토해야 한다.
"""

"""
5:10 시작
5:16 구상 완료
5:33 제출
"""
from collections import deque


def play(arr, nth):
    global ans

    if nth == 5:
        ans = max(ans, max([max(a) for a in arr]))
        return

    for d in range(4):
        narr = swipe(arr, d)
        play(narr, nth + 1)
    return


def swipe(arr, d):  # (d: 0 위 1 아래 2 왼 3 오)로 swipe 하기

    if d % 2:
        k = -1
    else:
        k = 1

    new_arr = []
    if d < 2:  # 위아래
        for j in range(N):
            q = deque()
            for i in range(N)[::k]:  # 숫자만 채워주기
                if arr[i][j]: q.append(arr[i][j])

            row = []
            while True:
                if len(q) >= 2:
                    if q[0] == q[1]:
                        row.append(q.popleft() + q.popleft())
                    else:
                        row.append(q.popleft())
                else:
                    if q:
                        row.append(q.popleft())
                    break

            row += [0] * (N - len(row))  # padding
            new_arr.append(row[::k])
        new_arr = list(map(list, zip(*new_arr)))

    else:  # 왼오
        for i in range(N):
            q = deque()
            for j in range(N)[::k]:  # 숫자만 채워주기
                if arr[i][j]: q.append(arr[i][j])
            row = []
            while True:
                if len(q) >= 2:
                    if q[0] == q[1]:
                        row.append(q.popleft() + q.popleft())
                    else:
                        row.append(q.popleft())
                else:
                    if q:
                        row.append(q.popleft())
                    break

            row += [0] * (N - len(row))  # padding
            new_arr.append(row[::k])

    return new_arr


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
play(arr, 0)

print(ans)

"""
9:10~10:04

컨디션이 안 좋아서 최대한 천천히 꼼꼼히 풀었다.
부딪힐 칸과 부딪힐 값을 따로 관리해야 해서 설계 단계에서 헷갈렸다. 변수명 지정부터 하니 그나마 풀렸다.

체크하고 초기화하며 dfs 돌리는 방법이 떠오르지 않아서 각 상황별로 새로운 배열을 만드는 방식을 채택했다.
처음엔 연속적으로 폭파되는 줄 알았는데, 게임을 직접 해보니 아니라서 폭파 후 idx를 갱신해주었다.

디버깅으로는 테스트 케이스를 만들기 힘들어서, 게임의 룰인 '상황마다 배열 값의 합이 일정하게 유지되는지'를 확인했다.
역시 유지되지 않아서 print를 활용하여 디버깅했다.
직전의 이동을 string으로 넘겨서 print를 찍어서 어느 부분에서 오류가 생기는지 쉽게 확인할 수 있었다.
new_arr의 값을 참조해야 하는데 arr의 값을 참조하여 실제보다 큰 값으로 바뀌는 오류였다.

이렇게 다양한 방식으로 실전에서 시간이 남으면 QA를 해봐야겠다

"""

import sys

input = sys.stdin.readline


def dfs(nth, arr):
    global ans

    if nth == 5:
        mx = max([max(a) for a in arr])
        ans = max(ans, mx)
        return

    # 위
    new_arr = up_down(1, arr)
    dfs(nth + 1, new_arr)

    # 아래
    new_arr = up_down(-1, arr)
    dfs(nth + 1, new_arr)

    # 왼
    new_arr = left_right(1, arr)
    dfs(nth + 1, new_arr)

    # 오
    new_arr = left_right(-1, arr)
    dfs(nth + 1, new_arr)

    return


def up_down(d, arr):  # 1이면 위, -1이면 아래 -> 움직인 후의 arr 반환

    new_arr = [[0] * N for _ in range(N)]

    if d == 1:
        start = 0  # 체크 시작 위치 (움직이는 방향 쪽)
    else:
        start = N - 1

    for j in range(N):
        crush_idx = start  # 부딪힐 칸
        crush_val = arr[start][j]  # 부딪힐 값
        new_arr[start][j] = crush_val

        i = start
        for _ in range(1, N):
            i += d  # 방향에 따라 이동

            if arr[i][j] == 0: continue

            if arr[i][j] == crush_val:  # 같은 값 -> 합쳐짐 (only 1회)
                new_arr[crush_idx][j] = new_arr[crush_idx][j] * 2
                crush_val = 0
                crush_idx += d
            else:
                if crush_val:  # 부딪힐 칸에 다른 숫자가 있는 경우 쌓인다
                    crush_idx += d
                new_arr[crush_idx][j] = arr[i][j]
                crush_val = arr[i][j]

    return new_arr


def left_right(d, arr):  # 1이면 왼쪽, -1이면 오른쪽 -> 움직인 후의 arr 반환

    new_arr = [[0] * N for _ in range(N)]
    if d == 1:
        start = 0
    else:
        start = N - 1
    for i in range(N):
        crush_idx = start  # 부딪힐 칸
        crush_val = arr[i][start]  # 부딪힐 값
        new_arr[i][start] = crush_val

        j = start
        for _ in range(1, N):
            j += d

            if arr[i][j] == 0: continue

            if arr[i][j] == crush_val:  # 같은 값 -> 합쳐짐 (only 1회)
                new_arr[i][crush_idx] = new_arr[i][crush_idx] * 2
                crush_val = 0
                crush_idx += d
            else:
                if crush_val:
                    crush_idx += d
                new_arr[i][crush_idx] = arr[i][j]
                crush_val = arr[i][j]

    return new_arr


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, arr)
print(ans)
