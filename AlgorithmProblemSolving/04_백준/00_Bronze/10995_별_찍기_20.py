N = int(input())
ans = []
odd = ("* "*N).rstrip()
even = " *"*N
for n in range(1, N+1):
    # 홀수일 경우
    if n%2:
        ans.append(odd)
    # 짝수일 경우
    else:
        ans.append(even)
print(*ans, sep="\n")
