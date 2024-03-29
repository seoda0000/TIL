'''
스위치 켜고 끄기
https://www.acmicpc.net/problem/1244
백준 실버3 1244

1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다. <그림 1>에 스위치 8개의 상태가 표시되어 있다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다. 그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다. 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.

남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다.
학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

'''

N = int(input())
lst = list(map(int, input().split()))                       # 스위치 리스트

sN = int(input())
arr = [list(map(int, input().split())) for _ in range(sN)]  # 학생 리스트

for a in arr:
    gender, num = a
    if gender == 1:                      # 남자일 경우
        for i in range(num-1, N, num):
            lst[i] = (lst[i]+1)%2

    if gender == 2:                      # 여자일 경우
        k = 0
        while 0<=num-1-k<N and 0<=num-1+k<N and lst[num-1-k] == lst[num-1+k]:
            k += 1
        if k != 0:
            for i in range(num-k, num+k-1):
                lst[i] = (lst[i] + 1) % 2

while len(lst) > 20:  # 20개씩 출력
    print(*lst[:20])
    lst = lst[20:]
print(*lst)

"""
1년 후 풀이
exclusive or 이용
"""
def switch(gender, x):
    if gender == 1:  # 남자

        num = x
        for i in range(num, N+1, num):
            lst[i] ^= 1

    else:  # 여자

        s = e = x
        while True:
            if s - 1 <= 0 or e + 1 > N: break
            if lst[s - 1] == lst[e + 1]:
                s -= 1
                e += 1
            else:
                break
        for n in range(s, e + 1):
            lst[n] ^= 1

    return


N = int(input())
lst = [0] + list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, x = map(int, input().split())
    switch(gender, x)

for i in range(1, N + 1, 20):
    print(*lst[i:i + 20])