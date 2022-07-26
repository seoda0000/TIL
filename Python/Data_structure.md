
- [데이터 구조](#데이터-구조)
  * [순서가 있는 데이터 구조](#순서가-있는-데이터-구조)
    + [문자열 String Type](#문자열-String-Type)
    + [리스트 List](#리스트-List)
    + [튜플 Tuple](#튜플-Tuple)
  * [비시퀀스형 데이터 구조](#비시퀀스형-데이터-구조)
    + [셋 Set](#셋-Set)
    + [딕셔너리 Dictionary](#딕셔너리-Dictionary)
  * [얕은 복사와 깊은 복사](#얕은-복사와-깊은-복사)
    + [할당 Assignment](#할당-Assignment)
    + [얕은 복사 Shallow copy](#얕은-복사-Shallow-copy)
    + [깊은 복사 Deep copy](#깊은-복사-Deep-copy)

# 데이터 구조


- **데이터 구조의 활용**
    - 메서드(method) : 클래스 내부에 정의한 함수. 객체의 기능.
    - `데이터 구조.메서드()`
    - `주어.동사()`
- **파이썬 공식 문서의 표기법**
    - `str.replace(old, new[, count])`
    - `(필수[, 선택적 인자])`

- **문자열 메서드 모두 확인하기**
    - 파이썬 내장함수 dir을 통해 컨테이너가 가지고 있는 메서드를 확인할 수 있다.
    - ex) `dir(str)`

---

---

## 순서가 있는 데이터 구조

### 문자열 String Type

- 문자들의 나열
    - 모든 문자는 str type (immutable)
- **기존의 문자열을 변경하는 게 아님. 변경된 문자열을 새롭게 만들어서 반환!**

- **문자열 조회/탐색**

| 문법 | 설명 |
| --- | --- |
| `s.find(x)` | x의 첫번째 위치를 반환, 없으면 **-1 반환** |
| `s.index(x)` | x의 첫번째 위치를 반환, 없으면 **오류 발생** |
| `s.startswith(x)` | 접두문자가 x인지 확인 |

- **문자열 검증 메서드**

| 문법 | 설명 |
| --- | --- |
| `s.isalpha()` | 알파벳 문자 여부 (단순 알파벳이 아닌 유니코드 상 Letter. 한국어 포함) |
| `s.isspace` | 공백 여부 (\n, \t 포함)|
| `s.isupper()` | 대문자 여부 |
| `s.islower()` | 소문자 여부 |
| `s.istitle()` | 타이틀 형식 여부 (모든 단어가 첫 글자만 대문자) |
| `s.isnumeric()` | 수랑 비슷한 거까지 (로마자, 특수기호, 분수표현 등) |
| `s.isdigit()` | 숫자 (원형숫자기호)sdecimal() |
| `s.isdecimal()` | 숫자 0~9 |

- **문자열 변경 메서드**

| 문법 | 설명 |
| --- | --- |
| `s.replace(old, new[, count])` | 바꿀 글자를 새로운 글자로 변경. (count개만) |
| `s.strip([chars])` | 공백이나 특정 문자를 제거 |
| `s.split(sep=None, maxsplit=-1)` | 공백이나 특정 문자를 기준으로 분리 |
| `‘separator’.join([iterable])` | 구분자로 iterable을 합침 |
| `s.capitalize()` | 가장 첫 글자를 대문자로 변경 |
| `s.title()` | 띄어쓰기를 기준으로 가장 첫 글자를 대문자로 변경 |
| `s.upper()` | 모두 대문자로 변경 |
| `s.lower()` | 모두 소문자로 변경 |
| `s.swapcase()` | 대↔소문자 서로 변경 |

---

### 리스트 List

- 여러개의 값을 순서가 있는 구조로 저장
- 생성 이후 내용 변경 가능 (가변 자료형)

- **값 추가 및 삭제**

| 문법 | 설명 |
| --- | --- |
| `L.append(x)` | 리스트 마지막에 항목 x 추가 |
| `L.insert(i, x)` | 리스트 인덱스 i에 항목을 삽입. i가 len보다 길어도 맨 마지막에 삽입됨. |
| `L.extend(m)` | iterable을 리스트 끝에 추가 |
| `L.remove(x)` | 리스트의 가장 첫 x 제거. 항목이 없을 경우 Error |
| `L.pop()` | 리스트 가장 마지막 항목을 반환 후 제거 |
| `L.pop(i)` | 인덱스 i에 있는 항목을 반환 후 제거 |
| `L.clear()` | 요소 모두 삭제 |
- **탐색 및 정렬**

| 문법 | 설명 |
| --- | --- |
| `L.index(x, start, end)` | 가장 첫 x의 인덱스 반환 |
| `L.count(x)` | 리스트에 항목 x가 몇개 존재하는지 갯수 반환 |
| `L.sort()` | 원본 리스트를 정렬. None 반환 |
| `sorted(L)` | 정렬된 리스트를 반환 |
| `L.reverse()` | 원본 리스트 순서를 반대로 뒤집음. None 반환 |

---

### 튜플 Tuple

- 여러개의 값을 순서가 있는 구조로 저장하고 싶을 때
- 담고 있는 값 변경 불가 (불변 자료형)
- **값에 영향을 미치지 않는 메서드**만을 지원 **(확장 시 새로운 튜플을 반환)**

---

---

## 비시퀀스형 데이터 구조

### 셋 Set

- 중복되는 요소 없이, 순서에 상관 없는 데이터 묶음
- 수학에서의 집합 표현, 집합 연산 가능
- 요소 삽입 변경, 삭제 가능 (가변 자료형)
- set()으로 만들어야 함. {}로 만들면 Dictionary

- **추가 및 변경**

| 문법 | 설명 |
| --- | --- |
| `s.add(x)` | x가 s에 없다면 추가 |
| `s.update(*others)` | 여러 값을 추가 |
- **요소 삭제**

| 문법 | 설명 |
| --- | --- |
| `s.remove(x)` | 항목 x를 s에서 삭제. 항목이 존재하지 않을 경우 Key Error |
| `s.discard(x)` | 항복 x가 **s에 있는 경우 x를 삭제**. **없어도 에러 발생 x** |
| `s.pop()` | s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거. set이 비어있을 경우 Key Error |
| `s.clear()` | 모든 항목을 제거 |
- **집합 관련 메서드**

| 문법 | 설명 |
| --- | --- |
| `s.isdisjoint(t)` | s가 t의 항목을 하나라도 갖고 있지 않을 경우(교집합이 없을 때) True 반환 |
| `s.issubset(t)` | s가 t의 하위 셋인 경우 True 반환 |
| `s.issuperset(t)` | s가 t의 상위 셋인 경우 True 반환 |

---

### 딕셔너리 Dictionary

- key-value 쌍. 3.7부터는 ordered.
- key는 변경 불가 데이터(immutable)만 가능.

- **조회**

| 문법 | 설명 |
| --- | --- |
| `d.get(key[, default])` | key를 통해 value를 가져옴. **KeyError가 발생하지 않으며**, default 값은 **None**이 기본 |
| `d.setdefault(key[, default])` | key를 통해 value를 가져옴. key가 딕셔너리에 없을 경우, default 값을 갖는 key를 삽입한 후 default를 반환. **KeyError가 발생하지 않으며**, default 값은 **None**이 기본.  |
- **추가 및 삭제**

| 문법 | 설명 |
| --- | --- |
| `d.pop(key[, default])` | **key가 딕셔너리에 있으면 제거하고 해당 value를 반환**. default 값은 **KeyError**가 기본.  |
| `d.update(key=value)` | key, value로 덮어씀 |
| `d.clear()` | 모든 항목을 제거 |

```python
dic = {'apple' : '사과'}
dic.update(apple = '사과')  # str 타입이 아니어도 자동으로 key 인식함
print(dic)  # {'apple': '사과'}
```

- **기타 메서드**

| 문법 | 설명 |
| --- | --- |
| `d.keys()` | 모든 key를 담은 뷰를 반환 |
| `d.values()` | 모든 value를 담은 뷰를 반환 |
| `d.items()` | 모든 key-value 쌍을 담은 뷰를 반환 |
| `d.copy()` | d의 얕은 복사본을 반환 |

---

---

## 얕은 복사와 깊은 복사

### 할당 Assignment

- 대입 연산자 (=)
- **해당 객체에 대한 객체 참조를 복사** ⭐⭐⭐ (주소를 공유)

```python
original = [1, 2, 3]
copy_lst = original

copy_lst[0] = 'hello'
print(original, copy_lst)  # ['hello', 2, 3] ['hello', 2, 3]
```

```
a = 3
b = 4
b = a
a = 5
print(a, b) # 5, 3

# 복사 문제는 데이터를 모아놓은 곳만 해당됨.
```
### 얕은 복사 Shallow copy

- **연산된 결과만 복사** ⭐⭐⭐ (다른 주소)
    
    ```python
    original = [1, 2, 3]
    copy_lst = original[:]
    
    copy_lst[0] = 'hello'
    print(original, copy_lst)  # [1, 2, 3] ['hello', 2, 3]
    ```
    
- **주의사항** : 리스트의 원소가 주소를 참조하는 경우
    
    ```python
    original = [1, 2, ['a', 'b']]
    copy_lst = original[:]
    
    copy_lst[2][0] = 0
    print(original, copy_lst)  # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
    ```
    

### 깊은 복사 Deep copy

- 주소가 아닌 값만 온전히 복사

```python
import copy
original = [1, 2, ['a', 'b']]
copy_lst = copy.deepcopy(original)

copy_lst[2][0] = 0
print(original, copy_lst)  # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
```