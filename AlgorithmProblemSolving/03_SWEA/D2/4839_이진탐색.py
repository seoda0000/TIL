'''
 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 D2
 https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.
'''
import sys
sys.stdin = open('s_input.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    P, A, B = map(int,input().split())
    a = b = 0

    l, r = 1, P
    while l<=r:
        c = int((l+r)/2)
        a += 1  # 시도 횟수 증가
        if c == A: break
        elif c > A: # 왼쪽 탐색
            r = c
        else: # 오른쪽 탐색
            l = c

    l, r = 1, P
    while l<=r:
        c = int((l+r)/2)
        b += 1  # 시도 횟수 증가
        if c == B: break
        elif c > B: # 왼쪽 탐색
            r = c
        else: # 오른쪽 탐색
            l = c


    if a < b:
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')