'''
1232. [S/W 문제해결 기본] 9일차 - 사칙연산 D4
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD
사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다.
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과에 해당 연산자를 적용한다.

사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.

계산 중간 과정에서의 연산은 모두 실수 연산으로 한다.
'''


import sys
sys.stdin = open('input.txt', 'r')
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def f(n):
    if type(tree[n].data) == int:
        return tree[n].data
    if type(tree[tree[n].left].data) != int:
        a = f(tree[n].left)
    else:
        a = tree[tree[n].left].data
    if type(tree[tree[n].right].data) != int:
        b = f(tree[n].right)
    else:
        b = tree[tree[n].right].data

    if tree[n].data == '+':
        return a+b
    elif tree[n].data == '-':
        return a-b
    elif tree[n].data == '*':
        return a*b
    elif tree[n].data == '/':
        return a/b



for tc in range(1, 11):
    N = int(input())
    tree = [Node(0, 0, 0)] * (N + 1)
    for _ in range(N):
        ipt = input().split()
        if len(ipt) == 2:
            nth, num = map(int, ipt)
            tree[nth] = Node(num, 0, 0)
        elif len(ipt) == 4:
            nth, cal, left, right = ipt
            nth, left, right = map(int, (nth, left, right))
            tree[nth] = Node(cal, left, right)


    ans = int(f(1))
    print(f'#{tc}', ans)