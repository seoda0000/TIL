"""
https://www.acmicpc.net/problem/2417
백준 실버4 2417 정수 제곱근

정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.
"""
N = int(input())

for i in range(int(N ** 0.5), N + 1):
    if i ** 2 >= N:
        print(i)
        break
