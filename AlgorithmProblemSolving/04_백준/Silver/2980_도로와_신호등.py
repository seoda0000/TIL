'''
도로와 신호등
https://www.acmicpc.net/problem/2980
백준 실버4 2980

상근이는 트럭을 가지고 긴 일직선 도로를 운전하고 있다. 도로에는 신호등이 설치되어 있다. 상근이는 각 신호등에 대해서 빨간 불이 지속되는 시간과 초록 불이 지속되는 시간을 미리 구해왔다. (빨강색과 초록색 불빛은 무한히 반복된다)

상근이의 트럭이 도로에 진입했을 때, 모든 신호등의 색상은 빨간색이고, 사이클이 막 시작한 상태이다. 상근이는 1초에 1미터를 움직인다. 신호등의 색상이 빨간색인 경우에는 그 자리에서 멈추고 초록색으로 바뀔때 까지 기다린다.

상근이가 도로의 끝까지 이동하는데 걸리는 시간을 구하는 프로그램을 작성하시오. 도로의 시작은 0미터이고, 끝은 L미터인 지점이다.
'''


N, L = map(int, input().split())

# 신호등 배열 : (신호등 위치, 빨간불 시간, 초록불 시간)
arr = [list(map(int, input().split())) for _ in range(N)]  
arr = [(0, 0, 0)] + arr + [(L, 0, 1)]   # 출발점과 도착점 추가
past = 0                                # 소모한 시간

for a in range(1, N+2):
    past += arr[a][0] - arr[a-1][0]    # 다음 신호등까지의 거리만큼 시간 추가
    R, G = arr[a][1], arr[a][2]
    cycle = R + G                      # 신호등의 한 사이클

    if past % cycle < R:               # 새로운 사이클 시작 후 지난 시간이 R보다 작을 경우
        past += R - past % cycle       # 남은 시간만큼 기다림

print(past)