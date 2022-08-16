'''
1216. [S/W 문제해결 기본] 3일차 - 회문2 D3
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi

"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.


[제약사항]

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
가로, 세로 각각에 대해서 직선으로만 판단한다.

'''

import sys
sys.stdin = open('input.txt', 'r')

def solve(lst):
    for i in range(100, ans-1, -1): # 100에서 ans 값까지 길이의 회문 검색
        for a in lst: # 행/열마다 탐색
            for j in range(101-i):
                if a[j:j+i] == a[j:j+i][::-1]: # 회문이면
                    return i # 길이 return

for _ in range(10):
    tc = input()
    arr = [input() for _ in range(100)]

    ans = 2
    ans = solve(arr) # 행 탐색시 최대 회문 길이.

    arr = list(zip(*arr))

    ans2 = solve(arr) # 열 탐색시 최대 회문 길이. 만약 행 탐색시 최대 길이보다 값이 작아지면 None을 반환한다.

    if ans2: # ans2 값이 있을 경우( 열 탐색시 수가 더 클 경우) 최대 회문 길이 갱신
        ans = ans2


    print(f'#{tc}', ans)

