"""
https://www.acmicpc.net/problem/10951
백준 브론즈5 A+B - 4
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
