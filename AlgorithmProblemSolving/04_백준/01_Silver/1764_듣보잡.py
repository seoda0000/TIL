"""
백준 실버4 듣보잡
https://www.acmicpc.net/problem/1764
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
"""
N, M = map(int, input().split())
st1 = set()
st2 = set()
for _ in range(N):
    st1.add(input())
for _ in range(M):
    st2.add(input())
ans = sorted(st1&st2)
print(len(ans))
for a in ans:
    print(a)