# Many to many relationship

한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

양쪽 모두에서 N:1 관계를 가짐


#### 💡 용어정리
<aside>

**Target model**

- 관계 필드를 가지지 않은 모델

**Source model**

- 관계 필드를 가진 모델
</aside>

<br>

### 중개 모델

- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

```python
class Reservation(models.Model):
		doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
		patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

```python
Reservation.objects.create(doctor=doctor1, patient=patient1)
```

<br>

---

# Django ManyToManyField

### → 중개 테이블 자동 형성 `{app_name}_{souce_mode}_{column_name}`

```python
class Patient(models.Model)
		doctors = models.ManyToManyField(Doctor)
		name = models.TextField()
```

→ `hospitals_patient_doctors` 중개 테이블 생성

- M:N 관계로 맺어진 두 테이블에는 변화가 없음

## 관계 형성

### `{source_model}.{column_name}.add({target_model})`

### `{target_model}.{source_model}_set.add({source_model})`

```python
# patient1 - doctor1에게 예약
patient1.doctors.add(doctor1)

# doctor1 - patient2를 예약
doctor1.patient_set.add(patient2)
```

## 관계 삭제

### `{source_model}.{column_name}.remove({target_model})`

### `{target_model}.{source_model}_set.remove({source_model})`

```python
# patient2 - doctor1 진료 예약 취소
patient2.doctors.remove(doctor1)

# doctor1 - patient2 진료 예약 취소
doctor1.patient_set.remove(patient2)
```

## 관계 테이블 확인

### `{source_model}.{column_name}.all()`

### `{target_model}.{source_model}_set.all()`

```python
# patient1 - 자신이 예약한 의사목록 확인
patient1.doctors.all()

# doctor1 - 자신의 예약된 환자목록 확인
doctor1.patient_set.all()
```

## `related_name`

- target model이 source model을 참조할 때 사용할 manager name

```python
class Patient(models.Model)
		doctors = models.ManyToManyField(Doctor, related_name='patients')
		name = models.TextField()
```

## `through` argument

- 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우

```python
class Patient(models.Model)
		doctors = models.ManyToManyField(Doctor, related_name='Reservation')
		name = models.TextField()

class Reservation(models.Model):
		doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
		patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
		symptom = models.TextField()
		reserved_at = models.DateTimeField(auto_now_add=True)		
```

```python
# 예약 생성
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()

# patient 객체를 통한 예약 생성
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

```

## `symmetrical`

- 기본값: True
    - _set 매니저를 추가하지 않음
    - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
    - 즉, 내가 당신의 친구라면 당신도 내 친구가 됨

```jsx
class Person(models.Model):
	friends = models.ManyToManyField('self')

```

## methods

### `add()`

- 지정된 객체를 관련 객체 집합에 추가
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

### `remove()`

- 관련 객체 집합에서 지정된 모델 개체를 제거
- 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
- 모델 인스턴스, 필드 값(PK)을 인자로 허용

<br>

---

# M:N (Article-User)

## Like 구현

```python
# articles/models.py

class Article(models.Model):
	user = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE)
	like_user = models.ManyToManyField(setting.AUTH_USER_MODEL, related_name='like_articles')
	title = models.CharField(max_length=10)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
```

```python
# articles/urls.py

urlpatterns = {
	...
	path('<int:article_pk>/likes/', views.likes, name='likes'),
}
```

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
	if request.user.is_authenticated:
		article = Article.objects.get(pk=article_pk)
	
		if article.like_users.filter(pk=request.user.pk).exists():
			article.like_users.remove(request.user)	
		else:
			article.like_users.add(request.user)
		return redirect('articles:index')
	return redirect('accounts:login')
```

### `.exists()`

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

<br>

---

# M:N (User-User)

## Profile 구현

```python
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
	User = get_user_model()
	person = User.objects.get(username=username)
	context = {
		'person': person,
	}
	return render(request, 'accounts/profile.html', context)
```

```python
# accounts/profile.html

<h1>{{ person.username }}님의 프로필</h1>
<hr>
<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
	<div>{{ article.title }}</div>
{% endfor %}

```

## Follow

```python
# accounts/models.py

class User(AbstractUser):
	followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```python
# accounts/urls.py

urlpatterns = [
	...
	path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
	if request.user.is_authenticated:
		User = get_user_model()
		person = User.objects.get(pk=user_pk)
		if person != request.user:
			if person.followers.filter(pk=request.user.pk).exists():
				person.followers.remove(request.user)
			else:
				person.followers.add(request.user)
		return redirect('accounts:profile', person.username)
	return redirect('accounts:login')
```

---

# Fixtures

## 데이터 추출 : dumpdata

`python [manage.py](http://manage.py) dumpdata --indent 4 articles.article articles.comment accounts.user > data.json`

`python [manage.py](http://manage.py) dumpdata --indent 4 > data.json`

→ 모든 모델을 하나의 json 파일로

## 데이터 입력 : loaddata

`python [manage.py](http://manage.py) loaddata data.json`

- 기본 경로
    - app_name/fixtures/
    - Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾음