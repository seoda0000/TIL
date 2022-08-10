'''
10866 덱
백준 실버4
https://www.acmicpc.net/problem/10866

정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

# import 처리
import sys
def input():
    return sys.stdin.readline().rstrip()

from collections import deque

T = int(input())

q = deque([])

for i in range(T):
    w = input()

    # 명령어 수행

    if w.startswith('push_front'):
        q.appendleft(int(w.replace('push_front ', '')))
    elif w.startswith('push_back'):
        q.append(int(w.replace('push_back ', '')))
    elif w == 'pop_front':
        if len(q) < 1:
            print(-1)
        else:
            print(q.popleft())
    elif w == 'pop_back':
        if len(q) < 1:
            print(-1)
        else:
            print(q.pop())
    elif w == 'size':
        print(len(q))
    elif w == 'empty':
        print(int(len(q) < 1))
    elif w == 'back':
        if len(q) < 1:
            print(-1)
        else:
            print(q[-1])
    elif w == 'front':
        if len(q) < 1:
            print(-1)
        else:
            print(q[0])
