"""
백준 골드5 12908
텔레포트 3

수빈이는 크기가 무한대인 격자판 위에 살고 있다. 격자판의 각 점은 두 정수의 쌍 (x, y)로 나타낼 수 있다.

제일 처음에 수빈이의 위치는 (xs, ys)이고, 집이 위치한 (xe, ye)로 이동하려고 한다.

수빈이는 두 가지 방법으로 이동할 수 있다. 첫 번째 방법은 점프를 하는 것이다.
예를 들어 (x, y)에 있는 경우에 (x+1, y), (x-1, y), (x, y+1), (x, y-1)로 이동할 수 있다. 점프는 1초가 걸린다.

두 번째 방법은 텔레포트를 사용하는 것이다. 텔레포트를 할 수 있는 방법은 총 세 가지가 있으며, 미리 정해져 있다.
텔레포트는 네 좌표 (x1, y1), (x2, y2)로 나타낼 수 있으며, (x1, y1)에서 (x2, y2)로 또는 (x2, y2)에서 (x1, y1)로 이동할 수 있다는 것이다.
텔레포트는 10초가 걸린다.

수빈이의 위치와 집의 위치가 주어졌을 때, 집에 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

def f(x, y, i, t):               # 현재 위치, 몇번째 텔레포트인지, 시간
    global mnt
    if i == 3 or t > mnt:        # 종료
        t += abs(x-xe) + abs(y-ye)
        if t < mnt:
            mnt = t
        return t

    f(x, y, i+1, t)              # 텔레포트 이용하지 않고 pass
    for k in range(3):           # 텔레포트 이용
        if visited[k] == 0:          # 아직 이용하지 않은 텔레포트 이용
            visited[k] = 1
            a1, b1 = tlst[k][0]
            a2, b2 = tlst[k][1]
            f(a2, b2, i+1, t + abs(x-a1) + abs(y-b1)+10)         # 텔레포트 이용 A->B
            f(a1, b1, i + 1, t + abs(x - a2) + abs(y - b2) + 10) # 텔레포트 이용 B->A
            visited[k] = 0


xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
tlst = []
mnt = abs(xs-xe) + abs(ys-ye)  # 초기 시간 : 텔레포트 이용하지 않은 시간

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    tlst.append(((x1, y1), (x2, y2)))
visited = [0, 0, 0]

if mnt > 10:
    f(xs, ys, 0, 0)

print(mnt)


