'''
수열
https://www.acmicpc.net/problem/2491
백준 실버4 2491

0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다.

그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라.
'''

N = int(input())
lst = list(map(int, input().split()))

flag = 0    # 1 증가수열 2 감소수열
tmp = 1     # 부분합 시작값
mx = 2      # 수열 길이 최대값
eq = 1      # 같은 숫자 수열 길이 (ex. 3 3 3)
for i in range(1, N):
    if lst[i-1] < lst[i]:    # 증가 수열
        if flag == 2:        # 이전까지 감소하고 있었을 경우
            tmp = eq         # 같은 숫자 수열 길이로 초기화
        flag = 1
        tmp += 1
        eq = 1               # 같은 숫자 수열 길이 초기화

    elif lst[i-1] > lst[i]:  # 감소 수열
        if flag == 1:        # 이전까지 증가하고 있었을 경우
            tmp = eq         # 같은 숫자 수열 길이로 초기화
        flag = 2
        tmp += 1
        eq = 1               # 같은 숫자 수열 길이 초기화

    else:                    # 같을 경우
        tmp += 1
        eq += 1

    if tmp > mx:             # 최대값 갱신
        mx = tmp

if N == 1:                   # 수열 길이가 1일 경우 수정
    mx = 1
print(mx)