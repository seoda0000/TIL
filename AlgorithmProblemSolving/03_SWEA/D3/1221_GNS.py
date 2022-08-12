'''
1221. [S/W 문제해결 기본] 5일차 - GNS D3
https://swexpertacademy.com/main/code/problem/problemDetail.do
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.
'''

import sys
sys.stdin = open('s_input.txt', 'rt', encoding='UTF8')

T = int(input())
for _ in range(1, T+1):
    ipt = input().split()
    tc, N = ipt[0], int(ipt[1])
    print(tc)
    lst = input().split()
    dic = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    tmp = 0

    for n in range(10):
        s = tmp
        a = True
        for i in range(s, N):
            if lst[i] == dic[n]:
                if a:
                    tmp = i+1
                else:
                    lst[i], lst[tmp] = lst[tmp], lst[i]
                    tmp += 1
            else:
                a = False
    print(*lst)


