"""
https://www.acmicpc.net/problem/10709
백준 10709 실버5 기상캐스터

JOI시는 남북방향이 H 킬로미터, 동서방향이 W 킬로미터인 직사각형 모양이다.
JOI시는 가로와 세로의 길이가 1킬로미터인 H × W 개의 작은 구역들로 나뉘어 있다.
북쪽으로부터 i 번째, 서쪽으로부터 j 번째에 있는 구역을 (i, j) 로 표시한다.

각 구역의 하늘에는 구름이 있을 수도, 없을 수도 있다. 모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동한다.
오늘은 날씨가 정말 좋기 때문에 JOI시의 외부에서 구름이 이동해 오는 경우는 없다.

지금 각 구역의 하늘에 구름이 있는지 없는지를 알고 있다.
기상청에서 일하고 있는 여러분은 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 예측하는 일을 맡았다.

각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 구하여라.
"""
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
ans = [[-1] * M for _ in range(N)]

for i in range(N):
    temp = -1  # 구름 여부
    for j in range(M):
        if arr[i][j] == 'c':
            temp = 0  # 구름 생김
        else:
            if temp >= 0:
                temp += 1  # 구름이 있으면 시간 계산
        ans[i][j] = temp
for i in range(N):
    print(*ans[i])
