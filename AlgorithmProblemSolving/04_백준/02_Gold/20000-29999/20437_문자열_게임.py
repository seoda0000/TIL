"""
https://www.acmicpc.net/problem/20437
백준 골드5 문자열 게임
작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

알파벳 소문자로 이루어진 문자열 W가 주어진다.
양의 정수 K가 주어진다.
어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
위와 같은 방식으로 게임을 T회 진행한다.
"""
N = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
for _ in range(N):
    W = input();
    K = int(input())
    alphalst = [list() for _ in range(26)]
    minLength = 10001
    tuplelst = []
    startEndlst = []
    maxLength = 0

		# 알파벳 별 인덱스 기록
    for w in range(len(W)):
        n = alphabet.index(W[w])
        alphalst[n].append(w)

    for alpha in alphalst:
        if len(alpha) >= K:
						# K개의 알파벳이 포함된 구간 길이 찾기
            for n in range(len(alpha)-K+1):
                length = alpha[n+K-1]-alpha[n]+1
                maxLength = max(length, maxLength)
                minLength = min(length, minLength)

    if minLength == 10001 or maxLength == 0:
        print(-1)
    else:
        print(minLength, maxLength)