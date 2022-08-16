- [**문자열**](#문자열)
  * [문자의 표현](#문자의-표현)
    + [ASCII 문자 인토딩 표준](#**ASCII-문자-인토딩-표준**)
    + [확장 아스키](#**확장-아스키**)
    + [유니코드](#**유니코드**)
  * [문자열의 분류](#문자열의-분류)
  * [파이썬에서의 문자열](#파이썬에서의-문자열)
    + [파이썬에서의 문자열 처리](#파이썬에서의-문자열-처리)
    + [파이썬에서 문자열 뒤집기](#파이썬에서-문자열-뒤집기)
    + [문자열 비교하기](#문자열-비교하기)
    + [문자열 숫자를 정수로 변환](#문자열-숫자를-정수로-변환)
    + [int와 같은 atoi 함수 만들기](#int와-같은-atoi-함수-만들기)
- [**패턴 매칭**](#패턴-매칭)
    + [고지식한 패턴 검색 알고리즘 Brute Forece](#고지식한-패턴-검색-알고리즘-Brute-Forece)
    + [카프-라빈 알고리즘](#카프-라빈-알고리즘)
    + [KMP 알고리즘](#KMP-알고리즘)
    + [보이어-무어 알고리즘](#보이어-무어-알고리즘)
- [**문자열 암호화**](#문자열-암호화)
- [**문자열 압축**](#문자열-압축)


---


# 문자열

## 문자의 표현

- 문자에 대응되는 숫자로 저장.
- 영어는 대소문자 합쳐서 52 → 6비트(64가지)면 모두 표현 가능 : **코드체계**

### **ASCII 문자 인토딩 표준**

- 7 bit 인코딩 : 128문자 표현
- 33개 제어 문자
- 95개 출력 가능한 문자 (32~126)

### **확장 아스키**

- 8 bit 인코딩. 추가적인 문자 표현
- 해독하려면 별도의 설계 필요

### **유니코드**

- 다국어 처리를 위한 표준
- UCS-2, UCS-4 : 유니코드를 저장하는 변수의 크기를 정의
- 적당한 외부 인코딩 필요
    - UTF-8(web, 파이썬 기본), UTF-16(windows, java), UTF-32(unix)
    

---

## 문자열의 분류

- **fixed length**
- **variable length**
    - length controlled : java
    - delimited : c

<aside>
🤖 `실행파일` ← `모듈`(파일) ← **`함수`** ← `문`(statement: if i>3) ← `식`(expression : i>3) ← `연산자` & `피연산자`(상수)

</aside>

---

## 파이썬에서의 문자열

### 파이썬에서의 문자열 처리

- 시퀀스 자료형 (인덱싱, 슬라이싱 연산 사용 가능)
- `replace()`, `split()`, `isalpha()`, `find()`
- immutable : 요소값 불변
- UTF-8로 저장

<br>

### 파이썬에서 문자열 뒤집기

```python
s = 'Reverse this strings'  # 'sgnirts sith esreveR

s = s[::-1] # 정답
s = 'abcd'
s = list(s)
s.reverse() # reverse는 list에서 사용 가능
s = ''.join(s)
```

<br>

### 문자열 비교하기

```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1 == s2) # True
print(s1 == s3) # False
print(s1 == s4) # True
print(s1 == s5) # True

print(s1 is s2) # True
print(s1 is s3) # False
print(s1 is s4) # True
print(s1 is s5) # False
```

<br>

### 문자열 숫자를 정수로 변환

```python
# 문자열 -> 숫자
int('123')
float('3.14')

# 숫자 -> 문자열
str(123)
print(repr(123), type(repr(123))) # 123 <class 'str'>
# repr : 문자열로 객체를 다시 생성. eval() 함수로 원상태로 복귀 가능

a = "Life is too short"
str(a)  # 'Life is too short'
repr(a)  # "'Life is too short'"

a = datetime.datetime(2017, 9, 27)
str(a)  # '2017-09-27 00:00:00'
repr(a)  # 'datetime.datetime(2017, 9, 27, 0, 0)'
```

<br>

### int와 같은 atoi 함수 만들기

```python
# 문자열 숫자를 정수로
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0') # 자릿수 적용
    return i

# 정수를 문자열 숫자로
def itoa(n):
    s = ""
    while n%10:
        s = chr(n%10 + ord('0')) + s
        n//=10
    return s
```

<br>

---

# 패턴 매칭

### 고지식한 패턴 검색 알고리즘 Brute Forece

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식
- 한칸씩 이동
- 시간 복잡도 : O(MN)

<br>

### 카프-라빈 알고리즘

- 문자열의 해시 값 이용
    - 해시 값 : 문자열의 각 문자(ASCII TABLE 값)에 특정 수의 제곱 수를 차례대로 곱하여 모두 더하기
    - ABCD의 해시 값 : 65 * 3^3 + 66 * 3^2 + 67 * 3^1 + 68 * 3^0 = 2618
    - ABED의 해시 값 : 65 * 3^3 + 66 * 3^2 + 69 * 3^1 + 68 * 3^0 = 2624

<br>


### KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함
    - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
    - 불일치 발생 다음 위치로 jump
- 시간 복잡도 : O(M+N)

<br>


### 보이어-무어 알고리즘

- 문자열 오른쪽에서 왼쪽을 비교
- 불일치할 경우 미리 정해둔 skip배열을 참고하여 jump
- 패턴의 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동거리는 패턴의 길이만큼이 된다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f82ebc6-66bf-43dc-9f4f-26ed37fa43f0/Untitled.png)
    
- 시간 복잡도 : O(n)~O(mn)

<br>


---

# 문자열 암호화

- 시저 암호 : n칸씩 이동)
- 단일 치환 암호 : 문자 변환표를 이용
- bit열의 암호화 : 배타적 논리합 연산 사용. (평문과 암호문의 XOR이 키)
    
    
    | x | XOR | y |
    | --- | --- | --- |
    | 0 | 0 | 0 |
    | 0 | 1 | 1 |
    | 1 | 0 | 1 |
    | 1 | 1 | 0 |

---

# 문자열 압축

- Run-length encoding 알고리즘
    - ABBBBBBBBA → A1B8A1