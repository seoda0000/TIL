<<<<<<< HEAD
# Python 기초 : 자료형과 자료구조


- [Python 기초](#Python-기초)
  * [프로그래밍 학습 마인드셋](#프로그래밍-학습-마인드셋)
    + [개념 구조화](#개념-구조화)
    + [소스코드 서치하고 활용하기](#소스코드-서치하고-활용하기)
- [프로그래밍이란?](#프로그래밍이란)
  * [프로그래밍의 정의](#프로그래밍의-정의)
  * [프로그래밍 언어란?](#프로그래밍-언어란)
  * [파이썬이란?](#파이썬이란)
  * [IDE](#IDE)
  * [코드 작성법](#코드-작성법)
    + [코드 스타일 가이드](#코드-스타일-가이드)
  * [변수(variable)](#변수(variable))
  * [연산자](#연산자)
    + [산술 연산자](#산술-연산자)
    + [멤버십 연산자](#멤버십-연산자)
    + [시퀀스형 연산자](#시퀀스형-연산자)
- [자료형](#자료형)
  * [수치형 자료 (Numeric Type)](#수치형-자료-(Numeric-Type))
    + [부동소수점](#부동소수점)
    + [진수 활용](#진수-활용)
    + [컴퓨터 지수 표현 방식](#컴퓨터-지수-표현-방식)
  * [문자열 자료형 (String Type)](#문자열-자료형-(String-Type))
    + [Escape sequence](#Escape-sequence)
    + [String interpolation](#String-interpolation)
  * [None](#None)
  * [Boolean](#Boolean)
    + [비교 연산자](#비교-연산자)
    + [논리 연산자](#논리-연산자)
  * [컨테이너(자료구조)](#컨테이너(자료구조))
    + [컨테이너의 분류](#컨테이너의-분류)
- [시퀀스형 컨테이너](#시퀀스형-컨테이너)
  * [리스트](#리스트)
  * [튜플](#튜플)
  * [Range](#Range)
  * [슬라이싱 연산자](#슬라이싱-연산자)
- [비시퀀스형 컨테이너](#비시퀀스형-컨테이너)
  * [Set과 Dictionary](#Set과-Dictionary)
  * [형변환이란?](#형변환이란?)
    + [암시적 변환](#암시적-변환)
    + [명시적 변환](#명시적-변환)
    + [컨테이너 형 변환](#컨테이너-형-변환)
- [프로그램 구성 단위](#프로그램-구성-단위)
    + [식별자(identifier)와 리터럴(literal)](#식별자(identifier)와-리터럴(literal))
    + [표현식(expression)과 문장(statement)](#표현식(expression)과-문장(statement))
    + [함수, 모듈, 패키지, 라이브러리](#함수)


---

## 프로그래밍 학습 마인드셋

### 개념 구조화

- 개념의 정의
- 개념의 포함 관계
- 두 개념의 차이점
- 기본기 탄탄히
- 동료 학습(Peer learning)
    - 친구에게 배운 개념 설명하기
    - 친구 코드의 에러 함께 해결하기
    - 지식의 빈틈 채우기

### 소스코드 서치하고 활용하기

- “수레바퀴를 두 번 만들지 마라”
- “거인의 어깨 위에서 프로그래밍 시작하기”

---

# 프로그래밍이란

## 프로그래밍의 정의

- 컴퓨터에게 일을 시키기 위해서 프로그램을 만드는 행위
- 프로그램 : 특정 작업을 수행하는 일련의 명령어들의 모음
- 프로그래머 : 프로그램을 만드는 사람

## 프로그래밍 언어란

- 언어 : 자신의 생각을 나타내고 전달하기 위해 사용하는 체계
- 기계어 : 0(전기신호가 들어오지 않음)과 1(전기신호가 들어옴)을 모든 것을 표현
- 컴퓨터 언어는 기계어가 아니다. → 프로그래밍 언어
- 특징
    - 사람이 이해할 수 있는 문자로 구성
    - 기본적인 규칙과 문법이 존재

- 소스코드
    - 프로그래밍 언어로 작성된 프로그램
- 번역기(interpreter, compiler)
    - 소스코드를 컴퓨터가 이해할 수 있는 기계어로 번역
    

## 파이썬이란

- 인터프리터 언어 : 통역하듯 1줄씩 변환
- 객체 지향 프로그래밍
    - 모든 것이 객체로 구현되어 있음

## IDE

- 통합 개발 환경. 개발에 필요한 다양하고 강력한 기능들을 모아둔 프로그램
    - ex) VScode, Pycharm

---

## 코드 작성법

### 코드 스타일 가이드

- PEP 8

[PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

- 스트링 통일하기

```python
print('hello')
a = 'apple'
```

- 들여쓰기 통일하기
    - 스페이스 4칸으로 통일 권장
- 주석(comment)을 다는 습관 들이기 ⭐⭐⭐

---

## 변수(variable)

- 변수 사용은 추상화에 도움
- 추상화
    - 코드의 가독성 증가
    - 의미 단위로 작성
    - 코드 수정에 용이
- `type()` : 데이터 타입 확인
- `id()` : 메모리 주소 확인
- 변수의 값 바꿔서 저장하기
1. 임시변수 활용

```python
x, y = 10, 20

tmp = x
x = y
y = tmp
print(x, y) # 20 10
```

2. Pythonic!

```python
x, y = 10, 20
y, x = x, y
print(x, y) # 20 10
```

## 연산자

### 산술 연산자

- +, -, *, /, //
- **연산자 우선순위** 주의
    1. `()`을 통한 grouping
    2. Slicing
    3. Indexing
    4. 제곱연산자 `**`
    5. 단항연산자 `+`, `-`(음수/양수 부호)
    6. 산술연산자 `+`, `/`, `%`
    7. 산술연산자 `+`, `-`
    8. 비교연산자, `in`, `is`
    9. `not`
    10. `and`
    11. `or`
- `divmod()` : 나눗셈과 관련된 함수

```python
print(divmod(5, 2))
quotient, remainder = divmod(5, 2) # (2, 1)
```

### 멤버십 연산자

- 요소가 시퀀스에 속해있는지 확인
- in, not in

### ****시퀀스형 연산자****

- ****산술 연산자 (+)****
- ****반복 연산자 (*)****

```python
[1, 2] + ['a'] # [1, 2, 'a']
(1, 2) + ('a',) # (1, 2, 'a')

[0] * 8 # [0, 0, 0, 0, 0, 0, 0, 0]
(1, 2) * 3 # (1, 2, 1, 2, 1, 2)
```

---

# 자료형

## 수치형 자료 (Numeric Type)

### 부동소수점

- 컴퓨터는 2진수를 사용하기 때문에 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음
- 부동소수점 해결법
1. 매우 작은 수보다 작은지 확인

```python
a = 3.2 - 3.1
b = 1.2 - 1.1
print(abs(a-b) <= 1e-10) # True
```

2. math 모듈 사용

```python
import math
print(math.isclose(a, b)) # True
```

### 진수 활용

- 2진수binary 0b
- 8진수octal 0o
- 16진수hexadecimal 0x

```python
print(0b10) #2
print(0o30) #24
print(0x10) #16
```

- `‘%알파벳’ %변수` :  변수에 저장되어있는 값을 특정 진수 문자열로 출력

```python
print('%b' %a) # 2진수
print('%o' %a) # 8진수
print('%x' %a) # 16진수

print('%X' %a) # 16진수 대문자
```


### 컴퓨터 지수 표현 방식

- e와 E 모두 사용 가능

```python
b = 314e-2
type(b)
print(b) # 3.14
```

## 문자열 자료형 (String Type)

### Escape sequence

- \뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
- String 안에서 사용

| str | 내용 |
| --- | --- |
| \n | 줄 바꿈 |
| \t | Tab |
| \r | 캐리지 리턴 |
| \o | NULL |
| \\ | \ |
| \' | 단일인용부호 (’) |
| \" | 이중인용부호 (”) |

```python
print('철수 \'안녕\'') # 철수 '안녕'
```

### String interpolation

- `f"{변수:.n+1}"` : 소숫점 n번째 자리까지 출력

```python
import datetime
today = datetime.datetime.now()
print(today)

print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
# 오늘은 22년 07월 18일

pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
# 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
```

cf) 컴퓨터는 시간을 숫자로 변환해서 기억한다. (timestamp)

- `format(변수, “.nf”)` : 반올림해서 소숫점 n번째 자리까지 출력

```python
a = float(input())
print(format(a, ".2f"))
print(f"{a:.3}")
```

## None

- 값이 없음을 표현
- 반환 값이 없는 함수에서 사용

## Boolean

### 비교 연산자

- \>, <, ≥, ≤, ==, ≠
- is : 객체 아이덴티티(OOP)
    - 동일한 object인지 확인 (id가 같은지)
    - 파이썬에서 -5 부터 256 까지의 id는 동일하다.
- is not : 객체 아이덴티티가 아닌 경우

### 논리 연산자

- and, or, Not
- 논리 연산자 주의사항
    - Falsy
        - False는 아니지만 False로 취급
        - 0, 0.0, (), [], {}, None, “”
        - Falsy 가 아닌 모든 값들은 True
    - 논리 연산자 우선순위
        - not, and, or 순으로 우선순위가 높음
    - 단축 평가 : 결과가 확실한 경우 두번째 값을 확인하지 않고 첫번째 값 반환
        - 단축평가가 가능하게 된 값 반환
    
    ```python
    print(3 and 5) # 5
    print(3 and 0) # 0
    print(0 and 3) # 0
    print(0 and 0) # 0
    
    print(5 or 3) # 5
    print(3 or 0) # 3
    print(0 or 3) # 3
    print(0 or 0) # 0
    
    a = 5 and 4
    print(a) # 4
    
    b = 5 or 3
    print(b) # 5
    
    c = 0 and 5
    print(b) # 0
    
    d = 5 or 0
    print(b) # 5
    
    'a' and 'b' # 'b'
    'a' or 'b' # 'a'
    
    ('a' and 'b') in 'aeiou' # False
    ('b' and 'a') in 'aeiou' # True
    ```
    

## 컨테이너(자료구조)

- 여러개의 값을 담을 수 있는 것
- 서로 다른 자료형을 저장할 수 있음 ex) list
- 분류
    - 순서가 있는 데이터(ordered) vs 순서가 없는 데이터(unordered)
    - 순서가 있다 ≠ 정렬되어 있다

### 컨테이너의 분류

- 시퀀스형 : 반복 가능
    - 리스트*
    - 튜플
    - 레인지
- 비시퀀스형 : 반복 불가능
    - 세트*
    - 딕셔너리*
- cf) * 가변형 : 값을 수정할 수 있다.

---

# 시퀀스형 컨테이너

## 리스트

- lst = [1, 2, 3]
- lst[index]
- lst[start\: end\:step]

## 튜플

- 주의사항
    - 단일 항목인 경우 : 값 뒤에 쉼표를 붙여야 함.
        - (1,)
    - 복수 항목인 경우 : 마지막에 쉼표를 넣는 것을 권장 (Trailing comma)
        - (1, 2, 3,)
- 튜플 대입
    - x, y = 1, 2
    - 파이썬 내부에서 튜플로 처리

## Range

- range(5, 1, -1)   # 5, 4, 3, 2

## 슬라이싱 연산자

- lst[::-1]    # 반대로 출력

# 비시퀀스형 컨테이너

## Set과 Dictionary

- Type
    - {} : 빈 dictionary
    - set() : 빈 set
- Set 연산자

| 연산자 | 내용 |
| --- | --- |
| \| | 합집합 |
| & | 교집합 |
| - | 차집합 |
| ^ | 대칭차집합 |
- key는 변경 불가능한 데이터만 활용 가능
    - string, int, float, bool, tuple, range
- value는 어떤 값이든 가능

```python
dic.update({'key':85})
```

## 형변환이란?

- 파이썬에서는 데이터 형태를 서로 변환할 수 있음.

### 암시적 변환

- 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
- ex) bool, numeric type(int, float)
- **암시적 변환은 의도하면 안된다. 코드에 있어서는 안됨!**

```python
print(True + 3) # 4
print(3 + 5.0) # 8.0
print(3 + complex(5, 5)) # 8 + 5j
```

### 명시적 변환

- 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우

```python
print('3' + 4) # TypeError
print(int('3') + 4) # 7
print(int('3.5') + 5) # Value Error

```

- 형식에 맞는 문자열만 float로 변환 가능

```python
print(float("3/4")) # Value Error : 
```

- str 변환 : 모두 가능. input()의 기본형은 str.

### 컨테이너 형 변환

- 컨테이너 간의 형 변환은 아래와 같이 가능

| before\after | string | list | tuple | range | set | dictionary |
| --- | --- | --- | --- | --- | --- | --- |
| string |  | o | o | x | o | x |
| list | o |  | o | x | o | x |
| tuple | o | o |  | x | o | x |
| range | o | o | o |  | o | x |
| set | o | o | o | x |  | x |
| dictionary | o | o (key only) | o (key only) | x | o (key only) |  |
- dictionary의 경우 key만 추출됨.

```python
d = {'name': 'ssafy', 'year': 2020}
print(str(d)) # {'name': 'ssafy', 'year': 2020}

print(list(d)) # ['name', 'year']
print(tuple(d)) # ('name', 'year')
print(set(d)) # {'name', 'year'}
```

---

# 프로그램 구성 단위

### 식별자(identifier)와 리터럴(literal)

- 식별자(identifier)
    - 변수, 함수, 클래스 등 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
    - 예약어 (파이썬 키워드 (명령어)) 불가능
- 리터럴(literal)
    - 읽혀지는 대로 쓰여있는 값 그 자체

```python
name = '김싸피'
# name은 식별자, 즉 변수
# '김싸피'는 리터럴
```

### 표현식(expression)과 문장(statement)

- 표현식(expression)
    - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
- 문장(statement)
    - 특정한 작업을 수행하는 코드 전체
    - 파이썬이 실행 가능한 최소한의 코드 단위
    - 표현식을 값을 생성하는 일부분이고, 문장은 특정 작업을 수행하는 코드 전체
- **“모든 표현식(expression)은 문장(statement)이다.”**

### 함수

### 모듈

- 모듈은 함수가 모여서 만들어진다.
- 모듈은 파이썬 파일 하나 단위.

### 패키지

=======
