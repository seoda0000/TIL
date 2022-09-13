'''
1231. [S/W 문제해결 기본] 9일차 - 중위순회 D4
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD
주어진 트리를 in-order 형식으로 순회해 각 노드를 읽으면 특정 단어를 알 수 있다.
주어진 트리를 in-order 형식으로 순회했을때 나오는 단어를 출력하라.
'''




class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def center(i):
    global ans
    if tree[i].left:
        center(tree[i].left)
    ans += lst[i]
    if tree[i].right:
        center(tree[i].right)




for tc in range(1, 11):
    N = int(input())
    tree = [Node(0, 0, 0)] * (N+1)
    lst = [''] * (N+1)
    ans = ''
    for i in range(N):
        ipt = input().split()
        if len(ipt) == 4:
            n, alpha, l, r = ipt
            tree[int(n)] = Node(int(n), int(l), int(r))
            lst[int(n)] += alpha
        elif len(ipt) == 3:
            n, alpha, l = ipt
            tree[int(n)] = Node(int(n), int(l), None)
            lst[int(n)] += alpha
        else:
            n, alpha = ipt
            lst[int(n)] += alpha
    center(1)
    print(f'#{tc}', ans)

