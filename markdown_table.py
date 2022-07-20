# input으로 받아 리스트 만들기
entire_md = list(input().split("  "))

# 공백 제거하기
t_md = []
for item in entire_md:
    if len(item) >= 1:
        t_md.append(item.strip())

# #으로 시작하는 목차 추출하기
table_md = []
for item in t_md:
    if item[0] == "#":
        table_md.append(item)

# 링크 목차 구성하기
out = ""
for item in table_md:
    if "`" not in item:
        if "###" in item:
            out += "    + [" + item[4:] + "](#" + item[4:].replace(" ", "-") + ")\n"
        elif "##" in item:
            out += "  * [" + item[3:] + "](#" + item[3:].replace(" ", "-") + ")\n"
        elif "#" in item:
            out += "- [" + item[2:] + "](#" + item[2:].replace(" ", "-") + ")\n"
print(out)
