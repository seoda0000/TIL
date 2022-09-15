'''
5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 D2
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

이진 최소힙은 다음과 같은 특징을 가진다.

    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.

    - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.

    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.


1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하시오.

'''

import sys
sys.stdin = open('s_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    tree = [0] * (N+1)
    for n in range(1, N+1):
        tree[n] = arr[n]
        f = True
        while f:
            f = False
            if tree[n // 2] > tree[n]:
                tree[n], tree[n // 2] = tree[n // 2], tree[n]
                n//=2
                f = True
    a = N
    ans = 0
    while True:
        if a == 1:
            break
        ans += tree[a//2]
        a //= 2
    print(f'#{tc}', ans)