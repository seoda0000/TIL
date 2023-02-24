"""
길이가 N인 수식이 있다. 수식은 0보다 크거나 같고, 9보다 작거나 같은 정수와 연산자(+, -, ×)로 이루어져 있다. 연산자 우선순위는 모두 동일하기 때문에, 수식을 계산할 때는 왼쪽에서부터 순서대로 계산해야 한다. 예를 들어, 3+8×7-9×2의 결과는 136이다.

수식에 괄호를 추가하면, 괄호 안에 들어있는 식은 먼저 계산해야 한다. 단, 괄호 안에는 연산자가 하나만 들어 있어야 한다. 예를 들어, 3+8×7-9×2에 괄호를 3+(8×7)-(9×2)와 같이 추가했으면, 식의 결과는 41이 된다. 하지만, 중첩된 괄호는 사용할 수 없다. 즉, 3+((8×7)-9)×2, 3+((8×7)-(9×2))은 모두 괄호 안에 괄호가 있기 때문에, 올바른 식이 아니다.

수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하시오. 추가하는 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.
"""

import sys

# 계산기 함수
def cal(string, num1, num2):
    if string == "+":
        nxt = int(num1) + int(num2)
    elif string == "-":
        nxt = int(num1) - int(num2)
    elif string == "*":
        nxt = int(num1) * int(num2)
    return nxt


def f(idx, result): # 해당 인덱스, 결과값
    if idx == N-1:  # 해당 인덱스가 마지막이면 결과값 반환
        ans.append(result)
        return
    elif idx+4 < N:  # 다음 숫자와 다다음 숫자의 결과와 계산
        num1 = lst[idx+2]
        num2 = lst[idx+4]
        nxt = cal(lst[idx+3], lst[idx+2], lst[idx+4])
        nxt_result = cal(lst[idx+1], result, nxt)
        f(idx+4, nxt_result)

    nxt_result = cal(lst[idx+1], result, lst[idx+2])  # 다음 숫자와 계산
    f(idx+2, nxt_result)


N = int(sys.stdin.readline())
lst = list(sys.stdin.readline())[:N]
ans = []
f(0, lst[0])
print(max(ans))