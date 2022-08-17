'''
직사각형
백준 2527 실버1
https://www.acmicpc.net/problem/2527

2차원 격자공간에 두 개의 꼭짓점 좌표로 표현되는 직사각형이 있다.
직사각형은 아래와 같이 왼쪽 아래 꼭짓점 좌표 (x, y)와 오른쪽 위 꼭짓점 좌표 (p, q)로 주어진다.

이 문제에서 모든 직사각형은 두 꼭짓점의 좌표를 나타내는 4개의 정수 x y p q 로 표현된다. 단 항상 x<p, y<q 이다.

여러분은 두 직사각형의 겹치는 부분이 직사각형인지, 선분인지, 점인지, 아니면 전혀 없는 지를 판별해서 해당되는 코드 문자를 출력해야 한다.

직사각형	a
선분	b
점	c
공통부분이 없음	d
'''


import sys
sys.stdin = open('input.txt', 'r')

for _ in range(4):
    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = map(int, input().split())

    # 겹치지 않는 경우
    if ax2 < bx1 or ay2 < by1 or ax1 > bx2 or ay1 > by2:
        print('d')

    # 꼭짓점만 겹치는 경우
    elif (ax2 == bx1 and (ay2 == by1 or ay1 == by2)) or (ax1 == bx2 and (ay1 == by2  or ay2 == by1)):
        print('c')

    # 선만 겹치는 경우
    elif ax1 == bx2 or ax2 == bx1 or ay1 == by2 or ay2 == by1:
        print('b')

   # 위 경우들이 아니면 면으로 겹침
    else:
        print('a')