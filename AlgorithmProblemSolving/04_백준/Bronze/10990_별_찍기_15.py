N = int(input())
print((N - 1) * ' ' + "*")

for n in range(2, N + 1):
    bcnt1 = N - n
    bcnt2 = (n-1)*2-1
    print(bcnt1*" "+"*"+bcnt2*" "+"*")
