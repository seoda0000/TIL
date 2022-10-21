# REST API



# HTTP

- HyperText Transfer Protocol : 클라이언트-서버 프로토콜
    - 요청(request)
        - 클라이언트에 의해 전송되는 메시지
    - 응답(response)
        - 서버에서 응답으로 전송되는 메시지
- 기본 특성
    - Stateless 무상태
    - Connectionless
- 쿠키와 세션을 통해 서버 상태를 요청과 연결되도록 함

<br>

## HTTP request methods

- HTTP verbs라고도 함. 자원에 대한 행위를 정의

### 1. GET

- 데이터를 가져올 때
- 서버에 리소스의 표현을 요청

### 2. POST

- DB를 hit해서 create할 때
- 데이터를 지정된 리소스에 제출. 서버의 상태를 변경.

### 3. PUT

- DB를 hit해서 update할 때 (모든 데이터를 수정)
- 요청한 주소의 리소스를 수정

### 4. DELETE

- DB를 hit해서 delete할 때
- 지정된 리소스를 삭제

### 5. PATCH

- DB를 hit해서 update할 때 (일부 데이터를 수정)

<br>

## HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
    1. Informational responses (100-199)
    2. Successful responses (200-299)
    3. Redirection responses (300-399)
    4. Client error responses (400-499)
    5. Server error responses (500-599)

<br>

---

# Identifying resources on the Web

- 웹에서 리소스를 식별하는 방법
- HTTP 요청의 대상을 리소스(resource, 자원)라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 URI로 식별됨

## URI

- Uniform Resource Identifier 통합 자원 식별자
- 인터넷에서 하나의 리소스를 가리키는 문자열
    - URN
        - 고유한 이름으로 자원을 식별 ex) ISBN
    - URL
        - 자원의 위치로 자원을 식별

## URL

- Uniform Resource Locator 통합 자원 위치
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속

<br>

## URL의 구조

`https://www.example.com:80/path/to/myfile.html/?key=value#quick-start`

### Scheme

`https`

- 브라우저가 리소스를 요청하는 데 사용해야할 프로토콜
- 기본적으로 웹은 HTTP(S)를 요구. 메일을 열기 위한 mailto:, 파일을 전송하기 위한 ftp: 등이 있음

### Authority

`www.example.com:80`

- 권한
1. Domain Name
    
    `www.example.com`
    
    - 요청 중인 웹 서버를 나타냄
    - 어떤 웹 서버가 요구되는지를 가리키며 직접 IP 주소를 사용하는 것도 가능
2. Port
    `:80`
    
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
    - HTTP 프로토콜의 표준 포트 (유일하게 생략 가능)
        - HTTP : 80
        - HTTPS : 443
    - Django의 경우 8000(80+00)이 기본 포트로 설정

### Path

`/path/to/myfile.html`

- 웹 서버의 리소스 경로
- 초기에는 실제 파일의 물리적 위치를 나타냈지만,
- 오늘날 실제 위치가 아닌 추상화된 형태의 구조를 표현

### Parameters

`?key=value`

- 웹 서버에 제공하는 추가적인 데이터
- 파라미터는 ‘&’ 기호로 구분되는 key-value 쌍 목록
- 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

### Anchor

`#quick-start`

- 리소스의 다른 부분에 대한 앵커
- 리소스 내부 일종의 북마크
- #이후의 fragment identifier(부분 식별자)은 서버에 전송되지 않음

<br>

---

# API

- Application Programming Interface 애플리케이션과 프로그래밍으로 소통하는 방법
    - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

## Web API

- 웹 서버 또는 웹 브라우저를 위한 API
- 여러 Open API 활용하는 추세
- API는 HTML, XML, JSON 등 다양한 타입의 데이터를 응답

<br>

---

# REST

- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- “소프트웨어 아키텍쳐 디자인 제약 모음”
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술
1. 자원을 식별 - URI
2. 자원에 대한 행위 - HTTP Methods
3. 자원을 표현(자원과 행위를 통해 궁극적으로 표현되는 추상화된 결과물) - JSON

## JSON

- lightweight data-interchange format
- JavaScript의 표기법을 따른 단순 문자열
- key-value 형태 : 사람이 읽고 쓰기 쉽고 기계가 해석하고 만들어내기 쉽다. 현재 API에서 가장 많이 사용하는 데이터 타입

<br>

---

# Response JSON

<aside>
💡 실습용 초기 데이터 입력

`python manage.py loaddata articles.json`

</aside>

## JsonResponse()를 사용한 JSON 응답

### `JsonResponse()`

- JSON-encoded response를 만드는 클래스
- `safe` parameter
    - 기본 값  True : dict 인스턴스만 허용
    - False : 모든 타입의 객체를 serialization 할 수 있다.

```python
# articles/views.py

from django.http.response import JsonResponse

def article_json_1(request):
	articles = Article.objects.all()
	article_json = []
	
	for article in articles:
		articles_json.append(
			{
				'id': article.pk,
				'title': article.title,
				'content': article.content,
			}
		)
	return JsonResponse(articles_json, safe=False)
	
```

<br>

## Django Serilizer를 사용한 JSON 응답

### Serialization

- 직렬화
- 데이터 구조나 객체 상태를 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    - 어떠한 언어나 환경에서도 **나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정**
    - 변환 포맷 : json, xml, yaml 등
- Serialization in Django : 변환 가능한 파이썬 데이터 타입으로 만들어줌

### DRF (Django REST framework)

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- ModelForm 클래스와 매우 유사하게 작동

```python
# articles/views.py

from django.http.response import HTTPResponse
from django.core import serializers

def article_json_2(request):
	articles = Article.objects.all()
	data = serializers.serialize('json', articles)
	return HTTPResponse(data, content_type='application/json')	
```

```python
class ArticleSerializer(serilaizers.ModelSerializer):
		
		class Meta:
				model = Article
				fields = '__all__'
```
<br>

## ModelSerializer

1. Model 정보에 맞춰 자동으로 필드를 생성
2. serializer에 대한 유효성 검사기를 자동으로 생성
3. `.create()` 및 `.update()` 의 간단한 기본 구현이 포함됨

### `many` option

- 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 `many=True`를 작성

```python
queryset = Book.objects.all()
serializer = BookSerializer(queryset, many=True)
serializer.data
'''
[
	{'id': 0, 'title': 'A'},
	{'id': 1, 'title': 'B'},
	{'id': 2, 'title': 'C'},
]
'''
```

<br>

---

# Build RESTful API - Single Model

### `api_view` decorator

- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용. 다른 메서드 요청에 대해서는 `405 Method Not Allowed`로 응답

⭐ DRF에서 `api_view` 데코레이터 작성은 필수

```python
# urls.py

urlpatterns = [
	...
	path('articles/<intLarticle_pk>/', views.article_detail),
]
```

```python
# views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers impor ArticleListSerializer

@api_view(['GET'])
def article_detail(request, article_pk):
	articles = Article.objects.get(pk=article_pk)
	serializer = ArticleSerializer(articles)
	return Response(serializer.data)
```

### `raise_exception`

- 유효하지 않은 데이터에 대해 예외 발생시키기
- 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리
    - 기본적으로 `HTTP 400` 응답을 반환

```python
# views.py

@api_view(['GET', 'POST'])
def article_detail(request, article_pk):
	...
	elif request.method == 'POST':
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
```

### DELETE

- 데이터 삭제 요청
- 삭제가 성공한 경우 `204 No Content` 상태 코드 응답

```python
# views.py

@api_view(['GET', 'POST', 'DELETE'])
def article_detail(request, article_pk):
	...
	elif request.method == 'DELETE':
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
```

### PUT

- 데이터 수정
- 수정이 성공한 경우 `200 OK` 상태 코드 응답

```python
# views.py

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
	...
	elif request.method == 'PUT':
		serializer = ArticleSerializer(article, data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
```

<br>

---

# Build RESTful API - N:1 Relation

<aside>
💡 Fixtures Data Load

`python [manage.py](http://manage.py) loaddata articles.json comments.json`

</aside>

### `.save()` 메서드

- 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- CommentSerializer를 통해 Serialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

```python
# views.py

@api_view(['POST'])
def comment_create(request, article_pk):
	article = Article.objects.get(pk=article_pk)
	serializer = CommentSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save(article=article)
		return Response(serializer.data, status.HTTP_201_CREATED)
```

→ Error

이유 : CommentSerializer에서 article field 데이터 또한 사용자로부터 입력 받도록 설정되어 있기 때문

→ 해결 방법 : 읽기 전용 필드 설정

<br>

### `read_only_fields`

- 외래 키 필드를 ‘읽기 전용 필드’로 설정

<aside>
💡 **읽기 전용 필드**

데이터를 전송하는 시점에 해당 필드를 **유효성 검사에서 제외**시키고 **데이터 조회 시에는 출력**하도록 함

</aside>

```python
# serializers.py

class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields = ('article',)
```

<br>

## N:1 - 역참조 데이터 조회

ex) 게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기

- serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

### 1. PrimaryKeyRelatedField()

```python
# serializers.py

class ArticleSerializer(serializers.ModelSerializer):
	comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Article
		fields = '__all__'
```

- [`models.py`](http://models.py)에서 `related_name`을 통해 이름 변경 가능
- 역참조 시 생성되는 comment_set을 override 할 수 있음

```python
# models.py

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	content = models.TextField()
```
<br>

### 2. Nested relationships

```python
# serializers.py

class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
	comment_set = CommentSerializer(many=True, read_only=True)

	class Meta:
		model = Article
		fields = '__all__'
```

- 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
- 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
- 두 클래스의 상/하 위치를 변경해야 함

<br>

## 새로운 필드 추가

ex) 게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기

```python
# serializers.py

class ArticleSerializer(serializers.ModelSerializer):
	comment_set = CommentSerializer(many=True, read_only=True)
	comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

	class Meta:
		model = Article
		fields = '__all__'
```
<br>

### `source`

- serializers field’s argument
- 필드를 채우는 데 사용할 속성의 이름
- 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음

<br>

### ⚠️ 주의사항

- 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않음

---

# Django shortcuts dunctions

- `django.shortcuts` 패키지 : 개발에 도움될 수 있는 여러 함수와 클래스 제공
    - `render()`, `redirect()`
    - `get_object_or_404()`, `get_list_or_404()` → 올바른 에러 전달을 위해

<br>

### `get_object_or_404()`

- 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 땐 기존 `DoesNotExist(500)` 예외 대신 `Http404`를 raise

```python
# views.py

from django.shortcuts import get_object_or_404

article = Article.objects.get(pk=article_pk)

# 위 코드를 다음과 같이 변경
article = get_object_or_404(Article, pk=article_pk)
```

<br>

### `get_list_or_404()`

- 모델 manager objects에서 filter()을 반환하고 해당 객체 목록이 없을 땐 Http404를 raise

```python
# views.py

from django.shortcuts import get_list_or_404

articles = Article.objects.all()

# 위 코드를 다음과 같이 변경
articles = get_list_or_404(Article)
```