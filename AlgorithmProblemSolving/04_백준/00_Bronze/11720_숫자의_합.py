# 백준 11720 브론즈4
# https://www.acmicpc.net/problem/11720
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

N = int(input())
q = sum(list(map(int, list(input()))))
print(q)