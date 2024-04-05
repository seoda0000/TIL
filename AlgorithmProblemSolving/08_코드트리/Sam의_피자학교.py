"""
9:29 시작
9:38 구상 완료
10:04 구현 완료
"""


def push(arr):
    new_arr = [[0] * len(arr[-1]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cur = arr[i][j]
            for d in range(2):
                ni, nj = i + di[d], j + dj[d]
                if not (0 <= ni < len(arr) and 0 <= nj < len(arr[ni])): continue
                nxt = arr[ni][nj]
                x = abs(nxt - cur) // 5
                if not x: continue
                if cur > nxt:
                    new_arr[i][j] -= x
                    new_arr[ni][nj] += x
                else:
                    new_arr[i][j] += x
                    new_arr[ni][nj] -= x

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += new_arr[i][j]

    c_arr = list(map(list, zip(*arr[::-1])))
    tail = arr[-1][len(arr[0]):]
    flat_lst = sum(c_arr, [])
    return flat_lst + tail


di = [0, 1]
dj = [1, 0]
N, K = map(int, input().split())
flat_lst = list(map(int, input().split()))

t = 0
while True:

    # 밀가루 추가
    mn = min(flat_lst)

    for n in range(N):
        if flat_lst[n] == mn:
            flat_lst[n] += 1

    # 도우 말기

    if N == 1:
        arr = [flat_lst]
    else:
        arr = [[flat_lst[0]]] + [flat_lst[1:]]

        while True:
            w = len(arr[0])
            dough = [a[:w] for a in arr]
            c_dough = list(map(list, zip(*dough[::-1])))
            floor = arr[-1][w:]
            if len(c_dough[0]) > len(floor):
                break
            arr = c_dough + [floor]

    # 꾹 누르기
    flat_lst = push(arr)

    # 두번 접기
    arr = [flat_lst[:N // 2][::-1]] + [flat_lst[N // 2:]]  # 힌번 접기
    up = [a[:N // 2 // 2] for a in arr]
    down = [a[N // 2 // 2:] for a in arr]
    up = list(map(list, zip(*up[::-1])))
    up = list(map(list, zip(*up[::-1])))
    arr = up + down

    # 꾹 누르기
    flat_lst = push(arr)

    t += 1
    if max(flat_lst) - min(flat_lst) <= K:
        break
print(t)
