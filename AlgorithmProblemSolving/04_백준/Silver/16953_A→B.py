"""
https://www.acmicpc.net/problem/16953
백준 실버2 16953 A → B

정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
"""

A, B = map(int, input().split())
dic = dict()
dic[A] = 1
q = [A]
ans = -1
while q:
    now = q.pop(0)
    if now == B:
        ans = dic[now]
        break

    if now * 2 <= B and not dic.get(now * 2):
        dic[now * 2] = dic[now] + 1
        q.append(now * 2)
    if now * 10 + 1 <= B and not dic.get(now * 10 + 1):
        dic[now * 10 + 1] = dic[now] + 1
        q.append(now * 10 + 1)
print(ans)
