"""
백준 골드4 이중 우선순위 큐
https://www.acmicpc.net/problem/7662
이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다.
전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다.
이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다.
데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.

정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.

Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.
"""


import sys
import heapq

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    minheap = []
    maxheap = []
    delset = set()

    for i in range(n):
        W, num = input().split()
        num = int(num)

        if W == "I":
            heapq.heappush(minheap, (num, i, num))
            heapq.heappush(maxheap, (-num, i, num))
        elif num == 1:
            if maxheap:
                id = heapq.heappop(maxheap)[1]
                while maxheap and (id in delset):
                    id = heapq.heappop(maxheap)[1]
                delset.add(id)
        else:
            if minheap:
                id = heapq.heappop(minheap)[1]
                while minheap and (id in delset):
                    id = heapq.heappop(minheap)[1]
                delset.add(id)

    flag = 0
    if maxheap:
        _, id, nummax = heapq.heappop(maxheap)
    else:
        flag = 1
    while (flag == 0) and (id in delset):
        if maxheap:
            _, id, nummax = heapq.heappop(maxheap)
        else:
            flag = 1

    if flag:
        print("EMPTY")
    else:
        if minheap:
            _, id, nummin = heapq.heappop(minheap)
        while minheap and (id in delset):
            _, id, nummin = heapq.heappop(minheap)
        print(nummax, nummin)