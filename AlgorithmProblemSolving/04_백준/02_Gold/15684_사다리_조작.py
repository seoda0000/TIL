"""
실행시간: 3400 -> 2876
풀이시간: 135분 -> 70분

이전엔 조합->완전탐색으로 풀었는데, 이번엔 dfs로 풀었다. 조합보단 dfs가 명확한 문제인 것 같다.
종료조건의 순서 때문에 오류가 나서 틀렸다.
여러 종료조건에 잡힐 때는 가장 빡빡한 종료조건을 먼저 체크해야 한다. 잊지말자! -> 테케로 잡아내기 어렵기 때문에 언제나 유념하자


"""

"""
10:39 시작
11:09 구현 완료
11:23 배열 복사 오류 디버깅
11:24 제출
11:45 디버깅 - 종료 조건
12:48~52 디버깅 및 백준 통과
"""


def check(bi, bj, bef_line, cnt):  # 점검 위치, 직전까지의 고객 순서, 만든 유실선의 개수
    global ans

    if bi < 0:  # 마지막까지 점검 완료
        if bef_line == list(range(M)):
            ans = min(ans, cnt)
        return

    if cnt >= ans:
        return

    if cnt == 3:  # 이젠 내려갈 수밖에 없다
        final_line = go_down(bef_line, bi)
        if final_line == list(range(M)):
            ans = min(ans, cnt)
        return



    # 그냥 가기
    ni, nj, nxt_line = next(bi, bj, bef_line)
    check(ni, nj, nxt_line, cnt)

    if not arr[bi][bj]:  # 사다리 없음 -> 사다리 세우기

        # 사다리 세우기
        if bj > 0 and arr[bi][bj - 1]:
            pass
        elif bj < M - 2 and arr[bi][bj + 1]:
            pass
        else:
            arr[bi][bj] = 1
            ni, nj, nxt_line = next(bi, bj, bef_line)
            check(ni, nj, nxt_line, cnt + 1)
            arr[bi][bj] = 0

    return


def next(i, j, bef_line):  # i, j의 다음칸 return
    ni, nj, nxt_line = i, j, bef_line[:]
    if j == M - 1:  # 다음 열로
        ni += 1
        nj = 0

        for m in range(M - 1):  # 이전 라인 갱신
            if arr[i][m]:  # 유실선 있다
                nxt_line[m], nxt_line[m + 1] = nxt_line[m + 1], nxt_line[m]

    else:
        nj += 1

    if ni > H - 1:  # 다음칸이 없다
        ni, nj = -1, -1

    return ni, nj, nxt_line


def go_down(bef_line, nth):  # nth번째 취약지점부터 확인하며 끝까지 가서 성공여부 return
    nxt_line = bef_line[:]
    for i in range(nth, H):
        for m in range(M - 1):  # 이전 라인 갱신
            if arr[i][m]:  # 유실선 있다
                nxt_line[m], nxt_line[m + 1] = nxt_line[m + 1], nxt_line[m]
    return nxt_line


M, line_cnt, H = map(int, input().split())
arr = [[0] * M for _ in range(H)]

for _ in range(line_cnt):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
ans = M * H + 1

check(0, 0, list(range(M)), 0)

if ans == M * H + 1:
    ans = -1
print(ans)

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
