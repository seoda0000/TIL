N = int(input())
st = input()
stk = []
dic = {'(': ')', ')': '('}
for s in st:
    if stk and stk[-1] == dic[s]:
        stk.pop()
        if stk and (stk[-1] not in dic):
            continue
        else:
            stk.append(1)
    elif stk and stk[-1] != s:
        n = stk.pop()
        if stk and stk[-1] == dic[s]:
            stk.pop()
            if stk and (stk[-1] not in dic):
                stk.append(max(stk.pop(), n + 1))
            else:
                stk.append(n + 1)
        else:
            stk.append(n)
            stk.append(s)
    else:
        stk.append(s)
if len(stk) == 1 and (stk[-1] not in dic):
    print(stk[-1])
else:
    print(-1)
