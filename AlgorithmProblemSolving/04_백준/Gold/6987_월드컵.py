ans_lst = []


def check_row(i):  # 가능한 조합인지 체크
    if arr[i].count(1) != ipts[3 * i + 0]:
        return False
    if arr[i].count(-1) != ipts[3 * i + 2]:
        return False
    if arr[i].count(0) != ipts[3 * i + 1]:
        return False
    return True


def dfs(i, j):
    if i and j == i + 1:  # 행의 시작에서
        if not check_row(i - 1):  # 이전 행 점검
            return False

    if j == 6:  # 모든 칸이 채워졌을 때 종료
        if not check_row(5):
            return False
        return True

    if j == 5:
        ni = i + 1
        nj = ni + 1
    else:
        ni = i
        nj = j + 1

    for able in [-1, 0, 1]:  # 승패무 채우기 dfs
        arr[i][j] = able
        arr[j][i] = -able
        if dfs(ni, nj): return True
        arr[i][j] = INF
        arr[j][i] = INF
    return False


INF = 9
for _ in range(4):
    ipts = list(map(int, input().split()))
    arr = [[INF] * 6 for _ in range(6)]
    ans_lst.append(int(dfs(0, 1)))

print(*ans_lst)
