T = int(input())


def make_formula(n, st):
    if len(st) == n:
        formulas.append(st)
        return

    for f in [' ', '+', '-']:
        make_formula(n, st + f)

    return


def calc(formula):
    f_lst = []
    num_stk = [1]

    for n in range(2, N + 1):

        if formula[n - 2] == ' ':
            before_num = num_stk.pop()
            num_stk.append(before_num * 10 + n)
        else:
            f_lst.append(formula[n - 2])
            num_stk.append(n)

    nf = len(f_lst)
    res = num_stk[0]

    for x in range(nf):
        if f_lst[x] == '+':
            res += num_stk[x + 1]
        else:
            res -= num_stk[x + 1]

    return res


for t in range(T):
    N = int(input())
    nums = list(range(1, N + 1))
    formulas = []
    make_formula(N - 1, '')
    ans = []
    for f in formulas:
        if not calc(f):
            ans_formula = ''
            for i in range(1, N):
                ans_formula += str(i) + f[i - 1]
            ans.append(ans_formula + str(N))
    print(*ans, sep='\n')
    if t < T-1:
        print()
