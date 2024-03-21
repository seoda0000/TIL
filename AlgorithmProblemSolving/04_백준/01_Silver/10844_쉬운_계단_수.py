'''
쉬운 계단 수
https://www.acmicpc.net/problem/10844
백준 실버1 10844

45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.
'''

import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
dic = {1:(0, 2), 2:(1, 3), 3:(2, 4), 4:(3, 5), 5:(4, 6), 6:(5, 7), 7:(6, 8), 8:(7, 9), 9:(8,), 0:(1,)}

lst = [0]+[1]*9
tmp = [0] * 10
ans , cnt = 9, 0
while cnt < N-1:
    tmp = [0] * 10
    for i in range(10):
        for j in dic[i]:
            tmp[j] += lst[i]
    lst = tmp
    cnt += 1
if cnt != 0:
    ans = sum(tmp)%1000000000
print(ans)