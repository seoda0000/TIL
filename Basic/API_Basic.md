# API 기초

## 요청과 응답

### 클라이언드(정보를 원한다) ↔ 서버(정보를 준다)

- 요청 : 주소
- 응답 : HTML 문서

---

## API (Application Programming Interface)

- 컴퓨터 처리를 쉽게 해주는 기능
- API를 활용하여 소통 가능
    
    ex) 
    
    [Agify.io | Predict the age of a name](https://agify.io/)
    

## json

- 데이터만 주고 받기 위한 표기법
- api의 응답으로 많이 이용

## request.library

- 파이썬 코드로 요청을 보내는 라이브러리

```python
pip install requests

import request

requests.get('url') #url에 정보를 달라는 요청을 보내줘

requests.get('url').json() #json 형식의 정보만 줘
```

```python
import requests

url = "https://api.agify.io/?name=liza"

rlt_data = requests.get(url).json()

print(rlt_data['name']) # data 중 name에 해당하는 값 출력
```

## API 사용의 핵심

### → “API 문서를 읽고 url을 만든다”