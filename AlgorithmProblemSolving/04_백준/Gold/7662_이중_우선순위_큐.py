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