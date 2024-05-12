'''
가장 가까운 공통 조상
https://www.acmicpc.net/problem/3584
백준 골드4 3584

루트가 있는 트리(rooted tree)가 주어지고,
그 트리 상의 두 정점이 주어질 때 그들의 가장 가까운 공통 조상(Nearest Common Anscestor)은 다음과 같이 정의됩니다.
두 노드의 가장 가까운 공통 조상은, 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드를 말합니다.
루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요
'''

import sys
def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    parent = [0] * (N+1)
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A
    n1, n2 = map(int, input().split())
    lst1 = [n1]
    lst2 = [n2]
    ans = 0
    while True:
        p1, p2 = parent[n1], parent[n2]
        if p1 == p2:
            ans = p1
            break
        elif p1 in lst2:
            ans = p1
            break
        elif p2 in lst1:
            ans = p2
            break
        lst1.append(p1)
        lst2.append(p2)
        n1, n2 = p1, p2
    print(ans)