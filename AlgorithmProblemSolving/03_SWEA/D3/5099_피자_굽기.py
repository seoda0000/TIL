'''
5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 D3
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

'''


import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = list(enumerate(lst, 1))       # 피자 순번과 함께 저장
    q = []

    while len(q) < N:                   # 화덕에 피자 넣기
        q.append(lst.pop(0))

    while q:
        n, c = q.pop(0)                 # 피자 꺼내기
        c //= 2
        if c > 0:                       # 치즈 남아있나 확인
            q.append((n, c))            # 남아있으면 다시 넣기
        else:
            if lst:
                q.append(lst.pop(0))    # 빈 자리에 나머지 피자 넣기

    print(f'#{tc}', n)
