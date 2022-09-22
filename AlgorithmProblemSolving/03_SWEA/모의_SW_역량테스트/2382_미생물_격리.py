'''
2382. [모의 SW 역량테스트] 미생물 격리
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJyPoa6X9gDFAVG&contestProbId=AX-0L9zqQQQDFARi&probBoxId=AYNZfUaqmwADFATf&type=USER&problemBoxTitle=220923%3A+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B45&problemBoxCnt=3

정사각형 구역 안에 K개의 미생물 군집이 있다.

이 구역은 가로 N개, 세로 N개, 총 N * N 개의 동일한 크기의 정사각형 셀들로 이루어져 있다.

미생물들이 구역을 벗어나는걸 방지하기 위해, 가장 바깥쪽 가장자리 부분에 위치한 셀들에는 특수한 약품이 칠해져 있다.

가장자리의 빨간 셀은 약품이 칠해져 있는 셀이다.


   ① 최초 각 미생물 군집의 위치와 군집 내 미생물의 수, 이동 방향이 주어진다. 약품이 칠해진 부분에는 미생물이 배치되어 있지 않다. 이동방향은 상, 하, 좌, 우 네 방향 중 하나이다.

   ② 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.

   ③ 미생물 군집이 이동 후 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다.
       미생물 수가 홀수인 경우 반으로 나누어 떨어지지 않으므로, 다음과 같이 정의한다.
       살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
       따라서 군집에 미생물이 한 마리 있는 경우 살아남은 미생물 수가 0이 되기 때문에, 군집이 사라지게 된다,

   ④ 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다.
       합쳐 진 군집의 미생물 수는 군집들의 미생물 수의 합이며, 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향이 된다.
       합쳐지는 군집의 미생물 수가 같은 경우는 주어지지 않으므로 고려하지 않아도 된다.


M 시간 동안 이 미생물 군집들을 격리하였다. M시간 후 남아 있는 미생물 수의 총합을 구하여라.
'''


import sys
sys.stdin = open('sample_input (1).txt', 'r')
dr = [(0, 0), (-1, 0), (0, 1), (0, -1), (1, 0)]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    mp = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        i, j, v, d = map(int, input().split())
        if d == 2:
            mp[i][j].append((v, 4))
        elif d == 4:
            mp[i][j].append((v, 2))
        else:
            mp[i][j].append((v, d))
    for _ in range(M):
        tmp = [[[] for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if mp[i][j]:
                    v, d = mp[i][j][0]
                    ni = i + dr[d][0]
                    nj = j + dr[d][1]
                    if ni == 0 or nj == 0 or ni == N - 1 or nj == N - 1:
                        v //= 2
                        d = 5 - d
                    tmp[ni][nj].append((v, d))
        for i in range(N):
            for j in range(N):
                r = tmp[i][j]
                if len(r) > 1:
                    r.sort()
                    d = r[-1][1]
                    v = sum([rr[0] for rr in r])
                    tmp[i][j] = [(v, d)]

        mp = tmp

    ans = 0
    for tt in mp:
        for t in tt:
            if t:
                ans += t[0][0]


    print(f'#{tc}', ans)




