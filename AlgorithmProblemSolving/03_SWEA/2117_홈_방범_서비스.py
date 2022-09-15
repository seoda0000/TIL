'''
2117. [모의 SW 역량테스트] 홈 방범 서비스
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu

N*N 크기의 도시에 홈방범 서비스를 제공하려고 한다.

홈방범 서비스는 운영 상의 이유로 [Fig. 1]의 파란색 부분과 같이 마름모 모양의 영역에서만 제공된다.

또한, 홈방범 서비스를 제공하기 위해서는 운영 비용이 필요하다.

[Fig. 2]와 같이 서비스 영역의 크기 K 가 커질수록 운영 비용이 커진다.

운영 비용은 서비스 영역의 면적과 동일하며, 아래와 같이 구할 수 있다.

운영 비용 = K * K + (K - 1) * (K - 1)

도시를 벗어난 영역에 서비스를 제공해도 운영 비용은 변경되지 않는다.


홈방범 서비스를 제공받는 집들은 각각 M의 비용을 지불할 수 있어, 보안회사에서는 손해를 보지 않는 한 최대한 많은 집에 홈방범 서비스를 제공하려고 한다.

도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M, 도시의 정보가 주어진다.

이때, 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고,

그 때의 홈방범 서비스를 제공 받는 집들의 수를 출력하는 프로그램을 작성하라.
'''


import sys
sys.stdin = open('sample_input.txt', 'r')


def f(i, j, k, n):
    global ans
    tmp = 0
    for b in range(-k+1, k):
        t = -abs(b)+k-1
        for a in range(-t, t+1):
            if 0<=i+a<n and 0<=j+b<n:
                if arr[i+a][j+b] > 0:
                    tmp += 1
    return tmp


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for hk in range(1, 2*(N-1)):
        for hi in range(N):
            for hj in range(N):
                house = f(hi, hj, hk, N)
                if house * M - hk*hk - (hk-1)**2 >= 0:
                    if mx < house:
                        mx = house
    print(f'#{tc}', mx)

