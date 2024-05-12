'''
트리
https://www.acmicpc.net/problem/1068
백준 골드5 1068

트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다.
그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오.
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

'''


from collections import deque
N = int(input())
arr = list(map(int, input().split()))
D = int(input())
q = deque([D])
dsum = 1   # 지운 노드 수
while q:
    dnum = q.popleft()  # 지울 노드
    for a in range(N):
        if a == dnum or arr[a] == dnum:
            if a != dnum:
                q.append(a)  # 지울 노드의 자식 노드 enque
                dsum += 1
            arr[a] = None

delsum = len(set(arr))-2 if len(set(arr))-2 >= 0 else 0  # 부모 노드 수
ans = N - dsum - dell
if ans < 0:
    ans = 0
print(ans)
