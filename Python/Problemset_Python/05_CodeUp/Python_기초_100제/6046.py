# 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기

n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 16 8 4 2 1
# 한칸씩 옆으로 옮겨서 값을 두배가 되게 한다. 그래서 비트시프트 연산이라고 한다.