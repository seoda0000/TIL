"""
쉬워 보여서 설계를 대충함...
인덱스를 0부터 할 것인지 1부터 할 것인지 설계 단계에 정하고, 바꾸지 않아야 함. (중간에 바꿔서 난리가 남)
톱니바퀴 회전이 연속적으로 이루어진다는 것을 늦게 깨달아서 난항을 겪음. 연속적인 활동의 경우 v 배열을 활용할 수 있음. (문제를 잘 읽지 않음)
보통 4방향에서는 (n+3)%4를 이용했는데, 이를 그대로 습관처럼 써서 또 오류가 남. ((n+7)%8로 해야함)
인덱스 배열과 값 배열의 혼동이 있었음. 인덱스 형태를 손코딩으로 우선 정리하고 코드를 짜야 함. 인덱스 배열인 경우 변수명에 idx를 넣어 확실히 구분해야 함. (ls, rs -> idx_l, idx_r)
"""


def roll(n, r):
    v[n] = 1
    if r == 1:  # n번째 시계 방향 회전
        # n+1번째 반시계 회전
        if n < 4 and v[n + 1] == 0 and wheels[n + 1][idx_l[n + 1]] != wheels[n][idx_r[n]]:
            roll(n + 1, -1)

        # n-1번째 반시계 회전
        if n > 1 and v[n - 1] == 0 and wheels[n - 1][idx_r[n - 1]] != wheels[n][idx_l[n]]:
            roll(n - 1, -1)

        idx_l[n] = (idx_l[n] + 7) % 8
        idx_r[n] = (idx_r[n] + 7) % 8


    else:  # n번째 반시계 방향 회전

        # n+1번째 시계 회전
        if n < 4 and v[n + 1] == 0 and wheels[n + 1][idx_l[n + 1]] != wheels[n][idx_r[n]]:
            roll(n + 1, 1)

        # n-1번째 시계 회전
        if n > 1 and v[n - 1] == 0 and wheels[n - 1][idx_r[n - 1]] != wheels[n][idx_l[n]]:
            roll(n - 1, 1)

        idx_l[n] = (idx_l[n] + 1) % 8
        idx_r[n] = (idx_r[n] + 1) % 8

    return


wheels = [list()] + [list(map(int, input())) for _ in range(4)]
K = int(input())
orders = [list(map(int, input().split())) for _ in range(K)]

idx_l = [6] * 5  # 9시 방향 인덱스
idx_r = [2] * 5  # 3시 방향 인덱스

for n, r in orders:
    v = [0] * 5
    roll(n, r)

ans = 0
for n in range(1, 5):
    ans += wheels[n][(idx_l[n] + 2) % 8] * (2 ** (n - 1))

print(ans)
