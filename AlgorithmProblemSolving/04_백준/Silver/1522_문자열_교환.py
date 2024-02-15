"""
https://www.acmicpc.net/problem/1522
백준 실버1 1522 문자열 교환

a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램을 작성하시오.

이 문자열은 원형이기 때문에, 처음과 끝은 서로 인접해 있는 것이다.

예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.
"""
st = input()
N = len(st)
b_cnt = st.count('b')
ans = 1000

for i in range(N - b_cnt + 1):
    cost = b_cnt - st[i:i + b_cnt].count('b')
    ans = min(ans, cost)

for i in range(N - b_cnt + 1, N):
    cost = b_cnt - st[i:].count('b') - st[:b_cnt - N + i].count('b')
    ans = min(ans, cost)
print(ans)
