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
