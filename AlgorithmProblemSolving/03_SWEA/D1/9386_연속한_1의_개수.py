'''
연속한 1의 개수
SWEA 9386 D1
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do

N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
'''
T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = input() + '0'  # 뒤에 0 추가

    ans = 0
    tmp = 0
    for i in lst:
        if i == '1': # 1이면 더하기
            tmp += 1
        else: # 0이면 비교 후 합계깞 초기화
            if ans < tmp:
                ans = tmp
            tmp = 0
    print(f'#{case} {ans}')