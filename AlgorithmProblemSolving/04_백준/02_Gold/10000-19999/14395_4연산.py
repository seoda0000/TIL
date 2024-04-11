"""
https://www.acmicpc.net/problem/14395

백준 골드5 14395 4연산
정수 s가 주어진다. 정수 s의 값을 t로 바꾸는 최소 연산 횟수를 구하는 프로그램을 작성하시오.

사용할 수 있는 연산은 아래와 같다.

s = s + s; (출력: +)
s = s - s; (출력: -)
s = s * s; (출력: *)
s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)

"""

from collections import defaultdict

s, t = map(int, input().split())
if s == t:
    print(0)
else:
    ops = defaultdict(str)
    q = []
    if s * s <= t and not ops[s * s]:
        ops[s * s] = '*'
        q.append(s * s)
    if s + s <= t and not ops[s + s]:
        ops[s + s] = '+'
        q.append(s + s)
    if not ops[0]:
        ops[0] = '-'
    if s != 0 and not ops[1]:
        ops[1] = '/'
        q.append(1)
    while q:
        now = q.pop(0)
        if now == t:
            print(ops[now])
            break
        if now * now <= t and ops[now * now] == '':
            ops[now * now] = ops[now] + '*'
            q.append(now * now)
        if now + now <= t and ops[now + now] == '':
            ops[now + now] = ops[now] + '+'
            q.append(now + now)
    else:
        print(-1)
