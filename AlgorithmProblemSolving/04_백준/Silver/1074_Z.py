"""
https://www.acmicpc.net/problem/1074
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

"""


import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

sr = sc = 0
er = ec = 2**N
ansLst = []
for _ in range(N):
    if (sr + er)/2 > r and (sc + ec)/2 > c:
        ansLst.append(1)
        er = (sr+er)/2
        ec = (sc+ec)/2
    elif (sr + er)/2 > r:
        ansLst.append(2)
        er = (sr+er)/2
        sc = (sc+ec)/2
    elif (sr + er)/2 <= r and (sc + ec)/2 > c:
        ansLst.append(3)
        sr = (sr+er)/2
        ec = (sc+ec)/2
    else:
        ansLst.append(4)
        sr = (sr+er)/2
        sc = (sc+ec)/2
ans = 0
for n in range(N):
    ans += 2**(2*(N-1-n)) * (ansLst[n]-1)
print(int(ans))