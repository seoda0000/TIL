"""
10:01 시작
10:08 구상 완료
10:20 1차 구현 완료
10:28 먼지 값 갱신 오류 디버깅
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ci, cj = N // 2, N // 2
v = [[0] * N for _ in range(N)]
v[ci][cj] = 1
ans = 0
cd = 6
dust_blow_lst = [
    (1, 0.01, (3, -3)),
    (1, 0.07, (2, -2)),
    (2, 0.02, (2, -2)),
    (1, 0.1, (1, -1)),
    (2, 0.05, (0,))
]  # 칸 수, 퍼센트, 방향 조작 리스트

while True:
    if ci == 0 and cj == 0:
        break

    # 다음 목적지 찾기
    nd = (cd + 2) % 8
    ni, nj = ci + di[nd], cj + dj[nd]
    if v[ni][nj]:
        ni, nj = ci + di[cd], cj + dj[cd]
    else:
        cd = nd
    v[ni][nj] = 1
    start_dust = dust = arr[ni][nj]  # 날려보낼 먼지들

    for cnt, percent, d_lst in dust_blow_lst:
        for plus in d_lst:
            pd = (cd + plus) % 8
            nni, nnj = ni + di[pd] * cnt, nj + dj[pd] * cnt  # 날아갈 칸
            flow_dust = int(start_dust * percent)  # 날아갈 먼지
            dust -= flow_dust
            if OOB(nni, nnj):
                ans += flow_dust
            else:
                arr[nni][nnj] += flow_dust

    # a 처리
    arr[ni][nj] = 0
    nni, nnj = ni + di[cd], nj + dj[cd]
    if OOB(nni, nnj):
        ans += dust
    else:
        arr[nni][nnj] += dust

    ci, cj = ni, nj

print(ans)
