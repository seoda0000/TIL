"""
2:51 시작
2:56 구상 완료
3:12 구현 완료
"""


def drop(arr, t, j):
    if t % 2:
        here = 5
        for i in range(6):
            if arr[i][j]:
                here = i - 1
                break
        arr[here][j] = 1
        if t == 3:
            arr[here - 1][j] = 1
    else:
        here = 5
        for i in range(6):
            if arr[i][j] or arr[i][j + 1]:
                here = i - 1
                break
        arr[here][j] = 1
        arr[here][j + 1] = 1
    return


def check_score(arr):
    score = 0

    cur = 0
    while cur < 6:
        if sum(arr[cur]) == 4:  # full
            score += 1
            arr.pop(cur)
            arr.insert(0, [0] * 4)
        cur += 1
    return score


def check_ceiling(arr):
    cnt = 0
    for cur in [0, 1]:
        if sum(arr[cur]):
            cnt += 1

    for _ in range(cnt):
        arr.pop()
        arr.insert(0, [0] * 4)


yello = [[0] * 4 for _ in range(6)]
red = [[0] * 4 for _ in range(6)]
K = int(input())
score = 0
red_dic = {1: 1, 2: 3, 3: 2}
for _ in range(K):
    t, i, j = map(int, input().split())

    drop(yello, t, j)
    drop(red, red_dic[t], i)

    score += check_score(yello)
    score += check_score(red)

    check_ceiling(yello)
    check_ceiling(red)

print(score)
cnt = sum([sum(a) for a in yello]) + sum([sum(a) for a in red])
print(cnt)
