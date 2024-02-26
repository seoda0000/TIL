N = int(input())
if N == 1:
    print("*")
else:
    odd = ("* " * ((N + 1) // 2)).rstrip()
    even = " *" * (N // 2)
    ans = [odd, even] * N
    print(*ans, sep="\n")
