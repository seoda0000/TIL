# JSON

JavaScript Object Notation

```jsx
{
    "students" : [
        {
            "name" : "harry",
            "age" : 30
        },
        {
            "name" : "Jerry"
            "age" : 30
        }
    ]
}
```

- Javascript 객체 문법으로 구조화된 데이터 교환 형식
- 파이썬, 자바스크립트, 자바 등 여러 언어에서 독립적으로 활용
- 객체 문법 뿐만 아니라 단순 배열`[1, 2, 3, 4]`, 문자열`"wow"`도 표현 가능

### 직렬화 Serialize

- 외부의 시스템에서도 사용할 수 있도록 바이트 형태로 데이터를 변환하는 기술

### 역직렬화 Deserialize

- 직렬화의 반대 과정
  - ex) json 파일을 객체로 변환 `JSON.parse`

```java
// JSON을 String으로 자동 변환해주는 어노테이션
public class ObjectDeserializer extends JsonDeserializer<String> {

    @Override
    public String deserialize(JsonParser p, DeserializationContext ctxt)
        throws IOException, JacksonException {
        return p.getCodec().readTree(p).toString();
    }
}
```

### JSON type

- javascript object와 유사하지만 undefined, 메서드를 포함하지 않는다.
- Number, String, Boolean, Array, Object, null

---

# XML

Extensible Markup Language

- 마크업 형태를 쓰는 데이터 교환 형식
- SEO(검색엔진최적화)을 위해 sitemap.xml로 구글에 제출
- 파이썬, 자바스크립트, 자바 등 여러 언어에서 독립적으로 활용

### 마크업 markup

```xml
<?xml version="1.0" encoding"UTF-8"?>
<MovieList>
    <Movie>
        <name>해리포터</name> <rate>4.9</rate>
    </Movie>
</MovieList>
```

- 태그 등을 이용하여 문서나 데이터의 구조를 나타내는 방법
- 속성부여도 가능하다.

### xml의 구성

1. 프롤로그 : 버전, 인코딩
2. 루트 요소 (단 하나만 존재)
3. 하위 요소들

### HTML과 XML의 차이

|               | HTML             | XML                   |
| ------------- | ---------------- | --------------------- |
| 용도          | 데이터 표시      | 데이터의 저장 및 전송 |
| 태그          | 미리 정의된 태그 | 고유한 태그 사용 가능 |
| 대소문자 구분 | X                | O                     |

---

# JSON과 XML의 차이

- xml이 더 무겁다 (닫힌 태그 때문)
- xml은 Javascript Object로 변환하기 위해 더 많은 노력이 필요하다.
