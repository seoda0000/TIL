'''
출석체크
https://www.acmicpc.net/problem/20438
백준 실버2 20438

코로나 바이러스로 인해 H 대학은 비대면 강의를 실시하고 있다. 조교를 담당하게 된 지환이는 출석체크 방식을 바꾸려고 한다.

학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다.

지환이가 한 학생에게 출석 코드를 보내게 되면, 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석을 할 수 있게끔 한다.

하지만, K명의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.

지환이는 무작위로 한 명의 학생에게 출석 코드를 보내는 행위를 Q번 반복한 뒤, 출석부 정리를 위해 특정 구간의 입장 번호를 받은 학생들 중에서 출석이 되지 않은 학생들의 수를 구하고 싶다.

많은 인원을 담당해서 바쁜 지환이를 위해 프로그램을 만들어주자!
'''

import sys
def input():
    return sys.stdin.readline().rstrip()

N, K, Q, M = map(int, input().split())
sleep = set(map(int, input().split()))
check = set(map(int, input().split())) - sleep   # 자는 사람 빼기
lst = [list(map(int, input().split())) for _ in range(M)]
ans = []
arr = [1] * (N+3)   # 출석부 1: 출석 안함 / 0: 출석함
for c in check:     # 출석
    i = 1
    while c*i < N+3:
        arr[c*i] = 0
        i += 1
for s in sleep:     # 자느라 출석 못한 사람
    arr[s] = 1
for m in range(M):  # 구간합 구하기
    s, e = lst[m]
    ans.append(sum(arr[s:e+1]))
for a in ans:
    print(a)