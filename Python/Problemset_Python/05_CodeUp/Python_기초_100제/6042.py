# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f"))
print(f"{a:.3}")

# format(수, ".2f")
# 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다. 
# f"{변수:.n+1}"
# 소숫점 n번째 자리까지 출력