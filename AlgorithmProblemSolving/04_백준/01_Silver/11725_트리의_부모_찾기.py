'''
트리의 부모 찾기
https://www.acmicpc.net/problem/11725
백준 실버2 11725

루트 없는 트리가 주어진다.
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
'''


import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def dfs(x, p):
    if ans[x] == 0:
        ans[x] = p        # 부모노드 기록
        for t in lst[x]:  # 여태 저장한 리스트의 수들의 부모노드를 x로 설정
            if ans[t] == 0:
                dfs(t, x)

N = int(input())-1
lst = deque([[0], [1]] + [[] for _ in range(N)])
ans = deque([0, 1] + [0] * N)  # 부모노드 기록 리스트
for _ in range(N):
    a, b = map(int, input().split())
    if ans[a]:                 # 상대값의 부모노드가 정해진 경우
        dfs(b, a)              # 부모노드로 기록
    elif ans[b]:
        dfs(a, b)
    else:
        lst[a].append(b)  # 둘 다 결정되지 않았다면 일단 리스트에 저장
        lst[b].append(a)

for s in range(2, N+2):
    print(ans[s])



