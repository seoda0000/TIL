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
            numA, id, numB = heapq.heappop(maxheap)
            while id in delset:
                numA, id, numB = heapq.heappop(maxheap)
            delset.add(id)
        else:
            numA, id, numB = heapq.heappop(minheap)
            while id in delset:
                numA, id, numB = heapq.heappop(minheap)
            delset.add(id)

    numA, id, nummax = heapq.heappop(maxheap)
    while id in delset:
        numA, id, nummax = heapq.heappop(maxheap)

    numA, id, nummin = heapq.heappop(minheap)
    while id in delset:
        numA, id, nummin = heapq.heappop(minheap)



