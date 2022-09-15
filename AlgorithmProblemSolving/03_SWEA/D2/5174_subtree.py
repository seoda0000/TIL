'''
5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree D2
https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

트리의 일부를 서브 트리라고 한다.
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
'''


import sys
sys.stdin = open('s_input.txt', 'r')
def f(n):
    global ans
    ans += 1
    if ch1[n]:
        f(ch1[n])
    if ch2[n]:
        f(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    ipt = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    for e in range(0, E*2, 2):
        p, s = ipt[e], ipt[e+1]
        if ch1[p]:
            ch2[p] = s
        else:
            ch1[p] = s
    ans = 0
    f(N)
    print(f'#{tc}', ans)



