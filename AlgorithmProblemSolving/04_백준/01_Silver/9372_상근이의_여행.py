'''
상근이의 여행
https://www.acmicpc.net/problem/9372
백준 실버4 9372

상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다.

하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.

이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.

상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.
'''


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        input()

    print(N - 1)