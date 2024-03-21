"""
백준 실버 1 20364
부동산 다툼
https://www.acmicpc.net/problem/20364


이진 트리 모양의 땅으로 이루어진 꽉꽉마을에는 오리들이 살고 있다. 땅 번호는 다음과 같이 매겨진다.

루트 땅의 번호는 1이다.
어떤 땅의 번호가 K라면, 왼쪽 자식 땅의 번호는 2 × K, 오른쪽 자식 땅의 번호는 2 × K + 1이다.
어느날 오리들끼리 부동산 다툼이 일어나서 꽉꽉마을 촌장 경완이가 해결책을 가져왔고, 그 내용은 다음과 같다.

오리들을 한 줄로 대기시킨다. 맨 처음 오리들은 1번 땅에 위치해 있다.
오리들이 서있는 순서대로 원하는 땅을 가지도록 한다.


만약, 한 오리가 원하는 땅까지 가는 길에 이미 다른 오리가 점유한 땅이 있다면 막대한 세금을 내야 하는 이유로 해당 땅을 지나가지 못해 그 오리는 땅을 가지지 못한다. 오리가 원하는 땅까지 가는 길에는 오리가 원하는 땅도 포함된다.

경완이의 해결책대로 땅 분배를 했을 때 각 오리별로 원하는 땅을 가질 수 있는지, 가질 수 없다면 처음 마주치는 점유된 땅의 번호를 구해보자.
"""


import sys

def f(num, k):
    if num == 0:
        return (0, k)
    if chk[num] == 1:
        return f(head[num], num)
    else:
        return f(head[num], k)


N, Q = map(int, sys.stdin.readline().split())
head = [i//2 for i in range(N+1)]
chk = [0] * (N+1)

ans = []
for _ in range(Q):
    target = int(sys.stdin.readline())
    z, nt = f(target, 0)
    if nt == 0:
        chk[target] = 1
        ans.append(0)
    else:
        ans.append(nt)

for a in ans:
    print(a)