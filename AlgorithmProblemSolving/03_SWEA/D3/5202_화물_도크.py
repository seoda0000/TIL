'''
5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 D3
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.

0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.

'''
import sys
sys.stdin = open('s_input (2).txt', 'r')

def f(ci, s):
    global ans
    if ci == N-1:
        if s > ans:
            ans = s
    for j in range(ci + 1, N):
        if lst[j][0] >= lst[ci][-1]:
            f(j, s+1)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort()
    ans = 0
    for i in range(N):
        f(i, 1)





    print(f'#{tc}', ans)
