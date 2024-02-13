from collections import defaultdict

st = input()
dic = defaultdict(int)

for s in st:
    dic[s] += 1
oddWord = []
for key, value in dic.items():
    if value % 2:
        oddWord.append(key)

if len(oddWord) > 1:
    print("I'm Sorry Hansoo")
else:
    ans = ""
    for key, value in sorted(dic.items()):
        ans += key * (value // 2)
    if oddWord:
        print(ans + oddWord[0] + ans[::-1])
    else:
        print(ans + ans[::-1])
