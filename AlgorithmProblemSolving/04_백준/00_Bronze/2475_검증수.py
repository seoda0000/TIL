lst = list(map(int, input().split()))
print(sum([l ** 2 for l in lst]) % 10)
