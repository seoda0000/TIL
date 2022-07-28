- [에러/예외 처리](#에러/예외-처리)
  * [디버깅](#디버깅)
  * [에러와 예외](#에러와-예외)
    + [문법 에러 Syntax Error](#문법-에러-Syntax-Error)
    + [예외 Exception](#예외-Exception)
    + [파이썬 내장 예외 built-in-exceptions](#파이썬-내장-예외-built-in-exceptions)
  * [예외 처리](#예외-처리)
  * [예외 발생 시키기 Exception Raising](#예외-발생-시키기-Exception-Raising)

# 에러/예외 처리

- **버그란?**
    - 최초의 버그는 1945년 코볼 발명자 그레이스 호퍼가 발견
    - 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작
    - 이때부터 소프트웨어에서 발생하는 문제를 버그라고 부름

## 디버깅

- 잘못된 프로그램을 수정하는 것
- 에러 메세지가 발생하는 경우
    - 해당하는 위치를 찾아 해결
- 로직 에러가 발생하는 경우
    - 명시적인 에러 메세지 없이 예상과 다른 결과가 나온 경우
        - 정상적으로 동작하였던 코드 이후 작성된 코드 살펴보기
        - 전체 코드 살펴보기
        - 휴식을 가지기
        - 누군가에게 설명하기
- print 함수 사용
    - print(”<<<<<<<<<<<”, i)

## 에러와 예외

### 문법 에러 Syntax Error

- 발생하면 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어나갈 때 문제가 발생한 위치를 표현
- **Invalid syntax** 문법 오류
    - while
- **assign to literal** 잘못된 할당
    - sum = 5; sum([1, 2, 3])
- **EOL** (End of Line)
    - print(’hello
- **EOF** (End of File)
    - print(

### 예외 Exception

- 실행 중 예상치 못한 상황을 맞이하면 프로그램 실행을 멈춤
    - **문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러**
- 예외 타입이 메세지의 일부로 출력됨
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리 가능

- **ZeroDivisionError**
    - `10/0` : 0으로 나눌 때
- **NameError**
    - namespace 상에 이름이 없는 경우
- **TypeError**
    - `1+’1’` : 타입 불일치
    - `divmod()` : argument 누락
    - `divmod(1, 2, 3)` : argument 개수 초과
    - `random.sample(1, 2)` : argument type 불일치
- **ValueError**
    - `int('3.5')` : 타입은 올바르지만 값이 적절하지 않거나 없는 경우
- **IndexError**
    - `ex = [ ]; ex[2]` : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
- **KeyError**
    - `ex = {’IU’ : ‘좋은날’}; ex[’BTS’]` : 해당 키가 존재하지 않는 경우
- **ModuleNotFoundError**
    - 해당 모듈이 존재하지 않는 경우
- **ImportError**
    - 모듈은 있지만 존재하지 않는 클래스/함수를 가져오는 경우
- **KeyboardInterrupt**
    - 임의로 프로그램을 종료하였을 때
- **IndentationError**
    - Indentation이 적절하지 않는 경우

### 파이썬 내장 예외 built-in-exceptions

[Built-in Exceptions - Python 3.10.5 documentation](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

## 예외 처리

- try문/except문을 이용하여 예외처리
- **try**
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생하지 않으면 명령문 실행
- **except**
    - 예외가 발생하면 예외처리 명령문 실행
    - 순차적으로 체크. 가장 작은 범주의 에러부터 넣어야 한다.
- try문은 반드시 한 개 이상의 except문 필요

```python
try:
    ex = []
    print(ex[01])
except IndexError as err:
    print(f'{err}, 오류가 발생했습니다')
except:
    print('모르는 에러가 발생하였습니다.')
```

- **else** : try 문에서 예외가 발생하지 않으면 실행
- **finally** : 예외 발생 여부와 상관 없이 실행함

## 예외 발생 시키기 Exception Raising

- `raise <에러>('메세지')`
    - 예외를 강제로 발생시키기
- `assert Boolean expression, ‘error message’`
    - 상태를 검증하는데 사용. AssertionError 발생
    - 검증식이 거짓일 경우 발생