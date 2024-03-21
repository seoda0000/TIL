N = int(input())
mxcnt = 2 * N - 1
for n in range(1, 2 * N):
    cnt = mxcnt - abs(N - n)*2
    print((mxcnt-cnt)//2*' '+cnt*'*')
