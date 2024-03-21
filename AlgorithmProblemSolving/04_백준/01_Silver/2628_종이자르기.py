'''
종이자르기
https://www.acmicpc.net/problem/2628
백준 실버5 2628

아래 <그림 1>과 같이 직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.

점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 그리고 2번 가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.

입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

'''


import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
n = int(input())
xlst = [0, w]
ylst = [0, h]

for _ in range(n):
    XorY, ipt = map(int, input().split())

    if XorY:            # 1일 경우 가로축 리스트에 추가
        xlst.append(ipt)
    else:               # 0일 경우 세로축 리스트에 추가
        ylst.append(ipt)

xlst.sort()             # 오름차순 정렬
ylst.sort()

maxw = maxh = 0

for x in range(len(xlst)-1):
    w = xlst[x+1] - xlst[x]
    if maxw < w:        # 최대 가로 길이 찾기
        maxw = w

for y in range(len(ylst)-1):
    h = ylst[y+1] - ylst[y]
    if maxh < h:        # 최대 세로 길이 찾기
        maxh = h
print(maxw * maxh)


"""
1년 후 풀이
"""

W, H = map(int, input().split())
N = int(input())
wlst = [0, H]
hlst = [0, W]
wlen = hlen = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a:
        hlst.append(b)
    else:
        wlst.append(b)

wlst.sort()
hlst.sort()

for w in range(1, len(wlst)):
    wlen = max(wlst[w]-wlst[w-1], wlen)

for h in range(1, len(hlst)):
    hlen = max(hlst[h]-hlst[h-1], hlen)

print(wlen * hlen)
