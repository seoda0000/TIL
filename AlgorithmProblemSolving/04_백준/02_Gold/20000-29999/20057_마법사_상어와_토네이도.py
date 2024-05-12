"""
실행시간: 336 -> 368
풀이시간: 40분 -> 27분

최초 먼지에서 퍼센트를 계속 구했어야 했는데, 그때그때 먼지 값을 감소시켜서 오류가 났다.
문제 읽고 디버깅했다.

현재 방향에서 인덱스를 더하고 빼줘서 다음 방향을 선정하는 아이디어를 유지했다.
또한 떨어진 칸 수도 언제나 일정하니까 튜플로 만들어서 반복문을 돌려버렸다.
다음칸을 구할 때 칸 수를 분리하니 훨씬 깔끔하다. 아이디어를 활용해보자!

회오리 아이디어도 두 변씩 처리하는 것에서 방문 배열을 활용하는 것으로 변경해보았다.
통일된 로직이라 더 편한 것 같다. 변수명을 헷갈리지만 않으면...
"""

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

"""
13:55~14:35 구상+구현

처음에 a를 0.55 고정값으로 착각하고 잘못 설계했다... 마지막에 남은 값을 구해줘야 한다.
이 부분은 첫번째 테케로 충분히 잡을 수 있었는데...! 적어도 첫번째 테케는 꼼꼼히 읽자

나름대로 꼼꼼하게 설계했다고 생각했으나 위의 이슈 때문에 구현하면서 코드 순서를 그때그때 바꾸느라 혼란스러웠다...
그래도 주석을 미리 달아두니 작은 혼란만 겪은 것 같다.

변수명 때문에 머리 터질 것 같아서 무조건 의미 반영한 변수명을 사용했다

깡구현은 괜히 복잡하게 머리 쓰지 말고 겸허하게 하나하나 구현하자
중복 부분 함수화 시키고 싶은데 더 헷갈릴 것 같아서 그냥 내버려두겠다

시험 전에 물 많이 마시지 말자...(중요)
"""


def wind(xi, xj, xd):  # x좌표에서 xd 방향으로 바람 처리 후 다음 위치 return
    global ans

    ni, nj = xi + di[xd], xj + dj[xd]  # y 좌표
    remain = y = arr[ni][nj]
    side_of_xd = [(xd - 1) % 4, (xd + 1) % 4]  # xd의 양옆 방향 리스트
    xside_of_xd = [xd, (xd + 1) % 4]  # xd의 대각선 방향 리스트

    # [1] x 양 옆: 1%
    sand = int(y * 0.01)
    for d in side_of_xd:
        nni, nnj = xi + di[d], xj + dj[d]
        remain -= sand  # 어디론가 날아가긴 한다

        if (0 <= nni < N and 0 <= nnj < N):  # 범위 내
            arr[nni][nnj] += sand
        else:  # 범위 밖
            ans += sand

    # [2] y 양 옆: side_p 참조
    for k in range(2):
        sand = int(y * side_p[k])

        for d in side_of_xd:
            nni, nnj = ni + di[d] * (k + 1), nj + dj[d] * (k + 1)
            remain -= sand  # 어디론가 날아가긴 한다

            if (0 <= nni < N and 0 <= nnj < N):  # 범위 내
                arr[nni][nnj] += sand
            else:  # 범위 밖
                ans += sand

    # [3] y 앞 2칸: 5%
    sand = int(y * 0.05)
    nni, nnj = ni + di[xd] * 2, nj + dj[xd] * 2
    remain -= sand  # 어디론가 날아가긴 한다

    if (0 <= nni < N and 0 <= nnj < N):  # 범위 내
        arr[nni][nnj] += sand
    else:  # 범위 밖
        ans += sand

    # [4] y 양 대각선: 10%
    sand = int(y * 0.1)
    for d in xside_of_xd:
        nni, nnj = ni + ei[d], nj + ej[d]
        remain -= sand  # 어디론가 날아가긴 한다

        if (0 <= nni < N and 0 <= nnj < N):  # 범위 내
            arr[nni][nnj] += sand
        else:  # 범위 밖
            ans += sand

    # [5] y 앞 1칸: 나머지
    nni, nnj = ni + di[xd], nj + dj[xd]

    if (0 <= nni < N and 0 <= nnj < N):  # 범위 내
        arr[nni][nnj] += remain
    else:  # 범위 밖
        ans += remain

    # [6] y: 모래 다 날아감
    arr[ni][nj] = 0

    return ni, nj


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
ei = [-1, 1, 1, -1]  # 대각선 방향
ej = [-1, -1, 1, 1]
side_p = [0.07, 0.02]
ans = 0

xi, xj = N // 2, N // 2
xd = 0

for cnt in range(1, N):  # 1 1 2 2 3 3 ... N-1 N-1만큼 회오리 이동
    for _ in range(2):
        for _ in range(cnt):
            xi, xj = wind(xi, xj, xd)
        xd = (xd + 1) % 4

for _ in range(N):  # 마지막 N만큼 회오리 이동
    xi, xj = wind(xi, xj, xd)

print(ans)
