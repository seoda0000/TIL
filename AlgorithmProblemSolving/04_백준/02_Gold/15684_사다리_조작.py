"""
3:00~3:15 1차 구상
3:32~5:30 구현 및 디버깅

약 15분간 구상을 시도했으나 떠오르지 않아서 다른 문제를 풀고 돌아왔다.

dfs를 활용하여 풀려고 시도했으나 틀렸습니다와 시간초과가 떴다! 코드를 어떻게든 개선해보려고 노력한 게 딱히 의미가 없었던 것 같다.
시간초과는 아슬아슬하게 세이프 같은 건 없으니 확실한 가지치기나 아예 엎는 것 말고는 해결 방법이 없다는 점을 잊지 말아야 한다.

지난 주 스터디에서 나는 dfs로 풀고 상돈 프로님과 영석 프로님은 아이디어를 접목 시켰었는데,
익숙한 방식으로 시도하다가 시간 초과가 난 것 같다. 마지막 30분에서 멘탈을 잡고 두분의 아이디어를 적용했다.
지금 생각해보면 당연히 시간초과가 날 방법이었는데 왜 매달렸을까... 초기 구상 때 조금 더 시간을 두고 여러 방법을 떠올려보아야 한다.

그리고 잘 안 풀리더라도 타임스탬프를 잘 남겨두어야겠다... 환기가 될 듯
"""

import sys

input = sys.stdin.readline


def pick(cnt):
    global ans
    if len(temp) == cnt:
        if check_final():
            return True
        return False

    if not temp:
        bef = -1
    else:
        bef = temp[-1]

    for n in range(bef + 1, bN):
        ti, tj = blank_lst[n]
        if is_possible_ladder(ti, tj):
            arr[ti][tj] = 1
            temp.append(n)
            if pick(cnt):
                return True
            temp.pop()
            arr[ti][tj] = 0
    return False


def is_possible_ladder(li, lj):
    if lj < MAX_IDX:
        if lj < MAX_IDX - 1 and arr[li][lj + 1]:  # 이미 건너편에 사다리 있음 -> 불가
            return False
        elif lj > 1 and arr[li][lj - 1]:  # 이미 건너편에 있음
            return False
        else:
            return True
    return False


def check_final():
    start = tuple(range(1, MAX_IDX + 1))
    cur = list(start)

    for i in range(1, H + 1):
        for j in range(1, MAX_IDX):
            if arr[i][j]:
                cur[j - 1], cur[j] = cur[j], cur[j - 1]
    return start == tuple(cur)


MAX_IDX, start_row_cnt, H = map(int, input().split())
arr = [[0] * MAX_IDX for _ in range(H + 1)]
blank_lst = []

for _ in range(start_row_cnt):
    a, b = map(int, input().split())
    arr[a][b] = 1

for i in range(1, H + 1):
    for j in range(1, MAX_IDX):
        if arr[i][j] == 0:
            blank_lst.append((i, j))
bN = len(blank_lst)

temp = []

for i in range(4):
    if pick(i):
        ans = i
        break
else:
    ans = -1

print(ans)
