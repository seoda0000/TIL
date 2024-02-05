"""
https://www.acmicpc.net/problem/9935

백준 골드4 9935 문자열 폭발

상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
"""
st = input()
bomb = list(input())
Ns = len(st)
Nb = len(bomb)
stk = []
for s in st:
    stk.append(s)
    if s in bomb and len(stk) >= Nb and stk[-Nb:] == bomb:
        for _ in range(Nb):
            stk.pop()
if stk:
    print(''.join(stk))
else:
    print('FRULA')

"""
stk을 주기적으로 비우는 풀이
"""
st = list(input())
bomb = list(input())
Ns = len(st)
Nb = len(bomb)
stk = []
ans = []
for n in range(Ns):
    if st[n] in bomb:
        stk.append(st[n])
        if stk[-Nb:] == bomb:
            for _ in range(Nb):
                stk.pop()
    else:
        ans.extend(stk)
        ans.append(st[n])
        stk = []
ans.extend(stk)
if ans:
    print(''.join(ans))
else:
    print('FRULA')
