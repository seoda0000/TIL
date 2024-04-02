"""
10:39 시작
11:09 구현 완료
11:23 배열 복사 오류 디버깅
11:24 제출
11:45 디버깅 - 종료 조건
12:52 백준 통과
"""


def check(bi, bj, bef_line, cnt):  # 점검 위치, 직전까지의 고객 순서, 만든 유실선의 개수
    global ans

    if bi < 0:  # 마지막까지 점검 완료
        if bef_line == list(range(M)):
            ans = min(ans, cnt)
        return

    if cnt == 3:  # 이젠 내려갈 수밖에 없다
        final_line = go_down(bef_line, bi)
        if final_line == list(range(M)):
            ans = min(ans, cnt)
        return

    if cnt >= ans:
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
