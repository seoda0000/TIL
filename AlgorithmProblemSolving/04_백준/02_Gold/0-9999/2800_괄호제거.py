'''
괄호제거
https://www.acmicpc.net/problem/2800
백준 골드 5 2800

어떤 수식이 주어졌을 때, 괄호를 제거해서 나올 수 있는 서로 다른 식의 개수를 계산하는 프로그램을 작성하시오.

이 수식은 괄호가 올바르게 쳐져 있다. 예를 들면, 1+2, (3+4), (3+4*(5+6))와 같은 식은 괄호가 서로 쌍이 맞으므로 올바른 식이다.

하지만, 1+(2*3, ((2+3)*4 와 같은 식은 쌍이 맞지 않는 괄호가 있으므로 올바른 식이 아니다.

괄호를 제거할 때는, 항상 쌍이 되는 괄호끼리 제거해야 한다.

어떤 식을 여러 쌍의 괄호가 감쌀 수 있다.
'''


from itertools import combinations

string = input()
lst = []
i = 0
stk = []
for s in string:
    if s == '(':    # n번째 괄호일 경우 n으로 표시
        i += 1
        lst.append(i)
        stk.append(i)
    elif s == ')':  # 짝을 맞춰 -n으로 표시
        lst.append(-stk.pop())
    else:
        lst.append(s)
num = i
n_range = range(1, num+1)
ans = []
for n in range(1, num+1):
    n_combi = combinations(n_range, n)  # n개의 괄호를 고르는 조합
    for c in n_combi:
        tmp = ""
        for j in lst:
            if type(j) == int:          # 괄호인 경우
                if j in c or -j in c:       # 조합에 포함되지 않으면 표기
                    continue
                elif j > 0:
                    tmp += '('
                else:
                    tmp += ')'
            else:
                tmp += j
        ans.append(tmp)
ans = list(set(ans))    # 중복값 제거
ans.sort()
for a in ans:
    print(a)