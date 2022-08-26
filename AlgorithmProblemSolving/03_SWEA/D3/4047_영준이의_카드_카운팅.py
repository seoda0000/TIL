'''
4047. 영준이의 카드 카운팅 D3
https://swexpertacademy.com/main/code/problem/problemDetail.do

최근 영준이는 카드 게임에 꽂혀 있다.

영준이가 하는 카드 게임에는 한 덱의 카드가 필요한데 여기서 얘기하는 “한 덱”이란 스페이드, 다이아몬드, 하트, 클로버 무늬 별로 각각 A, 2~10, J, Q, K의 라벨 즉 4개의 무늬 별로

각각 13장씩 총 52장의 카드가 있는 모음을 의미한다.

편의상 A는 1, J, Q, K는 11, 12, 13으로 하여 1~13의 숫자가 카드에 적혀있다고 하자.

영준이는 몇 장의 카드를 이미 가지고 있는데 게임을 하기 위해서 몇 장의 카드가 더 필요한지 알고 싶어 한다.

그리고 이미 겹치는 카드를 가지고 있다면 오류를 출력하고자 한다.

지금 가지고 있는 카드의 정보가 주어지면 이 작업을 수행하는 프로그램을 작성하라.
'''


import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    s = input()
    n = len(s)
    dic = {'S':[], 'D':[], 'H':[], 'C':[]}
    for i in range(0, n, 3):            # 세글자씩 순회
        w, num = s[i], int(s[i+1:i+3])  # 무늬, 숫자
        if num in dic[w]:               # 중복일 때
            print(f'#{tc} ERROR')
            break
        else:
            dic[w].append(num)
    else:                               # 필요한 카드 수 출력
        print(f'#{tc}', 13-len(dic['S']), 13-len(dic['D']), 13-len(dic['H']), 13-len(dic['C']))
