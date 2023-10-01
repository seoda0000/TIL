# 구글 스프레드 시트 JSON 포멧 문자열로 만들기

lines = []
while True:
    line = input("여러 줄의 텍스트를 입력하세요 (종료하려면 빈 줄 입력): ")
    if line:
        lines.append(line)
    else:
        break
outputString=""
for line in lines:
    strings = list(line.split("\t"))
    for s in strings:
        outputString += '"'+s+'",'

print(outputString)
