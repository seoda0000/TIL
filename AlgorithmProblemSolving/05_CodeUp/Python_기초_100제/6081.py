# 6081 : [기초-종합] 16진수 구구단 출력하기

"""
A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)
"""
def x_num(w):
    return ord(w)-55

word = input()
for i in range(1, 16):
    print('%s*%X=%X' %(word, i, x_num(word)*i))
