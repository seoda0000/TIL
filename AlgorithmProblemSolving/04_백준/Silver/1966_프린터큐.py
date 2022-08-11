'''
프린터 큐
https://www.acmicpc.net/problem/1966
백준 1966 실버3

여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
'''
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 리스트 길이, 목표 데이터 인덱스
    lst = deque(list(map(int, input().split())))  # 우선순위 리스트
    num = deque(range(1, N+1))   # 초기 인덱스 리스트
    ans = 1
    while lst: # 대기 리스트가 빌 때까지
        if lst[0] == max(lst):  # 첫 문서가 우선 순위가 가장 높은 경우 프린트
            if M == num.popleft()-1:  # 만약 프린트 되는 문서가 목표 데이터라면 break
                break
            lst.popleft()  # 인쇄. 우선순위 리스트에서 제거
            ans += 1
        else: # 첫 문서가 우선 순위가 가장 높지 않다면 맨 뒤로 이동
            lst.append(lst.popleft())
            num.append(num.popleft())
    print(ans)



