"""
14:00 시작
14:04 구상 완료
14:11 구현 완료
14:15 제출
"""


def get_dlst(d, g):
    dlst = [d]

    for _ in range(g):
        nd = len(dlst)

        for x in range(nd)[::-1]:
            dlst.append((dlst[x] + 1) % 4)

    return dlst


def draw(arr, x, y, dlst):
    ci, cj = x, y
    arr[ci][cj] = 1
    for d in dlst:
        ci, cj = ci + di[d], cj + dj[d]
        arr[ci][cj] = 1
    return


di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dlst = get_dlst(d, g)
    draw(arr, x, y, dlst)
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
            ans += 1
print(ans)
