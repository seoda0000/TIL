N = int(input())

for n in range(1, 2 * N):
    bcnt = abs(N-n)*2
    scnt = (2*N-bcnt)//2
    print('*'*scnt+' '*bcnt+'*'*scnt)
