"""
## 요세푸스 문제
https://www.acmicpc.net/problem/1158

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""
#
#
# N, M = map(int, input().split())
# lst = list(range(1, N+1))
#
# i = M-1
# ans = []
#
# while lst:
#     n = len(lst)
#     while i > n-1:
#         i -= n
#     ans.append(lst[i])
#     lst.pop(i)
#     i = i-1+M
# ans = ", ".join(map(str, ans))
# print(f"<{ans}>")
def calculateScore(text, prefixString, suffixString):
    # Write your code here
    tN = len(text)
    pN = len(prefixString)
    sN = len(suffixString)
    text += "x"
    dic = dict()
    for p in range(tN):
        for k in range(p+1, tN+1):
            target = text[p:k]
            print(target, p, k)
            preScore = sufScore = 0
            for p in range(1, pN+1):
                if prefixString[-p:] in target:
                    preScore = p
                else:
                    break
            for s in range(1, sN+1):
                if suffixString[:s] in target:
                    sufScore = s
                else:
                    break
            if preScore + sufScore > 0:
                dic[target] = preScore + sufScore
    print(dic)

calculateScore("nothing", "bruno", "thing")