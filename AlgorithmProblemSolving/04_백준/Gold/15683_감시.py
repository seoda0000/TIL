"""
9:40 구상 완료
10:01 1차 구현 완료
10:06 디버깅 및 테케 체크 완료
10:09 틀렸습니다 후 디버깅

테케 다 맞았는데 틀렸습니다 떠서 깜짝 놀랐다! 구현 방법에 따라 이럴 수 있구나...
idx를 증가하기 전에 방문 처리를 해야 하는데 그러지 않아서 오류가 생겼다.
엣지 케이스라서 공개 tc에도 없었던 것 같다. 헐...
안일하게 살지 말고 제출 전 로직 검토를 꼼꼼히 하자
값 증감에 유의하자
"""


def dfs(idx, v):
    global ans
    if idx > LAST_IDX:
        # cctv 모두 지정 완료 시 사각지대 세기
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0 and v[i][j] == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return

    cx, ci, cj = cctv_dic[idx]

    for dlst in cctv_dir[cx]:
        # v에 표기
        for d in dlst:
            check(ci, cj, d, 0, idx)
        dfs(idx + 1, v)  # 다음 cctv로
        # v 원상복구
        for d in dlst:
            check(ci, cj, d, idx, 0)

    return


def check(si, sj, sd, bef, aft):  # si, sj에서 sd방향쪽으로 확인하며 bef를 aft로 바꾸기

    ci, cj = si, sj
    while True:
        ni, nj = ci + di[sd], cj + dj[sd]

        if not (0 <= ni < N and 0 <= nj < M):
            break
        if arr[ni][nj] == 6:
            break
        if v[ni][nj] == bef:
            v[ni][nj] = aft
        ci, cj = ni, nj

    return


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctv_dic = dict()
idx_lst = []
cctv_dir = {
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 2), (1, 3)],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
    5: [(0, 1, 2, 3)]
}
idx = 1
v = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 5:
            # 5: 한 경우 뿐이니 미리 4방향 v 표시
            for d in range(4):
                check(i, j, d, 0, -1)

        elif 1 <= arr[i][j] <= 4:
            # 방향 전환을 위한 정보 저장
            cctv_dic[idx] = (arr[i][j], i, j)
            idx += 1

LAST_IDX = idx - 1
ans = N * M
dfs(1, v)
print(ans)
