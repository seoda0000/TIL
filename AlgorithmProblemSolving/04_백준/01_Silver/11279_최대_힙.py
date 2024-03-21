'''
최대힙
백준 실버2 11279
https://www.acmicpc.net/problem/11279

널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''


import sys
sys.stdin = open('input.txt', 'r')
def input():
    return sys.stdin.readline().rstrip()
import heapq

N = int(input())
heap = []
for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:                           # heap에 원소가 있으면 출력
            print(-heapq.heappop(heap))
        else:                              # 없으면 0 출력
            print(0)
    else:                                  # push (최소힙이 기본이므로 음수값으로 넣어야 최대힙이 된다.)
        heapq.heappush(heap, -x)