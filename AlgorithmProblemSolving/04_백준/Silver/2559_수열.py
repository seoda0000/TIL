'''
수열
https://www.acmicpc.net/problem/2559
백준 실버3 2559

매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

'''
N, K = map(int, input().split())
lst = list(map(int, input().split()))
daysum = 0
for i in range(K):
    daysum += lst[i]
mx = daysum
for i in range(N-K):
    daysum += (lst[i+K] - lst[i])
    if mx < daysum:
        mx = daysum

print(mx)