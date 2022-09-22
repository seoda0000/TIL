'''
5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.

이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
'''


import sys
sys.stdin = open('s_input (1).txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wlst = list(map(int, input().split()))
    tlst = list(map(int, input().split()))
    wlst.sort(reverse=True)
    tlst.sort(reverse=True)
    wf = tf = 0
    ans = 0
    while True:
        if tf == M:
            break
        if wf == N:
            break
        if wlst[wf] <= tlst[tf]:
            ans += wlst[wf]
            tf += 1
            wf += 1

        else:
            wf += 1
    print(f'#{tc}', ans)

