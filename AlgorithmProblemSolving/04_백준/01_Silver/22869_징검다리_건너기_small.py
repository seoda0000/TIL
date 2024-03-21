'''
징검다리 건너기 (small)
https://www.acmicpc.net/problem/22869
백준 실버1 22869

N개의 돌이 일렬로 나열 되어 있다. $N$개의 돌에는 수 A_{1} A_{2} ... A_{i} ... A_{N}로 부여되어 있다.
가장 왼쪽에 있는 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너가려고 한다.

항상 오른쪽으로만 이동가능하다.
i번째 돌에서 j(i < j)번째 돌로 이동할 때 (j - i) × (1 + |A_{i} - A_{j}|) 만큼 힘을 쓴다.
돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대 K$다.
이때, 가장 왼쪽 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너갈 수 있는지 구해보자.
'''
N, K = map(int, input().split())
lst = list(map(int, input().split()))
b = [1] + [0]*(N-1)
ans = 'YES'
for i in range(1, N):
    for j in range(i):
        if b[j] == 1 and (i-j) * (1+abs(lst[i]-lst[j])) <= K:
            b[i] = 1
            break
if b[-1] == 0:
    ans = "NO"
print(ans)
